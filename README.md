# Whisper Video Captioning

This project utilizes the OpenAI Whisper model to automatically generate subtitles for video files. The application processes video files, extracts audio, transcribes the audio to text, and formats the text into subtitle files.

## Project Structure

```
whisper-video-captioning
├── src
│   ├── main.py               # Entry point of the application
│   ├── transcriber.py        # Handles audio transcription
│   ├── video_processor.py     # Manages video processing
│   ├── subtitle_generator.py   # Generates and saves subtitles
│   └── utils.py              # Utility functions
├── config
│   └── settings.py           # Configuration settings
├── models
│   └── .gitkeep              # Placeholder for model files
├── input
│   └── .gitkeep              # Placeholder for input video files
├── output
│   └── .gitkeep              # Placeholder for output subtitle files
├── requirements.txt          # Project dependencies
├── .env.example              # Environment variable template
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd whisper-video-captioning
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your video files in the `input` directory.
2. Configure any necessary environment variables in a `.env` file based on the `.env.example` template.
3. Run the application:
   ```
   python src/main.py
   ```

## Functionality

- **Video Processing**: The application extracts audio from video files and processes them for transcription.
- **Transcription**: Utilizes the OpenAI Whisper model to transcribe audio into text.
- **Subtitle Generation**: Formats the transcribed text into subtitle files and saves them in the `output` directory.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.