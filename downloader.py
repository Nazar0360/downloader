import subprocess
import sys
import os

audio_formats = ["aac", "alac", "flac", "m4a", "mp3", "opus", "vorbis", "wav"]
# ffmpeg can't convert into mov and webm
# video_formats = ["avi", "flv", "mkv", "mov", "mp4", "webm"]
video_formats = ["avi", "flv", "mkv", "mp4"]
thumbnail_embeddable_formats = ["mp3", "mkv", "opus", "flac", "m4a", "mp4", "mov"]
subs_embeddable_formats = ["mp4", "webm", "mkv"]


def download(urls, *, audio_only=False, no_metadata=False, download_format=None, debug=False) -> int:
    from_exe = getattr(sys, 'frozen', False)

    if from_exe:
        command = [fr"{os.path.dirname(__file__)}\bin\yt-dlp.exe"]
    else:
        command = ["yt-dlp"]
        
    command.extend(set(urls))

    if audio_only:
        command.extend(["--extract-audio", "--audio-quality", "0"])
        if download_format is not None:
            download_format = download_format if download_format in audio_formats else "mp3"
            command.extend(["--audio-format", download_format])
    else:
        if download_format is not None:
            download_format = download_format if download_format in video_formats else "mp4"
            command.extend(["--remux-video", download_format, "--merge-output-format", download_format])

    if not no_metadata:
        command.extend(["--embed-metadata"])
        if download_format in thumbnail_embeddable_formats:
            command.extend(["--embed-thumbnail"])
        if not audio_only and download_format in subs_embeddable_formats:
            command.extend(["--embed-subs"])
    
    command.extend(["-o", "%(title)s.%(ext)s"])

    if from_exe:
        command.extend(["--ffmpeg-location", fr"{os.path.dirname(__file__)}\bin"])

    creationflags = subprocess.CREATE_NO_WINDOW if not debug else 0
    return subprocess.run(command, creationflags=creationflags).returncode
