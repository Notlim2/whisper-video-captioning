from video_processor import VideoProcessor
from transcriber import Transcriber
from subtitle_generator import SubtitleGenerator
from utils import load_env, validate_file
import os
from pathlib import Path
import sys

# Adiciona config ao path
sys.path.insert(0, '../config')

def main():
    load_env()
    
    # Carrega configurações
    try:
        from config.settings import LANGUAGE, MODEL_NAME
    except:
        LANGUAGE = "pt"
        MODEL_NAME = "base"
    
    video_file = input("Enter the path to the video file: ").strip()
    
    if not validate_file(video_file):
        print("Invalid file. Please provide a valid video file.")
        return
    
    # Initialize the video processing pipeline
    video_processor = VideoProcessor(video_file)
    transcriber = Transcriber(language=LANGUAGE, model_size=MODEL_NAME)
    subtitle_generator = SubtitleGenerator()
    
    # Extract audio from the video
    audio_file = video_processor.extract_audio()
    
    try:
        # Transcribe the audio
        transcribed_text = transcriber.transcribe_audio(audio_file)
        
        # Generate subtitles
        subtitles = subtitle_generator.generate_subtitles(transcribed_text)
        
        # Save subtitles to a file
        output_file = os.path.splitext(video_file)[0] + ".srt"
        subtitle_generator.save_subtitles(subtitles, output_file)
        
        print(f"✓ Subtitles saved to {output_file}")
    
    finally:
        # Remove audio file after conversion
        if os.path.exists(audio_file):
            Path(audio_file).unlink()
            print(f"✓ Audio file removed: {audio_file}")

if __name__ == "__main__":
    main()