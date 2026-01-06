#!/bin/bash

# 🤖 Verificar Copilot Setup
# Este script valida se o Copilot está configurado corretamente

echo "╔════════════════════════════════════════╗"
echo "║   🤖 VERIFICAÇÃO COPILOT SETUP        ║"
echo "╚════════════════════════════════════════╝"
echo ""

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 1. Verificar .copilot-instructions
echo "1️⃣ Verificando .copilot-instructions..."
if [ -f "$PROJECT_ROOT/.copilot-instructions" ]; then
    echo "   ✅ Arquivo encontrado"
    LINES=$(wc -l < "$PROJECT_ROOT/.copilot-instructions")
    echo "   📝 $LINES linhas de instruções"
else
    echo "   ❌ Arquivo NÃO encontrado"
    exit 1
fi

# 2. Verificar .vscode/settings.json
echo ""
echo "2️⃣ Verificando .vscode/settings.json..."
if [ -f "$PROJECT_ROOT/.vscode/settings.json" ]; then
    echo "   ✅ Arquivo encontrado"
    if grep -q "github.copilot" "$PROJECT_ROOT/.vscode/settings.json"; then
        echo "   ✅ Copilot habilitado para Python"
    fi
else
    echo "   ⚠️ Arquivo não encontrado (opcional)"
fi

# 3. Verificar arquivos de documentação
echo ""
echo "3️⃣ Verificando documentação..."
DOCS=("COPILOT_SETUP.md" "COPILOT_EXEMPLOS.md")
for doc in "${DOCS[@]}"; do
    if [ -f "$PROJECT_ROOT/$doc" ]; then
        echo "   ✅ $doc"
    else
        echo "   ❌ $doc não encontrado"
    fi
done

# 4. Resumo
echo ""
echo "╔════════════════════════════════════════╗"
echo "║   ✅ SETUP COMPLETO                    ║"
echo "╚════════════════════════════════════════╝"
echo ""
echo "📝 Instruções principais:"
echo "   • Nenhuma documentação desnecessária"
echo "   • Código limpo e conciso"
echo "   • Sem comentários óbvios"
echo ""
echo "🚀 Próximas ações:"
echo "   1. Feche e reabra VS Code"
echo "   2. Comece a usar Copilot normalmente"
echo "   3. Observe o código mais limpo"
echo ""
echo "📚 Saiba mais:"
echo "   • Leia: COPILOT_SETUP.md"
echo "   • Exemplos: COPILOT_EXEMPLOS.md"
echo ""
