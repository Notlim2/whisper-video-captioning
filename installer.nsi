; NSIS Installer Script para Whisper Video Captioning
; Cria um instalador profissional que inclui tudo

!include "MUI2.nsh"
!include "x64.nsh"

; Definições
Name "Whisper Video Captioning"
OutFile "Whisper_Video_Captioning_Setup.exe"
InstallDir "$PROGRAMFILES\Whisper Video Captioning"

; MUI Settings
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "Portuguese"
!insertmacro MUI_LANGUAGE "English"

; Seção de instalação
Section "Instalar"
    SetOutPath "$INSTDIR"
    
    ; Copia arquivos da aplicação
    File /r "dist\Whisper Video Captioning\*.*"
    
    ; Copia FFmpeg
    SetOutPath "$INSTDIR\ffmpeg"
    File /r "ffmpeg\*.*"
    
    ; Cria atalhos
    CreateDirectory "$SMPROGRAMS\Whisper Video Captioning"
    CreateShortCut "$SMPROGRAMS\Whisper Video Captioning\Whisper Video Captioning.lnk" "$INSTDIR\Whisper Video Captioning.exe"
    CreateShortCut "$SMPROGRAMS\Whisper Video Captioning\Desinstalar.lnk" "$INSTDIR\uninstall.exe"
    CreateShortCut "$DESKTOP\Whisper Video Captioning.lnk" "$INSTDIR\Whisper Video Captioning.exe"
    
    ; Cria entrada no Painel de Controle
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\WhisperVideoCaptioning" "DisplayName" "Whisper Video Captioning"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\WhisperVideoCaptioning" "UninstallString" "$INSTDIR\uninstall.exe"
    
    ; Cria desinstalador
    WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

; Seção de desinstalação
Section "Uninstall"
    RMDir /r "$INSTDIR"
    RMDir /r "$SMPROGRAMS\Whisper Video Captioning"
    Delete "$DESKTOP\Whisper Video Captioning.lnk"
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\WhisperVideoCaptioning"
SectionEnd
