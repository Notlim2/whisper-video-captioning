import sys
sys.path.insert(0, '../config')

class Transcriber:
    def __init__(self, language="pt", model_size="base"):
        self.language = language
        self.model_size = model_size
        self.model = self.load_model()

    def load_model(self):
        """Carrega o modelo Whisper otimizado para o idioma"""
        import whisper
        print(f"Carregando modelo Whisper '{self.model_size}' para {self.language}...")
        model = whisper.load_model(self.model_size)
        return model

    def transcribe_audio(self, audio_file):
        """
        Transcreve áudio com otimizações para português brasileiro.
        Retorna o dicionário completo com segmentos e tempos.
        """
        try:
            from config.settings import (
                TASK, BEST_OF, BEAM_SIZE, TEMPERATURE, NO_SPEECH_THRESHOLD
            )
        except:
            # Valores padrão se settings não estiver disponível
            TASK = "transcribe"
            BEST_OF = 5
            BEAM_SIZE = 5
            TEMPERATURE = 0.0
            NO_SPEECH_THRESHOLD = 0.6
        
        print(f"Transcrevendo áudio ({self.language})...")
        print(f"  - Modelo: {self.model_size}")
        print(f"  - Beam Size: {BEAM_SIZE}")
        print(f"  - Best Of: {BEST_OF}")
        
        result = self.model.transcribe(
            audio_file,
            language=self.language,
            task=TASK,
            best_of=BEST_OF,
            beam_size=BEAM_SIZE,
            temperature=TEMPERATURE,
            no_speech_threshold=NO_SPEECH_THRESHOLD,
            verbose=False
        )
        
        # Exibe informações da transcrição
        if 'segments' in result:
            print(f"✓ {len(result['segments'])} segmentos transcritos")
        
        return result