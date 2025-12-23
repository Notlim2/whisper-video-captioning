@echo off
chcp 65001 > nul
REM Cria package final com tudo pronto para distribuir

echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║  📦 Criador de Package para Distribuição                  ║
echo ║  Whisper Video Captioning                                 ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.

REM Verifica se dist existe
if not exist dist (
    echo ❌ Pasta dist\ não encontrada!
    echo.
    echo Execute primeiro: compilar.bat
    echo.
    pause
    exit /b 1
)

REM Verifica se o EXE foi criado
if not exist "dist\Whisper Video Captioning.exe" (
    echo ❌ Executável não encontrado em dist\!
    echo.
    pause
    exit /b 1
)

echo ✅ Executável encontrado
echo.

REM Cria pasta temporária
set "temp_dir=WhisperVideoCaptioning_Package"
echo 📁 Criando pasta temporária: %temp_dir%
if exist "%temp_dir%" rmdir /s /q "%temp_dir%"
mkdir "%temp_dir%"

REM Copia arquivos necessários
echo.
echo 📋 Copiando arquivos...
echo.

copy "dist\Whisper Video Captioning.exe" "%temp_dir%\" >nul
echo ✅ Executável copiado

if exist "dist\ffmpeg.exe" (
    copy "dist\ffmpeg.exe" "%temp_dir%\" >nul
    echo ✅ FFmpeg copiado
) else (
    echo ⚠️  FFmpeg.exe não encontrado em dist\
    echo    (coloque ffmpeg.exe na pasta manualmente antes de comprimir)
)

copy COMECE_AQUI.txt "%temp_dir%\" >nul
echo ✅ COMECE_AQUI.txt copiado

copy LEIA_ME.txt "%temp_dir%\" >nul
echo ✅ LEIA_ME.txt copiado

copy README_WINDOWS.md "%temp_dir%\" >nul
echo ✅ README_WINDOWS.md copiado

REM Copia templates se existir
if exist "src\templates" (
    xcopy "src\templates" "%temp_dir%\templates\" /E /I /Q >nul
    echo ✅ Templates copiados
)

REM Cria README de distribuição
(
echo # Whisper Video Captioning
echo.
echo ## Como Usar
echo.
echo 1. Descompacte esta pasta
echo 2. Clique duplo em "Whisper Video Captioning.exe"
echo 3. Seu navegador abrirá
echo 4. Selecione um vídeo
echo 5. Clique em Processar
echo 6. Pronto!
echo.
echo Para mais informações, leia COMECE_AQUI.txt
echo.
echo Versão: 1.0
echo Data: %date%
) > "%temp_dir%\LEIA_PRIMEIRO.txt"

echo ✅ LEIA_PRIMEIRO.txt criado

REM Cria arquivo de manifesto
(
echo [PACKAGE INFO]
echo Nome: Whisper Video Captioning
echo Versão: 1.0
echo Data: %date%
echo Hora: %time%
echo.
echo [ARQUIVOS]
echo - Whisper Video Captioning.exe (Aplicação Principal^)
echo - ffmpeg.exe (Processador de Áudio e Vídeo^)
echo - COMECE_AQUI.txt (Guia Rápido^)
echo - LEIA_ME.txt (Documentação Completa^)
echo - README_WINDOWS.md (Informações Técnicas^)
echo.
echo [REQUISITOS]
echo - Windows 10 ou superior
echo - Conexão de Internet (primeira execução apenas^)
echo - 500 MB de espaço em disco (mínimo^)
echo.
echo [COMO INSTALAR]
echo 1. Descompacte o arquivo ZIP
echo 2. Execute "Whisper Video Captioning.exe"
echo 3. Pronto! Sem instalação adicional!
) > "%temp_dir%\MANIFESTO.txt"

echo ✅ MANIFESTO.txt criado

REM Conta arquivos
echo.
echo 📊 Verificando conteúdo...
dir /s "%temp_dir%" | find /c /v ".">nul && (
    echo ✅ Package pronto!
)

REM Calcula tamanho
echo.
echo 💾 Calculando tamanho...
for /F "tokens=1" %%A in ('dir /s "%temp_dir%" ^| find /i "bytes"') do (
    for /F "tokens=2,3" %%B in (' ^"echo %%A^" ') do (
        set "size=%%B %%C"
    )
)

REM Pergunta se quer compactar
echo.
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║  ✅ Package criado com sucesso!                           ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo 📁 Pasta criada: %temp_dir%\
echo.
echo Arquivos incluídos:
echo   ✅ Whisper Video Captioning.exe
echo   ✅ ffmpeg.exe (se disponível^)
echo   ✅ Documentação completa em português
echo   ✅ Arquivos de templates
echo.
echo ⚠️  IMPORTANTE:
echo    Se FFmpeg não foi copiado, baixe de:
echo    https://ffmpeg.org/download.html
echo    E coloque ffmpeg.exe na pasta antes de comprimir!
echo.
echo Próximos passos:
echo   1. Verifique o conteúdo em: %temp_dir%\
echo   2. Se FFmpeg estiver faltando, copie manualmente
echo   3. Compacte a pasta em ZIP
echo   4. Distribua!
echo.
echo Para comprimir em ZIP, clique direito na pasta e escolha:
echo   "Enviar para" → "Pasta compactada"
echo.
pause
