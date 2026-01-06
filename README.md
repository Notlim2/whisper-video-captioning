╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║  🎬 WHISPER VIDEO CAPTIONING                                              ║
║  Gerador Automático de Legendas em Português                              ║
║                                                                             ║
╚═══════════════════════════════════════════════════════════════════════════╝


═══════════════════════════════════════════════════════════════════════════════
🚀 INÍCIO RÁPIDO
═══════════════════════════════════════════════════════════════════════════════

WINDOWS:
  1. Duplo clique em: iniciar_windows.bat
  2. Navegador abre em: http://localhost:5000
  3. Selecione vídeo e clique "Processar"

LINUX/MAC:
  1. Terminal: python src/web_app.py
  2. Abra: http://localhost:5000
  3. Selecione vídeo e clique "Processar"


═══════════════════════════════════════════════════════════════════════════════
📁 ESTRUTURA DO PROJETO
═══════════════════════════════════════════════════════════════════════════════

whisper-video-captioning/
├── 🚀 EXECUTAR
│   ├── iniciar_windows.bat      (Windows - clique duplo)
│   ├── compilar_completo.bat    (Gera .exe para Windows)
│   ├── compilar.py              (Compila em Python)
│   └── criar_package.bat        (Gera pacote para distribuir)
│
├── 🔧 CÓDIGO
│   ├── src/
│   │   ├── web_app.py           (Servidor web principal)
│   │   ├── main.py              (CLI interface)
│   │   ├── gui.py               (GUI Tkinter)
│   │   ├── transcriber.py       (Integração Whisper)
│   │   ├── video_processor.py   (Processamento de vídeo)
│   │   ├── subtitle_generator.py (Geração de legendas)
│   │   ├── utils.py             (Funções auxiliares)
│   │   └── templates/
│   │       └── index.html       (Interface web)
│   │
│   ├── config/
│   │   ├── settings.py          (Configurações padrão)
│   │   └── settings_windows.py  (Configurações Windows)
│   │
│   ├── input/                   (Pasta para vídeos de entrada)
│   ├── output/                  (Pasta para legendas geradas)
│   └── models/                  (Cache dos modelos Whisper)
│
├── 📋 CONFIGURAÇÃO
│   ├── requirements.txt          (Dependências Python)
│   ├── installer.nsi            (Gerador de instalador Windows)
│   ├── launcher_windows.py      (Launcher avançado - opcional)
│   └── streamer.wav             (Arquivo de teste)
│
└── 📚 DOCUMENTAÇÃO
    └── README.md                (Este arquivo)


═══════════════════════════════════════════════════════════════════════════════
⚙️ REQUISITOS
═══════════════════════════════════════════════════════════════════════════════

OBRIGATÓRIO:
  • Python 3.7+
  • FFmpeg (incluído em compilação .exe ou instale manualmente)
  • Conexão com internet (primeira execução baixa modelo Whisper)

RECOMENDADO:
  • GPU (NVIDIA com CUDA) para processamento mais rápido
  • 8GB+ RAM
  • 1GB+ disco (para cache do modelo Whisper)


═══════════════════════════════════════════════════════════════════════════════
🔧 INSTALAÇÃO
═══════════════════════════════════════════════════════════════════════════════

OPÇÃO 1: Executável Windows (Recomendado)
────────────────────────────────────────
1. Gere .exe:
   compilar_completo.bat

2. Distribua:
   • Whisper Video Captioning.exe
   • ffmpeg.exe
   • LEIA_ME.txt

3. Usuário:
   Duplo clique no .exe


OPÇÃO 2: Python Direto (Desenvolvimento)
──────────────────────────────────────
1. Clone o repositório
2. python -m venv venv
3. Ative venv:
   - Windows: venv\Scripts\activate
   - Linux: source venv/bin/activate
4. pip install -r requirements.txt
5. python src/web_app.py


OPÇÃO 3: Docker (Futuro)
────────────────────
Planejado para releases futuras.


═══════════════════════════════════════════════════════════════════════════════
📖 COMO USAR
═══════════════════════════════════════════════════════════════════════════════

INTERFACE WEB (Recomendado):
────────────────────────────
1. Inicie: iniciar_windows.bat (Windows) ou python src/web_app.py (Linux)
2. Navegador abre em: http://localhost:5000
3. Clique "Procurar Vídeo"
4. Selecione arquivo .mp4/.avi/.mov/.mkv
5. Clique "Processar"
6. Aguarde: 30s a 5 minutos (depende do tamanho)
7. Legendas salvas em: output/[nome_video].srt

