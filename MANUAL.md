# 🎬 Whisper Video Captioning - Guia de Uso

## 📋 Descrição

Sistema automático de legendagem de vídeos em português brasileiro usando OpenAI Whisper. Suporta múltiplas interfaces para processamento de vídeos.

---

## 🚀 Instalação Inicial

### 1. Clone ou abra o projeto

```bash
cd /home/milton/Projetos/poc-legenda-automatica
```

### 2. Crie e ative o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. (Opcional) Instale Tkinter para a GUI desktop

```bash
sudo apt install python3-tk -y
```

---

## 🎯 Como Executar as Interfaces

### Opção 1: Interface Web (Recomendado para a maioria)

**Melhor para:** Navegadores, acesso remoto, facilidade de uso

#### Executar:
```bash
cd /home/milton/Projetos/poc-legenda-automatica
source venv/bin/activate
python3 src/web_app.py
```

#### Acessar:
- Abra seu navegador em **http://localhost:5000**

#### Recursos:
✅ Interface bonita e intuitiva
✅ Ajuste de todas as configurações em tempo real
✅ Visualização de progresso em tempo real
✅ Suporta múltiplos processamentos simultâneos
✅ Funciona em qualquer navegador

---

### Opção 2: Interface Gráfica Desktop (Tkinter)

**Melhor para:** Uso local, sem navegador, aplicativo standalone

#### Executar:
```bash
cd /home/milton/Projetos/poc-legenda-automatica
source venv/bin/activate
python3 src/gui.py
```

#### Ou use o script:
```bash
./run_gui.sh
```

#### Recursos:
✅ Aplicativo desktop nativo
✅ Todos os controles da configuração
✅ Log detalhado de processamento
✅ Seleção visual de arquivos (diálogos nativas)

---

### Opção 3: Interface de Linha de Comando (CLI)

**Melhor para:** Automação, scripts, servidores headless

#### Executar:
```bash
cd /home/milton/Projetos/poc-legenda-automatica
source venv/bin/activate
python3 src/main.py
```

#### Como usar:
1. O script pedirá o caminho do vídeo
2. Exemplo: `/home/milton/Downloads/meu_video.mp4`
3. As legendas serão salvas no mesmo diretório do vídeo
4. O arquivo temporário de áudio será removido automaticamente

#### Recursos:
✅ Mais rápido
✅ Usa configurações padrão do `settings.py`
✅ Ideal para integração com scripts

---

## ⚙️ Configurações Disponíveis

Todas as interfaces usam as configurações definidas em `config/settings.py`:

```python
# Modelo Whisper (escolha um)
MODEL_NAME = "base"      # Padrão: 140MB
# Opções: "tiny" (39MB), "small" (244MB), "medium" (1.5GB), "large" (2.9GB)

# Idioma
LANGUAGE = "pt"          # Português/pt-BR
# Opções: "en", "es", "fr", etc

# Qualidade da transcrição
BEAM_SIZE = 5            # 1-10 (maior = mais preciso, mas lento)
BEST_OF = 5              # 1-10 (maior = melhor qualidade)
TEMPERATURE = 0.0        # 0-1 (0 = determinístico)

# Limites
MAX_AUDIO_LENGTH = 30   # Máximo de segundos para processar
```

### Modificar Configurações Padrão

Edit `config/settings.py`:

```bash
nano config/settings.py
```

---

## 📊 Comparação das Interfaces

| Recurso | CLI | Tkinter GUI | Web |
|---------|-----|-------------|-----|
| **Facilidade** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Configurações visuais** | ❌ | ✅ | ✅ |
| **Seleção de arquivos** | Manual | Visual | Manual |
| **Progresso visual** | Básico | Bom | Excelente |
| **Navegador necessário** | ❌ | ❌ | ✅ |
| **Automação** | ✅✅✅ | ❌ | ⚠️ |
| **Remoto** | ✅ | ❌ | ✅ |
| **Performance** | Rápido | Normal | Normal |

---

## 🎯 Exemplos de Uso

