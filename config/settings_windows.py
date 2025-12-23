# Configuração para Windows - Whisper Video Captioning

# Diretórios padrão (Windows usa \\ para caminhos)
DEFAULT_INPUT_DIR = r"C:\Users\{username}\Videos"
DEFAULT_OUTPUT_DIR = r"C:\Users\{username}\Downloads"

# Modelo de IA
# tiny, base (recomendado), small, medium, large
MODEL_NAME = "base"

# Idioma
LANGUAGE = "pt"

# Tarefa
TASK = "transcribe"  # ou "translate"

# Parâmetros de transcrição
BEAM_SIZE = 5
BEST_OF = 5
TEMPERATURE = 0.0
NO_SPEECH_THRESHOLD = 0.6

# Duração máxima de áudio em segundos
# 300 = 5 minutos, 600 = 10 minutos
MAX_AUDIO_LENGTH = 600

# Configurações de áudio
AUDIO_SAMPLE_RATE = 16000
AUDIO_CHANNELS = 1

# Formatos de vídeo suportados
SUPPORTED_FORMATS = ['.mp4', '.avi', '.mov', '.mkv', '.webm', '.flv', '.wmv', '.m4v']

# Porta para servidor web
WEB_PORT = 5000
WEB_HOST = '127.0.0.1'

# Modo debug
DEBUG = False
