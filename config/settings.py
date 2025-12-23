# Configuration settings for the Whisper video captioning project

# Model parameters
MODEL_NAME = "medium"  # Specify the Whisper model to use (tiny, base, small, medium, large)
LANGUAGE = "pt"  # Default language for transcription (pt for Portuguese/pt-BR)

# File paths
INPUT_VIDEO_PATH = "input/"  # Directory for input video files
OUTPUT_SUBTITLE_PATH = "output/"  # Directory for output subtitle files

# Whisper optimization for Portuguese
TASK = "transcribe"  # Can be "transcribe" or "translate"
BEST_OF = 5  # Number of candidates to consider (higher = better quality, slower)
BEAM_SIZE = 5  # Beam search size (higher = better quality, slower)
TEMPERATURE = 0.0  # Temperature for sampling (0 = deterministic, higher = more random)
NO_SPEECH_THRESHOLD = 0.6  # Skip segments with low speech probability

# Audio processing
TARGET_SAMPLE_RATE = 16000  # Whisper works best at 16kHz
AUDIO_NORMALIZATION = True  # Normalize audio levels for better recognition

# Other constants
MAX_AUDIO_LENGTH = 30  # Maximum audio length in seconds for processing
SUBTITLE_FORMAT = "srt"  # Default subtitle format to save as

# Logging settings
LOG_LEVEL = "INFO"  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)