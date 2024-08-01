# downloader

A simple [yt-dlp](https://github.com/yt-dlp/yt-dlp) wrapper written in Python.

## Usage

The `main.py` (`downloader.exe`) script can be run from the terminal with the following arguments:

```python
main.py [urls] [-d/--download-folder] [-a/--audio_only] [--no-metadata] [--ui]
```

- `urls`: YouTube links to download.
- `-d/--download-folder`: Specify the download folder.
- `-a/--audio_only`: Download only the audio.
- `--no-metadata`: Download files without adding metadata and cover art.
- `--ui`: Run the user interface instead of the command line.

If no arguments are specified, it'll open the UI.

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
