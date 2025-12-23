#!/usr/bin/env python3
"""
Launcher para Whisper Video Captioning
Inicia a aplicação web e abre automaticamente no navegador
Compatível com Windows e Linux
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path
import platform

def find_ffmpeg():
    """Procura por FFmpeg no sistema"""
    # Procura no PATH
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, 
                              timeout=5)
        if result.returncode == 0:
            return True
    except:
        pass
    
    # Procura em locais comuns do Windows
    if platform.system() == 'Windows':
        common_paths = [
            Path(sys.executable).parent / 'ffmpeg.exe',
            Path.cwd() / 'ffmpeg.exe',
            Path.cwd().parent / 'ffmpeg.exe',
            Path('C:/ffmpeg/bin/ffmpeg.exe'),
        ]
        for path in common_paths:
            if path.exists():
                return True
    
    return False

def main():
    """Função principal"""
    
    print("\n" + "="*70)
    print("🎬 WHISPER VIDEO CAPTIONING - LAUNCHER")
    print("="*70)
    
    # Verifica FFmpeg
    print("\n📋 Verificando dependências...")
    if not find_ffmpeg():
        print("⚠️  FFmpeg não encontrado!")
        print("   Instale FFmpeg para continuar:")
        print("   • Windows: https://ffmpeg.org/download.html")
        print("   • Linux: sudo apt install ffmpeg")
        print("   • macOS: brew install ffmpeg")
        print("\n   OU coloque ffmpeg.exe na mesma pasta do executável")
        input("\nPressione ENTER para sair...")
        sys.exit(1)
    print("✅ FFmpeg encontrado")
    
    # Detecta diretório da aplicação
    app_dir = Path(__file__).parent.absolute()
    web_app_dir = app_dir / 'src' if (app_dir / 'src').exists() else app_dir
    web_app_file = web_app_dir / 'web_app.py'
    
    print(f"📁 Diretório da aplicação: {app_dir}")
    print(f"📄 Arquivo principal: {web_app_file}")
    
    if not web_app_file.exists():
        print(f"\n❌ Arquivo não encontrado: {web_app_file}")
        input("Pressione ENTER para sair...")
        sys.exit(1)
    
    # Ativa virtual environment se existir
    venv_path = Path(app_dir) / 'venv'
    if platform.system() == 'Windows':
        activate_script = venv_path / 'Scripts' / 'activate.bat'
        if activate_script.exists():
            print(f"\n✅ Virtual environment encontrado")
            os.system(f'cd /d "{app_dir}" && "{activate_script}" && python "{web_app_file}"')
        else:
            print(f"\n⚠️ Virtual environment não encontrado")
            print(f"   Procurando em: {venv_path}")
            os.system(f'cd /d "{app_dir}" && python "{web_app_file}"')
    else:
        activate_script = venv_path / 'bin' / 'activate'
        if activate_script.exists():
            print(f"\n✅ Virtual environment encontrado")
            os.system(f'cd "{app_dir}" && source "{activate_script}" && python "{web_app_file}"')
        else:
            print(f"\n⚠️ Virtual environment não encontrado")
            os.system(f'cd "{app_dir}" && python "{web_app_file}"')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Aplicação encerrada pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        input("Pressione ENTER para sair...")
