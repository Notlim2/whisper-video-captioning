@echo off
chcp 65001 > nul
REM Script para compilar a aplicação em .EXE standalone

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║  🔨 Compilador para Executável (.EXE)                     ║
echo ║  Whisper Video Captioning                                 ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

REM Verifica se o ambiente virtual existe
if not exist venv (
    echo ❌ Ambiente virtual não encontrado!
    echo.
    echo Execute primeiro: instalar_windows.bat
    echo.
    pause
    exit /b 1
)

REM Ativa o ambiente virtual
call venv\Scripts\activate.bat

echo 📦 Instalando PyInstaller...
pip install --upgrade PyInstaller pyinstaller-hooks-contrib >nul 2>&1

echo.
echo 🔍 Compilando aplicação Web...
echo.

REM Compila a aplicação web como .EXE
PyInstaller --onefile ^
    --windowed ^
    --icon=icon.ico ^
    --add-data "src/templates:templates" ^
    --add-data "config:config" ^
    --add-data "requirements.txt:." ^
    --hidden-import=flask ^
    --hidden-import=openai-whisper ^
    --hidden-import=whisper ^
    --hidden-import=pydub ^
    --hidden-import=moviepy ^
    --name "Whisper Video Captioning" ^
    src/web_app.py

if errorlevel 1 (
    echo.
    echo ❌ Erro ao compilar!
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ Compilação concluída!
echo.
echo 📁 Executável criado em: dist\Whisper Video Captioning.exe
echo.
echo ⚠️  IMPORTANTE:
echo    O executável inclui Python mas NÃO inclui FFmpeg!
echo    Para distribuir, você precisa:
echo    1. Colocar o FFmpeg.exe junto com o .EXE
echo    2. Ou criar um instalador que inclua ambos
echo.
pause
