class VideoProcessor:
    def __init__(self, video_file):
        self.video_file = video_file

    def extract_audio(self):
        # Logic to extract audio from the video file
        import subprocess
        from pathlib import Path
        
        audio_file = Path(self.video_file).stem + ".wav"
        
        try:
            # Remove arquivo anterior se existir
            Path(audio_file).unlink(missing_ok=True)
            
            print(f"Extraindo áudio com ffmpeg...")
            # Extrai áudio com normalização para melhor reconhecimento
            # -af "volume=1.5" amplifica o áudio se estiver baixo
            result = subprocess.run([
                "ffmpeg", "-i", self.video_file, 
                "-vn", "-acodec", "pcm_s16le", "-ar", "16000",
                "-ac", "1", "-af", "loudnorm=I=-20:TP=-1.5:LRA=11", 
                "-y", audio_file
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                # Fallback sem normalização se loudnorm falhar
                print("Tentando sem normalização avançada...")
                subprocess.run([
                    "ffmpeg", "-i", self.video_file, 
                    "-vn", "-acodec", "pcm_s16le", "-ar", "16000",
                    "-ac", "1", "-af", "volume=1.2",
                    "-y", audio_file
                ], check=True, capture_output=True, text=True)
            
            print(f"✓ Áudio extraído: {audio_file}")
            return audio_file
            
        except subprocess.CalledProcessError as e:
            print(f"✗ Erro ao extrair áudio: {e}")
            raise
        except FileNotFoundError:
            print("✗ FFmpeg não encontrado. Instale com: sudo apt install ffmpeg")
            raise

    def process_video(self):
        # Logic to handle the overall video processing workflow
        pass