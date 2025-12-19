class SubtitleGenerator:
    def __init__(self):
        pass

    def generate_subtitles(self, transcribed_data):
        """
        Gera legendas a partir do objeto de transcrição do Whisper.
        Whisper retorna um dict com 'segments' contendo tempos reais.
        """
        subtitles = []
        
        # Se transcribed_data é um dicionário com 'segments' (resposta do Whisper)
        if isinstance(transcribed_data, dict) and 'segments' in transcribed_data:
            segments = transcribed_data['segments']
        # Se é uma lista direta de segmentos
        elif isinstance(transcribed_data, list):
            segments = transcribed_data
        else:
            # Fallback para string simples
            return [{"index": 1, "start": 0, "end": 1, "text": transcribed_data}]
        
        for i, segment in enumerate(segments, 1):
            start_time = segment.get('start', 0)
            end_time = segment.get('end', start_time + 2)  # Mínimo de 2 segundos
            text = segment.get('text', '').strip()
            
            if text:  # Só adiciona se houver texto
                subtitles.append({
                    'index': i,
                    'start': start_time,
                    'end': end_time,
                    'text': text
                })
        
        return subtitles

    def format_time(self, seconds):
        """Converte segundos para formato SRT: HH:MM:SS,mmm"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        milliseconds = int((seconds - int(seconds)) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"

    def save_subtitles(self, subtitles, output_file):
        """Salva legendas em formato SRT"""
        with open(output_file, 'w', encoding='utf-8') as f:
            for subtitle in subtitles:
                start = self.format_time(subtitle['start'])
                end = self.format_time(subtitle['end'])
                text = subtitle['text']
                
                f.write(f"{subtitle['index']}\n")
                f.write(f"{start} --> {end}\n")
                f.write(f"{text}\n\n")