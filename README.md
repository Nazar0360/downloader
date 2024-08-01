# downloader

A simple [yt-dlp](https://github.com/yt-dlp/yt-dlp) wrapper written in Python.

## Usage

```
usage: main.py [-h] [-d DOWNLOAD_FOLDER] [-a] [--no-metadata] [--ui] [urls ...]

Download audio and video from YouTube links

positional arguments:
  urls                  YouTube links

options:
  -h, --help            show this help message and exit
  -d DOWNLOAD_FOLDER, --download-folder DOWNLOAD_FOLDER
                        download folder
  -a, --audio_only      download only audio
  --no-metadata         don't add metadata and cover art to downloaded files
  --ui                  run UI instead of command line
```

If no arguments are specified, it'll open the UI.

For bash, you can use `downloader`, which is just a shortcut for `python main.py`; `downloader.exe` can run from terminal too.

## User Interface

Simple UI contains:

- multiline textbox for URLs (separated by whitespace)
- options for "Audio Only" and "No Metadata"
- path selector
- download button
- debug checkbox (opens terminal while downloading)

## Building Executable

To build the `downloader.exe` executable, use the `downloader.spec` file. Ensure you have the following executables in your environment:

- `ffmpeg`
- `ffprobe`
- `yt-dlp`

You can specify the paths to these executables in a `.env` file using the following keys:

- `FFMPEG_PATH`
- `FFPROBE_PATH`
- `YT_DLP_PATH`

To create the executable, run the following command (you have to have `pyinstaller` installed):

```bash
pyinstaller --noconfirm .\downloader.spec
```

## Requirements

Ensure you have the necessary dependencies installed by running:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE.md).
