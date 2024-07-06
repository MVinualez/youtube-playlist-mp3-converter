# YouTube Playlist MP3 Converter

YouTube Playlist MP3 Converter is a Python script that allows you to download all videos from a YouTube playlist as MP3 files, or download a single YouTube video and convert it to MP3. The script supports multiple languages and determines the user's language based on the operating system's locale settings.

## Features

- Download all videos from a YouTube playlist as MP3 files
- Download a single YouTube video and convert it to MP3
- Supports multiple languages (English, French, Spanish, German, Simplified Chinese, Japanese, Russian)
- Automatically determines the user's language based on the OS locale
- Allows specifying the output directory for the downloaded files

## Installation

### Prerequisites

- Python 3.x
- [pytube](https://pypi.org/project/pytube/)
- [moviepy](https://pypi.org/project/moviepy/)

You can install the required Python packages using pip:

```bash
pip install pytube moviepy
```

### Clone the Repository

```bash
git clone https://github.com/MVinualez/youtube-playlist-mp3-converter.git
cd youtube-playlist-mp3-converter
```

## Usage

1. Run the script:

```bash
python main.py
```

2. Choose the operation mode:
   - Enter 'P' to download a YouTube playlist.
   - Enter 'V' to download a single YouTube video.

3. Depending on your choice:
   - For downloading a playlist:
     - Enter the URL of the YouTube playlist.
     - Enter the destination folder (relative or absolute path).
   - For downloading a single video:
     - Enter the URL of the YouTube video.
     - Enter the destination folder (relative or absolute path).

The script will download the videos as MP3 files to the specified folder.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [pytube](https://pypi.org/project/pytube/)
- [moviepy](https://pypi.org/project/moviepy/)
