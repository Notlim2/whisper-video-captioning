#!/bin/bash
# =============================================================================
# Iniciador da Aplicação - Whisper Video Captioning (Linux/Mac)
# =============================================================================

set -e

echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║  🎬 WHISPER VIDEO CAPTIONING - LAUNCHER (Linux/Mac)      ║"
echo "║  Iniciando aplicação...                                  ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Detecta diretório atual
APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$APP_DIR"

echo "📁 Diretório: $APP_DIR"
echo ""

# Verifica Python
echo "📋 Verificando requisitos..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado!"
    echo ""
    echo "Instale com:"
    echo "  • Ubuntu/Debian: sudo apt install python3 python3-venv python3-pip"
    echo "  • Fedora: sudo dnf install python3"
    echo "  • Mac: brew install python3"
    exit 1
fi
echo "✅ Python3 encontrado: $(python3 --version)"

# Verifica FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  FFmpeg não encontrado!"
    echo ""
    echo "Instale com:"
    echo "  • Ubuntu/Debian: sudo apt install ffmpeg"
    echo "  • Fedora: sudo dnf install ffmpeg"
    echo "  • Mac: brew install ffmpeg"
    echo ""
    read -p "Deseja continuar mesmo assim? (s/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        exit 1
    fi
else
    echo "✅ FFmpeg encontrado: $(ffmpeg -version | head -n 1)"
fi

echo ""

# Ativa virtual environment se existir
if [ -d "venv" ]; then
    echo "✅ Virtual environment encontrado"
    echo ""
    echo "🚀 Ativando virtual environment..."
    source venv/bin/activate
    echo "✅ Virtual environment ativado"
else
    echo "⚠️  Virtual environment não encontrado"
    echo "   Criando..."
    python3 -m venv venv
    source venv/bin/activate
    echo "   Instalando dependências..."
    pip install -q -r requirements.txt
    echo "✅ Dependências instaladas"
fi

echo ""
echo "🚀 Iniciando aplicação..."
echo ""

# Inicia aplicação
python3 src/web_app.py

# Cleanup
deactivate 2>/dev/null || true
