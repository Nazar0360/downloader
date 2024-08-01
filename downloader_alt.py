import yt_dlp
import random
import copy
import sys
import os

'''
This is an alternative to downloader.py, witch imports yt-dlp as module instead of using it from
terminal. This means you can exclude yt-dlp.exe from the final build. It should work if you replace
downloader.py with this file but it is not tested and may be defective. Also it creates a TEMP folder
while downloading because I can't figure out how to make yt-dlp add cover art without downloading the
playlist cover as well (if downloading one).
'''

__all__ = ['download']

ydl_audio_opts = {
    'format': 'bestaudio[ext=mp3]/bestaudio[ext=m4a]/best',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'},
        {'key': 'FFmpegMetadata'},
        {'key': 'EmbedThumbnail'}
    ],
    'outtmpl': '%(channel)s - %(title)s.%(ext)s',
    'writethumbnail': True
}

ydl_video_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'postprocessors': [ 
        {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'},
        {'key': 'FFmpegMetadata'},
        {'key': 'EmbedThumbnail'}
    ],
    'outtmpl': '%(channel)s - %(title)s.%(ext)s',
    'writethumbnail': True
}

def _create_temp_dir() -> None:
    temp_dir = 'TEMP' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))
    os.mkdir(temp_dir)
    return temp_dir

def _remove_temp_dir(temp_dir: str) -> None:
    os.chdir('..')
    for filename in os.listdir(temp_dir):
        if os.path.isfile(filename):
            os.remove(filename)
        os.rename(f'{temp_dir}/{filename}', f'./{filename}')
    os.rmdir(temp_dir)

def download(urls, *, only_audio=False, no_metadata=False, debug) -> None:
    ydl_opts = copy.deepcopy(ydl_audio_opts if only_audio else ydl_video_opts)
    from_exe = getattr(sys, 'frozen', False)

    if from_exe:
        ydl_opts.update({'ffmpeg_location': fr'{os.path.dirname(__file__)}\bin'})
    
    if no_metadata:
        ydl_opts['postprocessors'].pop(-1)
        ydl_opts['postprocessors'].pop(-1)
        ydl_opts.pop('writethumbnail')
    
    if not no_metadata:
        temp_dir = _create_temp_dir()
        os.chdir(temp_dir)
        print('Temporary folder created:', temp_dir)
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
        if not no_metadata:
            for filename in os.listdir():
                _, ext = os.path.splitext(filename)
                if ext in ['.webp', '.png', '.jpg', '.jpeg']:
                    os.remove(filename)
    except KeyboardInterrupt:
        return 3
    except Exception:
        return 1
    finally:
        if not no_metadata:
            _remove_temp_dir(temp_dir)
            print('Temporary folder removed')
    return 0
