═══════════════════════════════════════════════════════════════════════════
✅ SETUP RÁPIDO - WHISPER VIDEO CAPTIONING
═══════════════════════════════════════════════════════════════════════════

🖥️ WINDOWS
═════════════════════════════════════════════════════════════════════════════

OPÇÃO 1: Executável (Mais Fácil)
─────────────────────────────────
1. Clique duplo em: compilar_completo.bat
   (Gera Whisper Video Captioning.exe em dist/)

2. Pronto! Execute o .exe

3. Navegador abre automaticamente
   → http://localhost:5000

4. Use a interface web para processar vídeos


OPÇÃO 2: Direto do Python
────────────────────────
1. Clique duplo em: iniciar_windows.bat

2. Navegador abre automaticamente
   → http://localhost:5000

3. Use a interface web


OPÇÃO 3: Command Prompt
──────────────────────
1. Abra Command Prompt (Win+R, cmd)

2. Navegue até a pasta do projeto:
   cd "C:\caminho\para\whisper-video-captioning"

3. Execute:
   python src\web_app.py

4. Abra navegador:
   http://localhost:5000


🐧 LINUX / 🍎 MAC
═════════════════════════════════════════════════════════════════════════════

OPÇÃO 1: Script Automático
──────────────────────────
1. Abra terminal

2. Navegue até a pasta:
   cd ~/caminho/para/whisper-video-captioning

3. Torne script executável:
   chmod +x iniciar_linux.sh

4. Execute:
   ./iniciar_linux.sh

5. Navegador abre automaticamente
   → http://localhost:5000


OPÇÃO 2: Manual
───────────────
1. Abra terminal

2. Navegue até a pasta:
   cd ~/caminho/para/whisper-video-captioning

3. Crie e ative virtual environment:
   python3 -m venv venv
   source venv/bin/activate

4. Instale dependências:
   pip install -r requirements.txt

5. Execute:
   python3 src/web_app.py

6. Abra navegador:
   http://localhost:5000


═════════════════════════════════════════════════════════════════════════════
📝 PRIMEIRA EXECUÇÃO
═════════════════════════════════════════════════════════════════════════════

A primeira execução pode levar 2-5 minutos porque:
• Baixa modelo Whisper (140+ MB)
• Instala bibliotecas necessárias
• Compila código

Execuções seguintes são muito mais rápidas!


═════════════════════════════════════════════════════════════════════════════
🎯 PRÓXIMOS PASSOS
═════════════════════════════════════════════════════════════════════════════

1. Aplicação iniciada?
   ✅ Navegador abre em http://localhost:5000

2. Interface carregou?
   ✅ Clique em "Procurar Vídeo"

3. Selecione um vídeo:
   ✅ Formatos suportados: MP4, AVI, MOV, MKV, WEBM, FLV

4. Clique "Processar":
   ✅ Aguarde: 30s a 5 minutos

5. Resultado:
   ✅ Arquivo .SRT criado em output/

6. Use legenda:
   ✅ Abra vídeo em seu player favorito
   ✅ Abra arquivo .SRT como legenda


═════════════════════════════════════════════════════════════════════════════
⚙️ CONFIGURAÇÃO AVANÇADA
═════════════════════════════════════════════════════════════════════════════

Edite: config/settings.py

Principais opções:
  LANGUAGE = "pt"          # Idioma
  MODEL_NAME = "base"      # Tamanho (tiny, base, small, medium, large)
  BEAM_SIZE = 5            # Qualidade
  TEMPERATURE = 0.0        # Precisão

Depois reinicie a aplicação.


═════════════════════════════════════════════════════════════════════════════
❓ PROBLEMAS?
═════════════════════════════════════════════════════════════════════════════

Python não encontrado?
  • Windows: Instale em https://www.python.org/
  • Linux: sudo apt install python3
  • Mac: brew install python3

FFmpeg não encontrado?
  • Windows: Copie ffmpeg.exe na mesma pasta
  • Linux: sudo apt install ffmpeg
  • Mac: brew install ffmpeg

Veja README.md para troubleshooting completo


═════════════════════════════════════════════════════════════════════════════
