# -*- mode: python ; coding: utf-8 -*-

from dotenv import load_dotenv
import os

load_dotenv()

default_ffmpeg_path = 'bin\\ffmpeg.exe'
default_ffprobe_path = 'bin\\ffprobe.exe'
default_yt_dlp_path = 'bin\\yt-dlp.exe'

ffmpeg_path = os.getenv('FFMPEG_PATH', default_ffmpeg_path)
ffprobe_path = os.getenv('FFPROBE_PATH', default_ffprobe_path)
yt_dlp_path = os.getenv('YT_DLP_PATH', default_yt_dlp_path)

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('.\\icon.ico', '.'), (ffmpeg_path, 'bin\\'), (ffprobe_path, 'bin\\'), (yt_dlp_path, 'bin\\')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
