from flask import Flask, render_template, request, jsonify
from pathlib import Path
import os
import sys
import threading
import json

# Adiciona config ao path
sys.path.insert(0, '../config')

from video_processor import VideoProcessor
from transcriber import Transcriber
from subtitle_generator import SubtitleGenerator
from utils import load_env, validate_file

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max

# Carrega configurações
try:
    from config.settings import (
        LANGUAGE, MODEL_NAME, TASK, BEST_OF, 
        BEAM_SIZE, TEMPERATURE, NO_SPEECH_THRESHOLD,
        MAX_AUDIO_LENGTH
    )
    DEFAULT_CONFIG = {
        "language": LANGUAGE,
        "model": MODEL_NAME,
        "task": TASK,
        "best_of": BEST_OF,
        "beam_size": BEAM_SIZE,
        "temperature": TEMPERATURE,
        "no_speech_threshold": NO_SPEECH_THRESHOLD,
        "max_audio_length": MAX_AUDIO_LENGTH,
    }
except:
    DEFAULT_CONFIG = {
        "language": "pt",
        "model": "base",
        "task": "transcribe",
        "best_of": 5,
        "beam_size": 5,
        "temperature": 0.0,
        "no_speech_threshold": 0.6,
        "max_audio_length": 30,
    }

# Variáveis globais para tracking de processamento
processing_status = {
    "is_processing": False,
    "progress": [],
    "current_file": None
}


@app.route('/')
def index():
    return render_template('index.html', config=DEFAULT_CONFIG)


@app.route('/api/config', methods=['GET'])
def get_config():
    return jsonify(DEFAULT_CONFIG)


@app.route('/api/browse', methods=['POST'])
def browse_files():
    """API para navegar arquivos do sistema (seguro)"""
    print("=== /api/browse chamado ===")
    try:
        data = request.json
        print(f"Data recebida: {data}")
        
        if not data:
            return jsonify({"error": "Nenhum caminho fornecido"}), 400
        
        current_path = data.get('path', str(Path.home())).strip()
        print(f"Caminho solicitado: {current_path}")
        
        if not current_path:
            current_path = str(Path.home())
        
        # Segurança: evita subir além do home
        try:
            current_path = Path(current_path).expanduser().resolve()
            print(f"Caminho resolvido: {current_path}")
        except Exception as e:
            print(f"Erro ao resolver caminho: {e}")
            return jsonify({"error": f"Caminho inválido: {str(e)}"}), 400
        
        # Verifica se existe
        if not current_path.exists():
            print(f"Caminho não existe: {current_path}")
            return jsonify({"error": f"Diretório não encontrado: {current_path}"}), 404
        
        if not current_path.is_dir():
            print(f"Caminho não é diretório: {current_path}")
            return jsonify({"error": f"Caminho não é um diretório: {current_path}"}), 400
        
        items = []
        print(f"Listando arquivos em: {current_path}")
        
        try:
            for item in sorted(current_path.iterdir()):
                try:
                    if item.is_dir():
                        items.append({
                            'name': item.name,
                            'path': str(item),
                            'type': 'dir'
                        })
                    elif item.is_file():
                        ext = item.suffix.lower()
                        if ext in ['.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv']:
                            try:
                                size_mb = item.stat().st_size / 1024 / 1024
                            except:
                                size_mb = 0
                            items.append({
                                'name': item.name,
                                'path': str(item),
                                'type': 'video',
                                'size': f'{size_mb:.2f}MB'
                            })
                except Exception as item_error:
                    print(f"Erro processando item {item.name}: {item_error}")
                    continue
        
        except Exception as e:
            print(f"Erro ao listar arquivos: {e}")
            import traceback
            traceback.print_exc()
            return jsonify({"error": f"Erro ao listar arquivos: {str(e)}"}), 500
        
        print(f"Encontrados {len(items)} itens")
        result = {
            'current_path': str(current_path),
            'parent_path': str(current_path.parent),
            'items': items
        }
        print(f"Retornando: {result}")
        return jsonify(result)
        
    except Exception as e:
        print(f"Erro geral em /api/browse: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Erro interno: {str(e)}"}), 500