INTERFACE CLI:
────────────────
python src/main.py --video "caminho/video.mp4" --output "output/"

INTERFACE GUI:
────────────────
python src/gui.py


═══════════════════════════════════════════════════════════════════════════════
⚙️ CONFIGURAÇÃO
═══════════════════════════════════════════════════════════════════════════════

Edite: config/settings.py

Opções principais:
  LANGUAGE = "pt"              # Idioma (pt, en, es, etc)
  MODEL_NAME = "base"          # Tamanho do modelo (tiny, base, small, medium, large)
  TASK = "transcribe"          # translate ou transcribe
  BEAM_SIZE = 5                # Qualidade (maior = melhor, mais lento)
  BEST_OF = 5                  # Número de tentativas
  TEMPERATURE = 0.0            # Criatividade (0 = determinístico)

Para Windows específico: config/settings_windows.py


═══════════════════════════════════════════════════════════════════════════════
🐛 TROUBLESHOOTING
═══════════════════════════════════════════════════════════════════════════════

PROBLEMA: "Python não encontrado"
SOLUÇÃO:
  • Instale Python: https://www.python.org/
  • IMPORTANTE: Marque "Add to PATH"
  • Reinicie terminal

PROBLEMA: "FFmpeg não encontrado"
SOLUÇÃO:
  • Windows: Coloque ffmpeg.exe na mesma pasta do .exe
  • Linux: apt install ffmpeg
  • Mac: brew install ffmpeg

PROBLEMA: "Erro ao processar vídeo"
SOLUÇÃO:
  • Verifique formato: .mp4, .avi, .mov, .mkv, .webm, .flv
  • Tente vídeo menor
  • Aumente timeout em settings.py

PROBLEMA: "Caminho de arquivo inválido no Windows"
SOLUÇÃO:
  • Caminho é automaticamente convertido para Windows
  • Se erro persistir, verifique se arquivo existe
  • Use caminhos sem caracteres especiais

PROBLEMA: "Processo muito lento"
SOLUÇÃO:
  • Use modelo "tiny" em settings.py
  • Reduza BEAM_SIZE para 3
  • Se tiver GPU, instale: pip install torch torchvision torchaudio


═══════════════════════════════════════════════════════════════════════════════
📦 COMPILAÇÃO PARA .EXE
═══════════════════════════════════════════════════════════════════════════════

1. Instale PyInstaller:
   pip install pyinstaller

2. Execute:
   compilar_completo.bat

3. Resultado:
   dist/Whisper Video Captioning.exe

4. Distribua:
   • Crie pasta com:
     ├─ Whisper Video Captioning.exe
     ├─ ffmpeg.exe
     └─ LEIA_ME.txt (este arquivo)
   • Compacte em ZIP
   • Envie!


═══════════════════════════════════════════════════════════════════════════════
🔄 ATUALIZAR
═══════════════════════════════════════════════════════════════════════════════

Código:
  git pull origin main

Dependências:
  pip install -r requirements.txt --upgrade

Modelos Whisper:
  rm -rf ~/.cache/whisper
  (Baixará versão mais recente na próxima execução)


═══════════════════════════════════════════════════════════════════════════════
💡 DICAS
═══════════════════════════════════════════════════════════════════════════════

• Use modelo "small" para melhor balanço qualidade/velocidade
• Primeira execução é lenta (baixa 140MB+ do modelo)
• GPU acelera 10x - vale a pena em uso frequente
• Aumentar BEAM_SIZE melhora qualidade, mas é mais lento
• Para português do Brasil: LANGUAGE = "pt-BR" (se suportado)


═══════════════════════════════════════════════════════════════════════════════
📝 SUPORTE
═══════════════════════════════════════════════════════════════════════════════

GitHub: https://github.com/Notlim2/whisper-video-captioning
Issues: Relate problemas no GitHub
Email: contato@exemplo.com (futuramente)


═══════════════════════════════════════════════════════════════════════════════
📄 LICENÇA
═══════════════════════════════════════════════════════════════════════════════

MIT License - Use livremente, mesmo em projetos comerciais


═══════════════════════════════════════════════════════════════════════════════
