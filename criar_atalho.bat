@echo off
REM Cria um atalho para rodar_app.bat na Área de Trabalho

setlocal enabledelayedexpansion

set "desktop=%USERPROFILE%\Desktop"
set "app_dir=%~dp0"
set "batch_file=%app_dir%rodar_app.bat"

REM Remove % da string (caso haja variáveis)
set "app_name=Whisper Video Captioning"

echo.
echo Criando atalho na Área de Trabalho...
echo.

REM Cria VBScript para criar o atalho (funciona melhor no Windows)
set "vbs_file=%temp%\create_shortcut.vbs"

(
echo Set oWS = WScript.CreateObject("WScript.Shell"^)
echo Set oLink = oWS.CreateShortcut("%desktop%\%app_name%.lnk"^)
echo oLink.TargetPath = "%batch_file%"
echo oLink.WorkingDirectory = "%app_dir%"
echo oLink.IconLocation = "cmd.exe,0"
echo oLink.Description = "Whisper Video Captioning - Legendagem de Vídeos"
echo oLink.Save
) > "%vbs_file%"

REM Executa o VBScript
cscript.exe //nologo "%vbs_file%"

REM Limpa o arquivo temporário
del "%vbs_file%"

echo.
echo ✅ Atalho criado com sucesso!
echo.
echo O arquivo 'Whisper Video Captioning' foi adicionado à sua Área de Trabalho.
echo.
echo Você pode agora:
echo   1. Clicar duplo no atalho para iniciar
echo   2. Fixar o atalho na Barra de Tarefas
echo.
pause
