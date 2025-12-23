#!/bin/bash

# Script de Menu para Whisper Video Captioning
# Permite escolher qual interface usar

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

# Cores para terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Ativa environment
source venv/bin/activate 2>/dev/null || {
    echo -e "${RED}❌ Erro: Não foi possível ativar o ambiente virtual${NC}"
    echo "Crie com: python3 -m venv venv"
    exit 1
}

clear

echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════╗"
echo "║     🎬 Whisper Video Captioning - Menu Principal       ║"
echo "║          Legendagem Automática - pt-BR 🇧🇷             ║"
echo "╚════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo -e "${YELLOW}Escolha uma opção:${NC}\n"
echo "  1️⃣  Interface Web (Recomendada)"
echo "       - Acesso via navegador"
echo "       - Mais bonita e intuitiva"
echo "       - http://localhost:5000"
echo ""
echo "  2️⃣  Interface Desktop (Tkinter)"
echo "       - Aplicativo nativo"
echo "       - Sem necessidade de navegador"
echo "       - Seleção visual de arquivos"
echo ""
echo "  3️⃣  Interface CLI (Linha de Comando)"
echo "       - Mais rápido"
echo "       - Ideal para automação"
echo "       - Configurações padrão"
echo ""
echo "  4️⃣  Ver Manual de Uso"
echo "       - Guia completo"
echo "       - Exemplos e dicas"
echo ""
echo "  5️⃣  Sair"
echo ""
echo -e "${YELLOW}Digite o número da opção:${NC}"
read -p "> " option

case $option in
    1)
        echo -e "\n${GREEN}🚀 Iniciando Interface Web...${NC}\n"
        python3 src/web_app.py
        ;;
    2)
        echo -e "\n${GREEN}🚀 Iniciando Interface Desktop...${NC}\n"
        python3 src/gui.py
        ;;
    3)
        echo -e "\n${GREEN}🚀 Iniciando Interface CLI...${NC}\n"
        python3 src/main.py
        ;;
    4)
        echo -e "\n${YELLOW}📖 Abrindo Manual...${NC}\n"
        if command -v less &> /dev/null; then
            less MANUAL.md
        else
            cat MANUAL.md
        fi
        ;;
    5)
        echo -e "\n${YELLOW}👋 Até logo!${NC}\n"
        exit 0
        ;;
    *)
        echo -e "\n${RED}❌ Opção inválida!${NC}\n"
        exit 1
        ;;
esac
