import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import os
import sys
import threading

# Adiciona config ao path
sys.path.insert(0, '../config')

from video_processor import VideoProcessor
from transcriber import Transcriber
from subtitle_generator import SubtitleGenerator
from utils import load_env, validate_file


class WhisperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Whisper Video Captioning - pt-BR")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Carrega configurações
        try:
            from config.settings import (
                LANGUAGE, MODEL_NAME, TASK, BEST_OF, 
                BEAM_SIZE, TEMPERATURE, NO_SPEECH_THRESHOLD,
                MAX_AUDIO_LENGTH
            )
            self.config = {
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
            self.config = {
                "language": "pt",
                "model": "base",
                "task": "transcribe",
                "best_of": 5,
                "beam_size": 5,
                "temperature": 0.0,
                "no_speech_threshold": 0.6,
                "max_audio_length": 30,
            }
        
        self.video_file = tk.StringVar()
        self.output_dir = tk.StringVar(value=str(Path.home() / "Downloads"))
        self.is_processing = False
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configura a interface gráfica"""
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar weight para redimensionamento
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # ===== SEÇÃO 1: SELEÇÃO DE VÍDEO =====
        video_frame = ttk.LabelFrame(main_frame, text="1. Selecionar Vídeo", padding="10")
        video_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        video_frame.columnconfigure(1, weight=1)
        
        ttk.Label(video_frame, text="Arquivo de Vídeo:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(video_frame, textvariable=self.video_file, state="readonly").grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=5
        )
        ttk.Button(video_frame, text="Procurar...", command=self.select_video).grid(
            row=0, column=2, padx=5
        )
        
        # ===== SEÇÃO 2: CONFIGURAÇÃO DE SAÍDA =====
        output_frame = ttk.LabelFrame(main_frame, text="2. Diretório de Saída", padding="10")
        output_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        output_frame.columnconfigure(1, weight=1)
        
        ttk.Label(output_frame, text="Pasta de Saída:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(output_frame, textvariable=self.output_dir, state="readonly").grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=5
        )
        ttk.Button(output_frame, text="Procurar...", command=self.select_output_dir).grid(
            row=0, column=2, padx=5
        )
        
        # ===== SEÇÃO 3: CONFIGURAÇÕES DO WHISPER =====
        config_frame = ttk.LabelFrame(main_frame, text="3. Configurações do Whisper", padding="10")
        config_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        config_frame.columnconfigure(1, weight=1)
        
        # Modelo
        ttk.Label(config_frame, text="Modelo:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.model_var = tk.StringVar(value=self.config["model"])
        model_combo = ttk.Combobox(
            config_frame, 
            textvariable=self.model_var,
            values=["tiny", "base", "small", "medium", "large"],
            state="readonly",
            width=15
        )
        model_combo.grid(row=0, column=1, sticky=tk.W, padx=5)
        ttk.Label(config_frame, text="(tiny=39MB, base=140MB, small=244MB, medium=1.5GB, large=2.9GB)").grid(
            row=0, column=2, sticky=tk.W, padx=5
        )
        
        # Idioma
        ttk.Label(config_frame, text="Idioma:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.language_var = tk.StringVar(value=self.config["language"])
        language_combo = ttk.Combobox(
            config_frame,
            textvariable=self.language_var,
            values=["pt", "en", "es", "fr"],
            state="readonly",
            width=15
        )
        language_combo.grid(row=1, column=1, sticky=tk.W, padx=5)
        
        # Tarefa
        ttk.Label(config_frame, text="Tarefa:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.task_var = tk.StringVar(value=self.config["task"])
        task_combo = ttk.Combobox(
            config_frame,
            textvariable=self.task_var,
            values=["transcribe", "translate"],
            state="readonly",
            width=15
        )
        task_combo.grid(row=2, column=1, sticky=tk.W, padx=5)
        
        # Beam Size
        ttk.Label(config_frame, text="Beam Size (precisão):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.beam_var = tk.IntVar(value=self.config["beam_size"])
        beam_scale = ttk.Scale(
            config_frame,
            from_=1, to=10,
            orient=tk.HORIZONTAL,
            variable=self.beam_var,
            command=lambda v: self.beam_label.config(text=f"Beam Size: {int(float(v))}")
        )
        beam_scale.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=5)
        self.beam_label = ttk.Label(config_frame, text=f"Beam Size: {self.config['beam_size']}")
        self.beam_label.grid(row=3, column=2, sticky=tk.W)
        
        # Best Of
        ttk.Label(config_frame, text="Best Of (qualidade):").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.best_of_var = tk.IntVar(value=self.config["best_of"])
        best_of_scale = ttk.Scale(
            config_frame,
            from_=1, to=10,
            orient=tk.HORIZONTAL,
            variable=self.best_of_var,
            command=lambda v: self.best_of_label.config(text=f"Best Of: {int(float(v))}")
        )
        best_of_scale.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=5)
        self.best_of_label = ttk.Label(config_frame, text=f"Best Of: {self.config['best_of']}")
        self.best_of_label.grid(row=4, column=2, sticky=tk.W)
        
        # Temperatura
        ttk.Label(config_frame, text="Temperatura (aleatoriedade):").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.temperature_var = tk.DoubleVar(value=self.config["temperature"])
        temp_scale = ttk.Scale(
            config_frame,
            from_=0, to=1,
            orient=tk.HORIZONTAL,
            variable=self.temperature_var,
            command=lambda v: self.temp_label.config(text=f"Temp: {float(v):.2f}")
        )
        temp_scale.grid(row=5, column=1, sticky=(tk.W, tk.E), padx=5)
        self.temp_label = ttk.Label(config_frame, text=f"Temp: {self.config['temperature']:.2f}")
        self.temp_label.grid(row=5, column=2, sticky=tk.W)
        
        # Tamanho Máximo do Áudio
        ttk.Label(config_frame, text="Tamanho Máx. Áudio (segundos):").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.max_audio_var = tk.IntVar(value=self.config["max_audio_length"])
        max_audio_scale = ttk.Scale(
            config_frame,
            from_=60, to=3600,
            orient=tk.HORIZONTAL,
            variable=self.max_audio_var,
            command=lambda v: self.max_audio_label.config(text=f"Máx: {int(float(v))}s ({int(float(v))//60}m)")
        )
        max_audio_scale.grid(row=6, column=1, sticky=(tk.W, tk.E), padx=5)
        max_audio_display = f"Máx: {self.config['max_audio_length']}s ({self.config['max_audio_length']//60}m)"
        self.max_audio_label = ttk.Label(config_frame, text=max_audio_display)
        self.max_audio_label.grid(row=6, column=2, sticky=tk.W)
        
        # ===== SEÇÃO 4: PROGRESS BAR =====
        progress_frame = ttk.LabelFrame(main_frame, text="4. Processamento", padding="10")
        progress_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        progress_frame.columnconfigure(0, weight=1)
        
        self.progress = ttk.Progressbar(
            progress_frame, 
            mode='indeterminate',
            length=400
        )
        self.progress.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)
        
        self.status_text = tk.Text(
            progress_frame,
            height=8,
            width=80,
            state="disabled",
            wrap=tk.WORD
        )
        self.status_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        scrollbar = ttk.Scrollbar(progress_frame, orient=tk.VERTICAL, command=self.status_text.yview)
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        self.status_text['yscrollcommand'] = scrollbar.set
        
        progress_frame.rowconfigure(1, weight=1)
        
        # ===== BOTÕES =====
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        button_frame.columnconfigure(0, weight=1)
        
        self.process_btn = ttk.Button(
            button_frame,
            text="▶ Processar",
            command=self.process_video
        )
        self.process_btn.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Limpar", command=self.clear_log).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Sair", command=self.root.quit).pack(side=tk.RIGHT, padx=5)
    
    def select_video(self):
        """Seleciona arquivo de vídeo"""
        file_path = filedialog.askopenfilename(
            title="Selecionar vídeo",
            filetypes=[
                ("Video Files", "*.mp4 *.avi *.mov *.mkv *.webm"),
                ("All Files", "*.*")
            ]
        )
        if file_path:
            self.video_file.set(file_path)
            self.log(f"✓ Vídeo selecionado: {file_path}")
    
    def select_output_dir(self):
        """Seleciona diretório de saída"""
        dir_path = filedialog.askdirectory(title="Selecionar diretório de saída")
        if dir_path:
            self.output_dir.set(dir_path)
            self.log(f"✓ Diretório de saída: {dir_path}")
    
    def log(self, message):
        """Adiciona mensagem ao log"""
        self.status_text.config(state="normal")
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.status_text.config(state="disabled")
        self.root.update()
    
    def clear_log(self):
        """Limpa o log"""
        self.status_text.config(state="normal")
        self.status_text.delete(1.0, tk.END)
        self.status_text.config(state="disabled")
    
    def process_video(self):
        """Processa o vídeo em thread separada"""
        if not self.video_file.get():
            messagebox.showerror("Erro", "Por favor, selecione um vídeo!")
            return
        
        if self.is_processing:
            messagebox.showwarning("Aviso", "Já há um processamento em andamento!")
            return
        
        # Inicia processamento em thread separada
        thread = threading.Thread(target=self._process_video_thread, daemon=True)
        thread.start()
    
    def _process_video_thread(self):
        """Thread de processamento"""
        try:
            self.is_processing = True
            self.process_btn.config(state="disabled")
            self.progress.start()
            
            video_file = self.video_file.get()
            output_dir = self.output_dir.get()
            
            # Validar arquivo
            if not validate_file(video_file):
                self.log("✗ Arquivo de vídeo inválido!")
                return
            
            # Validar diretório de saída
            output_dir_path = Path(output_dir)
            if not output_dir_path.exists():
                self.log(f"✗ Diretório de saída inválido: {output_dir}")
                return
            
            if not output_dir_path.is_dir():
                self.log(f"✗ Caminho de saída não é um diretório: {output_dir}")
                return
            
            self.log("\n" + "="*60)
            self.log("INICIANDO PROCESSAMENTO")
            self.log("="*60)
            self.log(f"Vídeo: {video_file}")
            self.log(f"Saída: {output_dir}")
            self.log(f"Modelo: {self.model_var.get()}")
            self.log(f"Idioma: {self.language_var.get()}")
            self.log(f"Tamanho máx. áudio: {self.max_audio_var.get()}s")
            self.log("")
            
            # Inicializa processadores
            video_processor = VideoProcessor(video_file)
            transcriber = Transcriber(
                language=self.language_var.get(),
                model_size=self.model_var.get()
            )
            subtitle_generator = SubtitleGenerator()
            
            # Extrai áudio
            self.log("1️⃣ Extraindo áudio do vídeo...")
            audio_file = video_processor.extract_audio()
            self.log(f"   ✓ Áudio extraído")
            
            # Transcreve
            self.log("\n2️⃣ Transcrevendo áudio...")
            transcribed_text = transcriber.transcribe_audio(audio_file)
            self.log(f"   ✓ Transcrição concluída")
            
            # Gera legendas
            self.log("\n3️⃣ Gerando legendas...")
            subtitles = subtitle_generator.generate_subtitles(transcribed_text)
            
            # Salva legendas no diretório especificado
            video_name = Path(video_file).stem
            output_file = os.path.join(output_dir, video_name + ".srt")
            subtitle_generator.save_subtitles(subtitles, output_file)
            self.log(f"   ✓ Legendas salvas em: {output_file}")
            
            # Remove áudio
            self.log("\n4️⃣ Limpando arquivos temporários...")
            if os.path.exists(audio_file):
                Path(audio_file).unlink()
                self.log(f"   ✓ Arquivo de áudio removido")
            
            self.log("\n" + "="*60)
            self.log("✅ PROCESSAMENTO CONCLUÍDO COM SUCESSO!")
            self.log("="*60)
            
            messagebox.showinfo(
                "Sucesso",
                f"Legendas salvas em:\n{output_file}"
            )
        
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            self.log(f"\n❌ ERRO: {str(e)}")
            self.log(f"\nDetalhes:\n{error_details}")
            messagebox.showerror("Erro", f"Erro durante o processamento:\n{str(e)}\n\nVeja o log para mais detalhes.")
        
        finally:
            self.is_processing = False
            self.process_btn.config(state="normal")
            self.progress.stop()


def main():
    load_env()
    root = tk.Tk()
    app = WhisperGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
