#!/usr/bin/env python3
"""
Script para compilar Whisper Video Captioning em executável .EXE standalone
Inclui Python, dependências e FFmpeg
"""

import os
import sys
import subprocess
import shutil
import zipfile
from pathlib import Path

def run_command(cmd, description):
    """Executa comando e mostra progresso"""
    print(f"\n{'='*60}")
    print(f"📦 {description}")
    print(f"{'='*60}\n")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"\n❌ Erro ao executar: {description}")
        sys.exit(1)
    print(f"✅ {description} concluída!")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║  🔨 Compilador Profissional - Whisper Video Captioning    ║
║  Gera executável .EXE com tudo incluído                  ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Verifica se está no diretório certo
    if not os.path.exists("src/web_app.py"):
        print("❌ Execute este script da raiz do projeto!")
        sys.exit(1)
    
    # Verificações
    print("\n📋 Verificando requisitos...")
    
    if not shutil.which("pyinstaller"):
        print("❌ PyInstaller não está instalado!")
        print("   Execute: pip install pyinstaller")
        sys.exit(1)
    print("✅ PyInstaller encontrado")
    
    if not shutil.which("ffmpeg"):
        print("⚠️  FFmpeg não encontrado no PATH")
        print("   Você precisará fornecer FFmpeg.exe junto com o EXE")
    print("✅ Verificações concluídas")
    
    # Limpa builds anteriores
    print("\n🧹 Limpando builds anteriores...")
    for folder in ["build", "dist", "__pycache__"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    print("✅ Limpeza concluída")
    
    # Compila aplicação
    cmd = (
        'pyinstaller --onefile '
        '--windowed '
        '--name "Whisper Video Captioning" '
        '--add-data "src/templates;templates" '
        '--add-data "config;config" '
        '--add-data "requirements.txt;." '
        '--hidden-import=flask '
        '--hidden-import=openai-whisper '
        '--hidden-import=whisper '
        '--hidden-import=pydub '
        '--hidden-import=moviepy '
        '--hidden-import=pathlib '
        '--hidden-import=json '
        '--collect-all=flask '
        '--collect-all=whisper '
        '--collect-all=torch '
        'src/web_app.py'
    )
    
    run_command(cmd, "Compilação do executável")
    
    # Verifica resultado
    exe_path = Path("dist/Whisper Video Captioning.exe")
    if not exe_path.exists():
        print(f"\n❌ Executável não foi criado em {exe_path}")
        sys.exit(1)
    
    print(f"\n✅ Executável criado: {exe_path}")
    print(f"   Tamanho: {exe_path.stat().st_size / 1024 / 1024:.1f} MB")
    
    # Copia arquivos auxiliares
    print("\n📁 Copiando arquivos auxiliares...")
    
    # Copia FFmpeg se encontrar
    if shutil.which("ffmpeg"):
        ffmpeg_path = shutil.which("ffmpeg")
        dest = Path("dist/ffmpeg.exe")
        shutil.copy(ffmpeg_path, dest)
        print(f"✅ FFmpeg copiado: {dest}")
    else:
        print("⚠️  FFmpeg não encontrado - você precisará fornecer ffmpeg.exe")
    
    # Copia documentação
    docs = [
        "COMECE_AQUI.txt",
        "LEIA_ME.txt",
        "README_WINDOWS.md"
    ]
    
    for doc in docs:
        if os.path.exists(doc):
            shutil.copy(doc, Path("dist") / doc)
            print(f"✅ {doc} copiado")
    
    # Cria pasta templates se necessário
    if os.path.exists("src/templates"):
        if os.path.exists("dist/templates"):
            shutil.rmtree("dist/templates")
        shutil.copytree("src/templates", "dist/templates")
        print("✅ Templates copiados")
    
    # Cria arquivo info
    info = """
╔═══════════════════════════════════════════════════════════╗
║  🎉 COMPILAÇÃO CONCLUÍDA COM SUCESSO!                    ║
╚═══════════════════════════════════════════════════════════╝

📁 Pasta: dist/

Arquivos para distribuir:
  ✅ Whisper Video Captioning.exe (aplicação)
  ✅ ffmpeg.exe (se copiado automaticamente)
  ✅ Documentação (COMECE_AQUI.txt, etc)

Se FFmpeg não foi copiado automaticamente:
  1. Baixe FFmpeg: https://ffmpeg.org/download.html
  2. Coloque ffmpeg.exe na mesma pasta do EXE

Para distribuir:
  1. Crie uma pasta com:
     - Whisper Video Captioning.exe
     - ffmpeg.exe
     - COMECE_AQUI.txt
     - LEIA_ME.txt
  
  2. Compacte em ZIP
  
  3. Envie para seus amigos!

Seu amigo precisa apenas:
  1. Descompactar
  2. Clicar no .EXE
  3. Pronto!

═══════════════════════════════════════════════════════════
    """
    
    print(info)
    
    # Salva informações
    with open("dist/COMPILACAO_INFO.txt", "w", encoding="utf-8") as f:
        f.write(info)
    
    print("✨ Tudo pronto para distribuição!")

if __name__ == "__main__":
    main()