### Exemplo 1: Legendar um vídeo (CLI - mais rápido)

```bash
source venv/bin/activate
python3 src/main.py
# Digite: /home/milton/Downloads/video.mp4
```

### Exemplo 2: Legendar com interface amigável (Web)

```bash
python3 src/web_app.py
# Abra http://localhost:5000
# Clique em "Procurar..." para selecionar o vídeo
# Ajuste as configurações
# Clique em "Processar"
```

### Exemplo 3: Legendar com interface desktop (Tkinter)

```bash
python3 src/gui.py
# Clique em "Procurar..." para o vídeo
# Ajuste as configurações nos sliders
# Clique em "▶ Processar"
```

---

## 📁 Estrutura do Projeto

```
poc-legenda-automatica/
├── config/
│   └── settings.py           # Configurações padrão
├── src/
│   ├── main.py              # Interface CLI
│   ├── gui.py               # Interface Tkinter Desktop
│   ├── web_app.py           # Interface Web Flask
│   ├── video_processor.py   # Processamento de vídeo
│   ├── transcriber.py       # Transcrição com Whisper
│   ├── subtitle_generator.py # Geração de legendas
│   ├── utils.py             # Funções utilitárias
│   └── templates/
│       └── index.html       # Frontend web
├── input/                    # Pasta para vídeos (opcional)
├── output/                   # Pasta para legendas (opcional)
├── requirements.txt          # Dependências Python
├── run_gui.sh               # Script para iniciar GUI
└── README.md                # Este arquivo
```

---

## 🔧 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'whisper'"
```bash
source venv/bin/activate
pip install openai-whisper
```

### Erro: "FFmpeg not found"
```bash
sudo apt install ffmpeg -y
```

### Erro: "Tkinter not found"
```bash
sudo apt install python3-tk -y
```

### Aplicação web não abre
- Certifique-se que a porta 5000 está livre: `lsof -i :5000`
- Mate o processo: `pkill -f "python3 src/web_app.py"`
- Inicie novamente

### GUI Tkinter travada
- Feche a janela
- Execute novamente: `python3 src/gui.py`

---

## 📈 Dicas de Otimização

### Para vídeos longos (>10 minutos):
```python
MODEL_NAME = "tiny"        # Mais rápido
BEAM_SIZE = 3
BEST_OF = 3
```

### Para máxima qualidade:
```python
MODEL_NAME = "large"       # Mais preciso
BEAM_SIZE = 10
BEST_OF = 10
TEMPERATURE = 0.0
```

### Para vídeos muito longos (>30 min):
```python
MAX_AUDIO_LENGTH = 1800    # 30 minutos
```

---

## 🚀 Execução em Background

Para manter a aplicação rodando mesmo fechando o terminal:

```bash
# Usando nohup
nohup python3 src/web_app.py > whisper.log 2>&1 &

# Ou usando screen
screen -S whisper python3 src/web_app.py
# Para desatachar: Ctrl+A, depois D
# Para voltar: screen -r whisper
```

---

## 📝 Formato de Saída

As legendas são geradas em formato **SRT** padrão:

```srt
1
00:00:00,000 --> 00:00:06,200
Alô, testando 1, 2, 3, 4, 5.

2
00:00:06,200 --> 00:00:12,500
Próxima frase do vídeo...
```

O arquivo é salvo com o mesmo nome do vídeo:
- Input: `video.mp4`
- Output: `video.srt`

---

## 💡 Próximas Melhorias

- [ ] Suporte para múltiplos idiomas simultâneos
- [ ] Exportação em VTT, ASS, SSA
- [ ] Incorporação de legendas direto no vídeo
- [ ] API REST para integração
- [ ] Banco de dados para histórico

---

## 📞 Suporte

Para problemas ou dúvidas:

1. Verifique se todas as dependências estão instaladas: `pip list | grep -E "whisper|torch|flask"`
2. Teste com um vídeo de teste pequeno primeiro
3. Consulte os logs de erro na interface

---

**Desenvolvido com ❤️ para legendagem automática em português** 🇧🇷

