import subprocess
import sys
import os


def download(urls, *, audio_only=False, no_metadata=False, debug=False) -> int:
    from_exe = getattr(sys, 'frozen', False)

    if from_exe:
        command = [fr"{os.path.dirname(__file__)}\bin\yt-dlp.exe"]
    else:
        command = ["yt-dlp"]
        

    command.extend(set(urls))

    if audio_only:
        command.extend(["--extract-audio", "--audio-format", "mp3"])
    else:
        command.extend(["--format", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"])

    if not no_metadata:
        command.extend(["--embed-metadata", "--embed-thumbnail"])
    
    command.extend(["-o", "%(title)s.%(ext)s"])

    if from_exe:
        command.extend(["--ffmpeg-location", fr"{os.path.dirname(__file__)}\bin"])

    creationflags = subprocess.CREATE_NO_WINDOW if not debug else 0
    return subprocess.run(command, creationflags=creationflags).returncode
