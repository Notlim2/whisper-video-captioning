# 🎬 Whisper Video Captioning - Windows

Legendagem automática de vídeos em português usando IA.

## ⚡ Comece Agora!

```
1. Abra: COMECE_AQUI.txt  ← Leia este arquivo PRIMEIRO!
2. Execute: instalar_windows.bat
3. Execute: rodar_app.bat
4. Escolha a opção 1 (Web)
5. Clique em "Procurar" para selecionar seu vídeo
6. Clique em "Processar"
7. Pronto! Legendas criadas!
```

## 📋 Arquivos Importantes

| Arquivo | Função |
|---------|--------|
| **COMECE_AQUI.txt** | 👈 LEIA ESTE PRIMEIRO! Guia rápido em português |
| **LEIA_ME.txt** | Guia completo com tudo explicado |
| **instalar_windows.bat** | Execute para instalar dependências |
| **rodar_app.bat** | Execute para usar a aplicação |

## ✅ Requisitos

- **Python 3.8+** (https://python.org)
- **FFmpeg** (https://ffmpeg.org)
- **Conexão internet** (só na primeira execução)
- Windows 10 ou superior

O instalador verifica tudo automaticamente!

## 🎯 Como Funciona

1. **Seleção**: Escolha o vídeo que quer legendas
2. **Processamento**: IA analisa o áudio e transcreve
3. **Saída**: Gera arquivo .SRT com as legendas
4. **Resultado**: Abre em qualquer reprodutor de vídeo

## 🚀 Interfaces Disponíveis

### 1️⃣ Web (Recomendado)
- Abre no navegador
- Interface visual e amigável
- Melhor experiência do usuário

### 2️⃣ Interface Gráfica (GUI)
- Janela nativa do Windows
- Simples e direto
- Bom para quem prefere desktop

### 3️⃣ Linha de Comando (CLI)
- Para usuários avançados
- Modo texto
- Processamento em batch

## 📝 Formatos Suportados

**Vídeos:** MP4, AVI, MOV, MKV, WebM, FLV, WMV, M4V

**Legendas:** SRT (SubRip)

## ⏱️ Tempo de Processamento

| Duração | Tempo Estimado |
|---------|----------------|
| 5 min | 2-5 minutos |
| 10 min | 5-10 minutos |
| 30 min | 15-30 minutos |
| 1 hora | 30-60 minutos |

*Depende da velocidade do seu PC*

## 🎨 Configurações

Na interface web você pode ajustar:

- **Modelo**: tiny, base, small, medium (padrão: base)
- **Idioma**: pt, en, es, etc (padrão: pt-BR)
- **Qualidade**: parâmetros de IA
- **Duração máxima**: limitar processamento

## ❓ FAQ Rápido

**P: Precisa de internet?**
R: Só na primeira execução (baixa modelo de IA 140MB)

**P: Funciona offline?**
R: Sim! Após primeira execução

**P: Pode editar legendas depois?**
R: Sim! SRT é texto puro, edita com qualquer editor

**P: Demora quanto tempo?**
R: Varia conforme tamanho do vídeo e velocidade do PC

**P: Qual a qualidade?**
R: Excelente! Whisper é muito preciso

## 🐛 Problemas?

Leia a seção "PROBLEMAS COMUNS" em LEIA_ME.txt

Problemas típicos:
- Python não encontrado → Instale Python 3.8+
- FFmpeg não encontrado → Instale FFmpeg
- Porta 5000 em uso → Feche outro programa

## 📞 Suporte

1. Leia LEIA_ME.txt (respostas para tudo)
2. Reinstale: execute instalar_windows.bat novamente
3. Reinicie o Windows

## 🎬 Exemplo Prático

Você tem: `C:\Videos\meu_video.mp4`

1. Execute `rodar_app.bat`
2. Escolha opção 1 (Web)
3. "Procurar Vídeo" → `C:\Videos\meu_video.mp4`
4. "Procurar Pasta" → `C:\Videos`
5. Clique "Processar"
6. Aguarde...
7. Resultado: `C:\Videos\meu_video.srt`

Abra o SRT no VLC junto com o vídeo!

## 🎉 Pronto!

Leia **COMECE_AQUI.txt** agora!

---

Made with ❤️ for Portuguese video creators
