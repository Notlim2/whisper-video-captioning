@echo off
REM ============================================================
REM Iniciador da Aplicação - Whisper Video Captioning
REM ============================================================

setlocal enabledelayedexpansion
chcp 65001 >nul 2>&1
cls

echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║  🎬 WHISPER VIDEO CAPTIONING                           ║
echo ║  Iniciando aplicação...                                ║
echo ╚════════════════════════════════════════════════════════╝
echo.

REM Detecta diretório atual
set APP_DIR=%~dp0
cd /d "%APP_DIR%"

echo 📁 Diretório: %APP_DIR%

REM Verifica Python
python --version >nul 2>&1
if !errorlevel! neq 0 (
    echo.
    echo ❌ Python não encontrado!
    echo.
    echo Instale Python de: https://www.python.org/
    echo IMPORTANTE: Marque "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado

REM Verifica FFmpeg
ffmpeg -version >nul 2>&1
if !errorlevel! neq 0 (
    REM Procura FFmpeg localmente
    if exist "ffmpeg.exe" (
        echo ✅ FFmpeg encontrado localmente
    ) else (
        echo.
        echo ⚠️  FFmpeg não encontrado!
        echo.
        echo Opções:
        echo   1. Coloque ffmpeg.exe nesta pasta
        echo   2. Instale FFmpeg: https://ffmpeg.org/download.html
        echo.
        pause
        exit /b 1
    )
) else (
    echo ✅ FFmpeg encontrado
)

REM Verifica Virtual Environment
if exist "venv\Scripts\activate.bat" (
    echo ✅ Virtual Environment encontrado
    echo.
    echo 🚀 Iniciando aplicação...
    echo.
    call venv\Scripts\activate.bat
    python src\web_app.py
) else (
    echo ⚠️ Virtual Environment não encontrado
    echo.
    echo 🚀 Iniciando aplicação (modo alternativo)...
    echo.
    python src\web_app.py
)

if !errorlevel! equ 0 (
    exit /b 0
) else (
    echo.
    echo ❌ Erro ao iniciar a aplicação
    echo.
    pause
    exit /b 1
)
