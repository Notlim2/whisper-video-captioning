#!/usr/bin/env python3
"""
Script para compilar Whisper Video Captioning em executável .EXE
Versão simplificada e robusta - sem dependência de ícone
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def main():
    print("""
╔════════════════════════════════════════════════════════╗
║  🔨 Compilador - Whisper Video Captioning              ║
║  Versão 2.0 (Sem dependência de ícone)                 ║
╚════════════════════════════════════════════════════════╝
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
        print("⚠️  FFmpeg não encontrado - copie ffmpeg.exe após compilação")
    
    # Limpa builds ANTERIORES (IMPORTANTE!)
    print("\n🧹 Limpando builds anteriores...")
    
    # Remove pastas de build
    for folder in ["build", "dist", "__pycache__"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"  ✅ {folder}/ removido")
    
    # Remove TODOS os arquivos .spec (ISSO É IMPORTANTE!)
    for spec_file in Path(".").glob("*.spec"):
        spec_file.unlink()
        print(f"  ✅ {spec_file.name} removido (arquivo antigo)")
    
    for spec_file in Path("src").glob("*.spec"):
        spec_file.unlink()
        print(f"  ✅ {spec_file.name} removido (arquivo antigo)")
    
    print("✅ Limpeza concluída - arquivos antigos removidos")
    
    # Comando PyInstaller (SEM ícone, sem --spec, sem dependências problemáticas)
    print("\n📦 Compilando (isto pode levar 5-10 minutos)...\n")
    
    cmd = (
        'pyinstaller '
        '--onefile '
        '--windowed '
        '--name "Whisper Video Captioning" '
        '--add-data "src/templates;templates" '
        '--add-data "config;config" '
        '--hidden-import=flask '
        '--hidden-import=whisper '
        '--hidden-import=moviepy '
        '--hidden-import=pydub '
        '--hidden-import=openai-whisper '
        '--collect-all=flask '
        '--collect-all=whisper '
        'src/web_app.py'
    )
    
    result = subprocess.run(cmd, shell=True)
    
    if result.returncode != 0:
        print("\n❌ ERRO na compilação!")
        print("\nDicas para resolver:")
        print("  1. Limpe a pasta 'build' manualmente")
        print("  2. Certifique-se que todos os .spec foram removidos")
        print("  3. Tente novamente")
        sys.exit(1)
    
    # Verifica resultado
    exe_path = Path("dist/Whisper Video Captioning.exe")
    if not exe_path.exists():
        print(f"\n❌ EXE não criado! Procure em dist/")
        sys.exit(1)
    
    exe_size = exe_path.stat().st_size / 1024 / 1024
    print(f"\n✅ SUCESSO! Executável criado:")
    print(f"   📁 {exe_path}")
    print(f"   📊 Tamanho: {exe_size:.1f} MB")
    
    # Copia FFmpeg
    print("\n📋 Preparando distribuição...")
    ffmpeg_copied = False
    
    if shutil.which("ffmpeg"):
        ffmpeg_src = shutil.which("ffmpeg")
        ffmpeg_dst = Path("dist/ffmpeg.exe")
        try:
            shutil.copy(ffmpeg_src, ffmpeg_dst)
            ffmpeg_copied = True
            print(f"✅ FFmpeg copiado automaticamente")
        except Exception as e:
            print(f"⚠️  Não foi possível copiar FFmpeg: {e}")
    
    # Copia documentação
    for doc in ["COMECE_AQUI.txt", "LEIA_ME.txt", "README_WINDOWS.md"]:
        if os.path.exists(doc):
            try:
                shutil.copy(doc, f"dist/{doc}")
                print(f"✅ {doc} copiado")
            except:
                pass
    
    # Resumo final
    print(f"""
╔════════════════════════════════════════════════════════╗
║  ✨ COMPILAÇÃO CONCLUÍDA!                              ║
╚════════════════════════════════════════════════════════╝

📁 Arquivos em: dist/

Conteúdo:
  ✅ Whisper Video Captioning.exe
""")
    
    if ffmpeg_copied:
        print("  ✅ ffmpeg.exe (incluído automático)")
    else:
        print("  ⚠️  ffmpeg.exe (COPIE MANUALMENTE - veja instruções abaixo)")
    
    print("""
📋 PRÓXIMOS PASSOS:

1️⃣ Se ffmpeg.exe não foi copiado:
   • Baixe: https://ffmpeg.org/download.html
   • Extraia ffmpeg.exe
   • Copie para a pasta dist/

2️⃣ Teste localmente:
   • Execute: dist/Whisper Video Captioning.exe
   • Verifique que a interface abre

3️⃣ Distribua:
   • Compacte a pasta dist/ em ZIP
   • Envie para seus amigos
   • Eles só precisam descompactar e clicar no EXE!

═════════════════════════════════════════════════════════
    """)

if __name__ == "__main__":
    main()
