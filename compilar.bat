@echo off
chcp 65001 > nul
REM Automatiza todo o processo de compilação para .EXE

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║  🔨 Compilador Automático para Executável                 ║
echo ║  Whisper Video Captioning                                 ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

REM Verifica Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado!
    pause
    exit /b 1
)

REM Verifica se está no diretório certo
if not exist src\web_app.py (
    echo ❌ Não estou no diretório certo!
    echo Execute da raiz do projeto
    pause
    exit /b 1
)

REM Pergunta se quer criar estrutura FFmpeg
echo.
echo 📥 Configuração do FFmpeg
echo.
echo Você já tem FFmpeg em ffmpeg\bin\ffmpeg.exe?
echo.
set /p ffmpeg_ready="Digite 'sim' se sim, ou 'não' para seguir sem: "

if /i "%ffmpeg_ready%"=="não" (
    echo.
    echo ⚠️  FFmpeg não será incluído automaticamente
    echo    Você precisará:
    echo    1. Baixar de: https://ffmpeg.org/download.html
    echo    2. Colocar em: ffmpeg\bin\ffmpeg.exe
    echo.
    pause
)

REM Ativa ambiente virtual se existir
if exist venv (
    call venv\Scripts\activate.bat
) else (
    echo.
    echo ⚠️  Ambiente virtual não encontrado
    echo    Criando novo ambiente...
    python -m venv venv
    call venv\Scripts\activate.bat
)

REM Instala PyInstaller
echo.
echo 📦 Instalando PyInstaller...
pip install pyinstaller --quiet

REM Executa script Python de compilação
echo.
echo 🔨 Iniciando compilação...
python compilar_executavel.py

if errorlevel 1 (
    echo.
    echo ❌ Erro durante compilação!
    pause
    exit /b 1
)

echo.
echo ✅ Compilação concluída com sucesso!
echo.
echo 📁 Arquivos gerados em: dist\
echo.
echo Próximos passos:
echo   1. Verifique se dist\Whisper Video Captioning.exe existe
echo   2. Teste executando o .EXE
echo   3. Copie para uma pasta com ffmpeg.exe
echo   4. Compacte em ZIP
echo   5. Distribua!
echo.
echo Para mais detalhes, leia: COMPILAR_PARA_EXE.txt
echo.
pause
