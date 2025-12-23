@echo off
REM Script de compilação - Whisper Video Captioning
REM Versão simplificada sem dependência de ícone

chcp 65001 >nul
cls

echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║  🔨 Compilador - Whisper Video Captioning              ║
echo ║  VERSÃO 2.0 (Sem erros de ícone)                       ║
echo ╚════════════════════════════════════════════════════════╝
echo.

REM Verifica Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado!
    pause
    exit /b 1
)
echo ✅ Python encontrado

REM Verifica PyInstaller
pip list | findstr "pyinstaller" >nul
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  PyInstaller não está instalado
    echo    Instalando...
    pip install pyinstaller >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❌ Erro ao instalar PyInstaller
        pause
        exit /b 1
    )
)
echo ✅ PyInstaller disponível

echo.
echo 🧹 Limpando builds anteriores...
REM Deleta pastas de build antigas
if exist build rmdir /s /q build >nul
if exist dist rmdir /s /q dist >nul
if exist build.spec del /q build.spec >nul 2>&1
if exist *.spec del /q *.spec >nul 2>&1

echo ✅ Limpeza concluída

echo.
echo 📦 Compilando (isto pode levar alguns minutos)...
echo.

REM COMANDO PRINCIPAL - SEM ÍCONE
pyinstaller ^
    --onefile ^
    --windowed ^
    --name "Whisper Video Captioning" ^
    --add-data "src\templates;templates" ^
    --add-data "config;config" ^
    --hidden-import=flask ^
    --hidden-import=whisper ^
    --hidden-import=moviepy ^
    --hidden-import=pydub ^
    --collect-all=flask ^
    --collect-all=whisper ^
    src\web_app.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ ERRO na compilação!
    echo.
    echo Dicas:
    echo  1. Verifique se todos os .spec foram removidos
    echo  2. Feche qualquer aplicação usando dist/
    echo  3. Tente novamente
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ Executável criado com sucesso!
echo.

REM Copia FFmpeg se encontrar
echo 📋 Procurando FFmpeg...
where ffmpeg >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ FFmpeg encontrado - copiando...
    for /f "delims=" %%A in ('where ffmpeg') do (
        copy "%%A" "dist\ffmpeg.exe" >nul
    )
    echo ✅ FFmpeg copiado para dist\
) else (
    echo ⚠️  FFmpeg não encontrado
    echo    Você precisará copiar ffmpeg.exe para dist\ manualmente
    echo    Baixe em: https://ffmpeg.org/download.html
)

REM Copia documentação
echo ✅ Copiando documentação...
if exist "COMECE_AQUI.txt" copy "COMECE_AQUI.txt" "dist\" >nul
if exist "LEIA_ME.txt" copy "LEIA_ME.txt" "dist\" >nul
if exist "README_WINDOWS.md" copy "README_WINDOWS.md" "dist\" >nul

echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║  ✨ COMPILAÇÃO CONCLUÍDA!                              ║
echo ╚════════════════════════════════════════════════════════╝
echo.
echo 📁 Arquivos em: dist\
echo.
echo ✅ Whisper Video Captioning.exe
if exist "dist\ffmpeg.exe" (
    echo ✅ ffmpeg.exe
) else (
    echo ⚠️  ffmpeg.exe (não encontrado - copie manualmente)
)
echo.
echo 📋 PRÓXIMOS PASSOS:
echo.
echo 1. Se ffmpeg.exe não estiver em dist\:
echo    • Baixe: https://ffmpeg.org/download.html
echo    • Copie ffmpeg.exe para: dist\
echo.
echo 2. Teste:
echo    • Execute: dist\Whisper Video Captioning.exe
echo    • Verifique que a interface abre
echo.
echo 3. Distribua:
echo    • Compacte a pasta dist\ em ZIP
echo    • Envie para seus amigos!
echo.
pause
