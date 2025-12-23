# 🎯 Guia Rápido - Como Rodar as Interfaces

## 🚀 Forma Mais Fácil: Menu Interativo

```bash
cd /home/milton/Projetos/poc-legenda-automatica
./menu.sh
```

Escolha uma opção no menu e aproveite!

---

## 🌐 Interface Web (Melhor para a Maioria)

**Característica:** Acesso via navegador, mais intuitiva e bonita

```bash
cd /home/milton/Projetos/poc-legenda-automatica
source venv/bin/activate
python3 src/web_app.py
```

📱 **Abra:** http://localhost:5000

✨ **Vantagens:**
- Interface moderna e intuitiva
- Ajuste visual de todas as configurações
- Progresso em tempo real
- Funciona em qualquer navegador

---

## 🖥️ Interface Desktop (GUI Tkinter)

**Característica:** Aplicativo desktop nativo, sem navegador

```bash
cd /home/milton/Projetos/poc-legenda-automatica
source venv/bin/activate
python3 src/gui.py
```

Ou simplesmente:
```bash
./run_gui.sh
```

✨ **Vantagens:**
- Aplicativo standalone
- Seleção visual de arquivos
- Log detalhado
- Funciona sem navegador

---

## 💻 Interface CLI (Linha de Comando)

**Característica:** Rápido, automatizado, para scripts

```bash
cd /home/milton/Projetos/poc-legenda-automatica
source venv/bin/activate
python3 src/main.py
```

Será pedido:
1. Caminho do vídeo
2. Exemplo: `/home/milton/Downloads/video.mp4`

✨ **Vantagens:**
- Mais rápido
- Usa configurações padrão
- Ideal para automação
- Sem interface gráfica

---

## 📋 Resumo Rápido

| Interface | Comando | Melhor Para |
|-----------|---------|-------------|
| **Menu** | `./menu.sh` | Novos usuários |
| **Web** | `python3 src/web_app.py` | Uso geral |
| **Desktop** | `python3 src/gui.py` ou `./run_gui.sh` | Uso local |
| **CLI** | `python3 src/main.py` | Automação |

---

## ⚙️ Configurações (settings.py)

Para mudar configurações padrão:

```bash
nano config/settings.py
```

**Principais parâmetros:**

```python
MODEL_NAME = "base"          # tiny, base, small, medium, large
LANGUAGE = "pt"              # Idioma (pt, en, es, fr)
BEAM_SIZE = 5                # Precisão (1-10)
BEST_OF = 5                  # Qualidade (1-10)
TEMPERATURE = 0.0            # Aleatoriedade (0-1)
MAX_AUDIO_LENGTH = 30       # Máximo de segundos
```

---

## 🆘 Problemas Comuns?

**Erro: "venv not found"**
```bash
python3 -m venv venv
```

**Erro: "whisper not found"**
```bash
source venv/bin/activate
pip install openai-whisper
```

**Erro: "ffmpeg not found"**
```bash
sudo apt install ffmpeg
```

**Erro: "tkinter not found"**
```bash
sudo apt install python3-tk
```

---

## 📂 Arquivos Importantes

- `src/main.py` → CLI
- `src/gui.py` → Desktop GUI
- `src/web_app.py` → Web Interface
- `config/settings.py` → Configurações
- `MANUAL.md` → Documentação completa
- `menu.sh` → Menu interativo

---

🎬 **Pronto para legendar vídeos!** 🚀

