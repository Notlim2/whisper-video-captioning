@echo off
REM ============================================================
REM LIMPEZA COMPLETA + COMPILAÇÃO
REM Whisper Video Captioning
REM ============================================================
REM Este script resolve TODOS os problemas conhecidos de compilação

chcp 65001 >nul
setlocal enabledelayedexpansion
cls

echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║  🔨 COMPILAÇÃO COMPLETA + LIMPEZA AUTOMÁTICA             ║
echo ║  Whisper Video Captioning                                ║
echo ╚══════════════════════════════════════════════════════════╝
echo.
echo Esta ferramenta irá:
echo   1. Limpar COMPLETAMENTE builds anteriores
echo   2. Remover TODOS os arquivos .spec antigos
echo   3. Compilar o executável do zero
echo   4. Copiar FFmpeg (se encontrado)
echo   5. Copiar documentação
echo.
timeout /t 3

REM ============================================================
REM VERIFICAÇÕES INICIAIS
REM ============================================================

echo [1/5] Verificando requisitos...

python --version >nul 2>&1
if !errorlevel! neq 0 (
    echo.
    echo ❌ ERRO: Python não está instalado ou não está no PATH!
    echo.
    echo Solução:
    echo   1. Instale Python de: https://www.python.org/
    echo   2. IMPORTANTE: Marque "Add Python to PATH"
    echo   3. Reinicie o Command Prompt
    echo.
    pause
    exit /b 1
)
echo   ✅ Python encontrado

REM ============================================================
REM LIMPEZA AGRESSIVA
REM ============================================================

echo.
echo [2/5] Limpando builds anteriores (limpeza agressiva)...

REM Termina processos que possam estar usando os arquivos
taskkill /F /IM "Whisper Video Captioning.exe" 2>nul

REM Remove as pastas
for /d %%D in (build dist __pycache__ .pytest_cache .spec) do (
    if exist "%%D" (
        echo   🗑️ Removendo %%D/
        rmdir /s /q "%%D" 2>nul
    )
)

REM Aguarda um pouco para o sistema liberar os arquivos
timeout /t 2 /nobreak >nul

REM Remove TODOS os arquivos .spec do projeto
echo   🗑️ Removendo arquivos .spec antigos...
for /r . %%F in (*.spec) do (
    if exist "%%F" (
        echo     • %%~nxF
        del /q "%%F" 2>nul
    )
)

echo   ✅ Limpeza concluída

REM ============================================================
REM VERIFICAÇÃO PÓS-LIMPEZA
REM ============================================================

if exist "build" (
    echo.
    echo ⚠️  AVISO: Pasta 'build' ainda existe!
    echo    Isto pode gerar conflitos...
    echo    Fechando aplicações que usam a pasta...
    timeout /t 2 /nobreak >nul
    rmdir /s /q "build" 2>nul
)

REM ============================================================
REM INSTALA PYINSTALLER SE NECESSÁRIO
REM ============================================================

echo.
echo [3/5] Verificando PyInstaller...

python -m pip show pyinstaller >nul 2>&1
if !errorlevel! neq 0 (
    echo   ⚠️ PyInstaller não encontrado. Instalando...
    python -m pip install --upgrade pyinstaller -q
    if !errorlevel! neq 0 (
        echo   ❌ Erro ao instalar PyInstaller
        pause
        exit /b 1
    )
    echo   ✅ PyInstaller instalado
) else (
    echo   ✅ PyInstaller encontrado
)

REM ============================================================
REM COMPILAÇÃO PRINCIPAL
REM ============================================================

echo.
echo [4/5] COMPILANDO EXECUTÁVEL...
echo   (isto pode levar de 5 a 15 minutos)
echo.

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
    --hidden-import=openai-whisper ^
    --hidden-import=numpy ^
    --hidden-import=librosa ^
    --collect-all=flask ^
    --collect-all=whisper ^
    src\web_app.py

if !errorlevel! neq 0 (
    echo.
    echo ❌ ERRO NA COMPILAÇÃO!
    echo.
    echo Informações de debug:
    echo   • Verifique se src\web_app.py existe
    echo   • Verifique se src\templates\ existe
    echo   • Verifique se config\ existe
    echo   • Tente fechar todas as aplicações abertas
    echo   • Tente executar este script novamente
    echo.
    echo Se o problema persistir:
    echo   1. Delete MANUALMENTE as pastas: build, dist
    echo   2. Delete TODOS os arquivos .spec
    echo   3. Tente novamente
    echo.
    pause
    exit /b 1
)

REM ============================================================
REM VERIFICAÇÃO DO EXECUTÁVEL
REM ============================================================

if not exist "dist\Whisper Video Captioning.exe" (
    echo.
    echo ❌ ERRO: Executável não foi criado!
    echo   Procurado em: dist\Whisper Video Captioning.exe
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ Executável criado com sucesso!
for /F "tokens=*" %%A in ('dir /b "dist\Whisper Video Captioning.exe"') do (
    set "EXE_FILE=dist\Whisper Video Captioning.exe"
)

REM ============================================================
REM CÓPIA DE ARQUIVOS AUXILIARES
REM ============================================================

echo.
echo [5/5] Preparando distribuição...

REM FFmpeg
where ffmpeg >nul 2>&1
if !errorlevel! equ 0 (
    for /f "delims=" %%A in ('where ffmpeg') do (
        echo   📋 Copiando FFmpeg...
        copy "%%A" "dist\ffmpeg.exe" >nul
        echo   ✅ FFmpeg copiado
    )
) else (
    echo   ⚠️ FFmpeg não encontrado no PATH
    echo   (Você pode copiar ffmpeg.exe manualmente depois)
)

REM Documentação
for %%F in (COMECE_AQUI.txt LEIA_ME.txt README_WINDOWS.md SOLUCAO_ERRO_ICONE.txt) do (
    if exist "%%F" (
        copy "%%F" "dist\" >nul
        echo   ✅ %%F copiado
    )
)

REM ============================================================
REM RESULTADO FINAL
REM ============================================================

echo.
echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║  ✨ COMPILAÇÃO CONCLUÍDA COM SUCESSO!                   ║
echo ╚══════════════════════════════════════════════════════════╝
echo.
echo 📁 Pasta: dist\
echo.
echo Arquivos criados:
if exist "dist\Whisper Video Captioning.exe" (
    for /F "usebackq" %%A in ('dist\Whisper Video Captioning.exe') do (
        set /A size=%%~zA/1024/1024
        echo   ✅ Whisper Video Captioning.exe (!size! MB)
    )
)

if exist "dist\ffmpeg.exe" (
    echo   ✅ ffmpeg.exe
) else (
    echo   ⚠️ ffmpeg.exe (não encontrado - copie manualmente)
)

echo   ✅ Documentação
echo.
echo 🚀 PRÓXIMOS PASSOS:
echo.
echo 1️⃣  Se ffmpeg.exe não estiver em dist\:
echo    • Baixe: https://ffmpeg.org/download.html
echo    • Extraia ffmpeg.exe
echo    • Copie para: dist\ffmpeg.exe
echo.
echo 2️⃣  Teste a aplicação:
echo    • Execute: dist\Whisper Video Captioning.exe
echo    • Verifique que a interface abre no navegador
echo.
echo 3️⃣  Crie o instalador:
echo    • Execute: criar_package.bat
echo    • Isto gera uma pasta pronta para distribuir
echo.
echo 4️⃣  Distribua:
echo    • Compacte a pasta gerada em ZIP
echo    • Envie para seus amigos!
echo.
echo ═══════════════════════════════════════════════════════════
echo.
pause
