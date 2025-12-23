#!/bin/bash

# Script para iniciar a GUI do Whisper Video Captioning

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

# Ativa o ambiente virtual
source venv/bin/activate

# Executa a GUI
python3 src/gui.py
