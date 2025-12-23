@echo off
chcp 65001 > nul
title Whisper Video Captioning

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║  🎬 Whisper Video Captioning                              ║
echo ║  Legendagem Automática de Vídeos em Português             ║
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

REM Verifica qual interface o usuário quer usar
echo.
echo 📱 Escolha como deseja usar a aplicação:
echo.
echo   1 - Interface Web (recomendado)
echo   2 - Interface Gráfica Desktop
echo   3 - Interface de Linha de Comando
echo   4 - Sair
echo.
set /p choice="Digite sua opção (1-4): "

if "%choice%"=="1" (
    echo.
    echo 🚀 Iniciando Interface Web...
    echo.
    echo 📱 Abra seu navegador em: http://localhost:5000
    echo.
    echo Para parar, pressione Ctrl+C
    echo.
    python src/web_app.py
) else if "%choice%"=="2" (
    echo.
    echo 🚀 Iniciando Interface Gráfica...
    echo.
    python src/gui.py
    if errorlevel 1 (
        echo.
        echo ❌ Erro ao iniciar interface gráfica
        echo.
        pause
    )
) else if "%choice%"=="3" (
    echo.
    echo 🚀 Iniciando Interface de Linha de Comando...
    echo.
    python src/main.py
    if errorlevel 1 (
        echo.
        echo ❌ Erro ao iniciar aplicação
        echo.
        pause
    )
) else if "%choice%"=="4" (
    exit /b 0
) else (
    echo.
    echo ❌ Opção inválida!
    echo.
    pause
    goto :inicio
)

pause