@app.route('/api/process', methods=['POST'])
def process_video_api():
    """API para processar vídeo"""
    if processing_status["is_processing"]:
        return jsonify({"error": "Já há um processamento em andamento"}), 400
    
    try:
        data = request.json
        video_file = data.get('video_file', '').strip()
        output_dir = data.get('output_dir', '').strip()
        config = data.get('config', DEFAULT_CONFIG)
        
        # Validações
        if not video_file:
            return jsonify({"error": "Arquivo de vídeo não foi selecionado"}), 400
        
        video_path = Path(video_file).expanduser().resolve()
        if not video_path.exists():
            return jsonify({"error": f"Arquivo de vídeo não encontrado: {video_file}"}), 400
        
        if not video_path.is_file():
            return jsonify({"error": f"Caminho não é um arquivo: {video_file}"}), 400
        
        if not output_dir:
            return jsonify({"error": "Diretório de saída não foi selecionado"}), 400
        
        output_path = Path(output_dir).expanduser().resolve()
        if not output_path.exists():
            return jsonify({"error": f"Diretório de saída não encontrado: {output_dir}"}), 400
        
        if not output_path.is_dir():
            return jsonify({"error": f"Caminho de saída não é um diretório: {output_dir}"}), 400
        
        # Inicia processamento em thread separada
        thread = threading.Thread(
            target=process_video_thread,
            args=(str(video_path), str(output_path), config),
            daemon=True
        )
        thread.start()
        
        return jsonify({"status": "Processamento iniciado"})
    
    except Exception as e:
        return jsonify({"error": f"Erro ao processar requisição: {str(e)}"}), 400


@app.route('/api/status', methods=['GET'])
def get_status():
    """Retorna status do processamento"""
    return jsonify(processing_status)


@app.route('/api/clear-log', methods=['POST'])
def clear_log():
    """Limpa o log"""
    processing_status["progress"] = []
    return jsonify({"status": "Log limpo"})


def add_log(message):
    """Adiciona mensagem ao log"""
    processing_status["progress"].append(message)
    print(message)


def process_video_thread(video_file, output_dir, config):
    """Thread para processar o vídeo"""
    try:
        processing_status["is_processing"] = True
        processing_status["current_file"] = video_file
        processing_status["progress"] = []
        
        add_log("\n" + "="*60)
        add_log("INICIANDO PROCESSAMENTO")
        add_log("="*60)
        add_log(f"Vídeo: {video_file}")
        add_log(f"Saída: {output_dir}")
        add_log(f"Modelo: {config['model']}")
        add_log(f"Idioma: {config['language']}")
        add_log(f"Tamanho máximo de áudio: {config.get('max_audio_length', 30)}s")
        add_log("")
        
        # Inicializa processadores
        video_processor = VideoProcessor(video_file)
        transcriber = Transcriber(
            language=config['language'],
            model_size=config['model']
        )
        subtitle_generator = SubtitleGenerator()
        
        # Extrai áudio
        add_log("1️⃣ Extraindo áudio do vídeo...")
        audio_file = video_processor.extract_audio()
        add_log(f"   ✓ Áudio extraído")
        
        # Verifica tamanho máximo do áudio
        max_audio_length = config.get('max_audio_length', 30)
        import wave
        try:
            with wave.open(audio_file, 'rb') as wav_file:
                frames = wav_file.getnframes()
                rate = wav_file.getframerate()
                duration = frames / float(rate)
                
                add_log(f"\n📊 Informações do áudio:")
                add_log(f"   - Duração: {duration:.1f}s")
                add_log(f"   - Limite: {max_audio_length}s")
                
                if duration > max_audio_length:
                    add_log(f"\n⚠️ AVISO: Áudio excede o limite!")
                    add_log(f"   A transcrição será cortada em {max_audio_length}s")
        except Exception as e:
            add_log(f"   ⚠️ Não foi possível verificar duração: {str(e)}")
        
        # Transcreve
        add_log("\n2️⃣ Transcrevendo áudio...")
        transcribed_text = transcriber.transcribe_audio(audio_file)
        add_log(f"   ✓ Transcrição concluída")
        
        # Gera legendas
        add_log("\n3️⃣ Gerando legendas...")
        subtitles = subtitle_generator.generate_subtitles(transcribed_text)
        
        # Salva legendas no diretório especificado
        video_name = Path(video_file).stem
        output_file = os.path.join(output_dir, video_name + ".srt")
        subtitle_generator.save_subtitles(subtitles, output_file)
        add_log(f"   ✓ Legendas salvas em: {output_file}")
        
        # Remove áudio
        add_log("\n4️⃣ Limpando arquivos temporários...")
        if os.path.exists(audio_file):
            Path(audio_file).unlink()
            add_log(f"   ✓ Arquivo de áudio removido")
        
        add_log("\n" + "="*60)
        add_log("✅ PROCESSAMENTO CONCLUÍDO COM SUCESSO!")
        add_log("="*60)
        
    except Exception as e:
        add_log(f"\n❌ ERRO: {str(e)}")
    
    finally:
        processing_status["is_processing"] = False


def main():
    load_env()
    print("🚀 Iniciando servidor web...")
    print("📱 Abra seu navegador em: http://localhost:5000")
    app.run(debug=False, host='127.0.0.1', port=5000, threaded=True)


if __name__ == "__main__":
    main()
