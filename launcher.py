#!/usr/bin/env python3
"""
Wrapper para iniciar Whisper Video Captioning
Detecta FFmpeg automaticamente
"""

import os
import sys
import subprocess
from pathlib import Path

def find_ffmpeg():
    """Procura por ffmpeg no PATH ou no diretório local"""
    
    # Tenta encontrar no PATH do sistema
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, 
                              timeout=2)
        if result.returncode == 0:
            return 'ffmpeg'
    except:
        pass
    
    # Tenta no diretório local
    local_ffmpeg = Path(__file__).parent / 'ffmpeg.exe'
    if local_ffmpeg.exists():
        return str(local_ffmpeg)
    
    # Tenta em subpasta
    local_ffmpeg = Path(__file__).parent / 'ffmpeg' / 'bin' / 'ffmpeg.exe'
    if local_ffmpeg.exists():
        return str(local_ffmpeg)
    
    return None

def main():
    # Verifica FFmpeg
    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        print("❌ FFmpeg não encontrado!")
        print("\nOpcões:")
        print("1. Instale FFmpeg de: https://ffmpeg.org/download.html")
        print("2. Coloque ffmpeg.exe no mesmo diretório deste arquivo")
        print("3. Adicione FFmpeg ao PATH do Windows")
        input("\nPressione Enter para sair...")
        sys.exit(1)
    
    # Define variável de ambiente
    os.environ['FFMPEG_BINARY'] = ffmpeg
    
    # Inicia a aplicação web
    try:
        from src.web_app import app
        print("\n🚀 Iniciando Whisper Video Captioning...")
        print("📱 Abra seu navegador em: http://localhost:5000")
        print("\nPara parar, pressione Ctrl+C")
        app.run(host='127.0.0.1', port=5000, debug=False)
    except Exception as e:
        print(f"❌ Erro ao iniciar: {e}")
        input("\nPressione Enter para sair...")
        sys.exit(1)

if __name__ == "__main__":
    main()
