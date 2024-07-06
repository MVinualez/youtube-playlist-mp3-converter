import locale
import json
import os
from pytube import Playlist, YouTube
from moviepy.editor import AudioFileClip

def load_messages(filename='messages.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

language_code = locale.getdefaultlocale()[0][:2]
messages = load_messages()

if language_code in messages:
    lang = language_code
else:
    lang = 'en'

def download_youtube_video_as_mp3(url, output_path='.'):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()

        print(f"{messages[lang]['downloading_video']} {url}")
        download_path = video.download(output_path)

        base, ext = os.path.splitext(download_path)
        mp3_path = base + '.mp3'

        audio_clip = AudioFileClip(download_path)
        audio_clip.write_audiofile(mp3_path)

        audio_clip.close()
        os.remove(download_path)

        print(f"{messages[lang]['download_completed']} {mp3_path}")
    except Exception as e:
        print(f"{messages[lang]['error_occurred']} {e}")

def download_youtube_playlist_as_mp3(playlist_url, output_path='.'):
    try:
        playlist = Playlist(playlist_url)

        print(f"{messages[lang]['downloading_playlist']} {playlist.title}")
        print(f"{messages[lang]['number_of_videos']} {len(playlist.video_urls)}")

        for url in playlist.video_urls:
            download_youtube_video_as_mp3(url, output_path)

        print(messages[lang]['playlist_download_completed'])
    except Exception as e:
        print(f"{messages[lang]['error_occurred']} {e}")

def main():
    choice = input(f"{messages[lang]['choose_operation_mode']} ").strip().lower()

    if choice == 'p':
        playlist_url = input(messages[lang]['enter_playlist_url'])
        output_path = input(messages[lang]['enter_output_path'])

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        download_youtube_playlist_as_mp3(playlist_url, output_path)
    elif choice == 'v':
        video_url = input(messages[lang]['enter_video_url'])
        output_path = input(messages[lang]['enter_output_path'])

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        download_youtube_video_as_mp3(video_url, output_path)
    else:
        print(messages[lang]['invalid_choice'])

if __name__ == "__main__":
    main()
