@echo off
chcp 65001 > nul
REM Instalador para Windows - Whisper Video Captioning

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║  🎬 Whisper Video Captioning - Instalador Windows          ║
echo ║  Legendagem Automática de Vídeos em Português              ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não foi encontrado!
    echo.
    echo 📥 Você precisa instalar o Python 3.8+ primeiro:
    echo    👉 Acesse: https://www.python.org/downloads/
    echo    👉 Baixe a versão mais recente
    echo    👉 IMPORTANTE: Marque a opção "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado!
echo.

REM Verifica se FFmpeg está instalado
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo ❌ FFmpeg não foi encontrado!
    echo.
    echo 📥 Você precisa instalar o FFmpeg:
    echo    👉 Acesse: https://ffmpeg.org/download.html
    echo    👉 Baixe a versão "Full" para Windows
    echo    👉 Extraia e adicione à variável PATH
    echo    👉 Ou use: choco install ffmpeg (se tiver Chocolatey)
    echo.
    pause
    exit /b 1
)

echo ✅ FFmpeg encontrado!
echo.

REM Cria ambiente virtual
echo 📦 Criando ambiente virtual Python...
if not exist venv (
    python -m venv venv
    echo ✅ Ambiente virtual criado
) else (
    echo ✅ Ambiente virtual já existe
)

echo.
echo 📚 Instalando dependências (isso pode levar alguns minutos)...
echo.

REM Ativa ambiente virtual e instala dependências
call venv\Scripts\activate.bat
pip install --upgrade pip setuptools wheel >nul 2>&1
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ❌ Erro ao instalar dependências!
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ Todas as dependências instaladas com sucesso!
echo.
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║  ✨ INSTALAÇÃO CONCLUÍDA COM SUCESSO!                     ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo 🚀 Para iniciar o aplicativo, execute:
echo    - Execute: rodar_app.bat
echo    - Ou: python src/gui.py (para interface gráfica)
echo    - Ou: python src/web_app.py (para web browser)
echo.
echo 📖 Para mais informações, leia: LEIA_ME.txt
echo.
pause
