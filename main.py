from downloader import download
import argparse
import sys
import ui
import os

def main() -> None:
    parser = argparse.ArgumentParser(description='Download audio and video from YouTube links')
    parser.add_argument('urls', nargs='*', help='YouTube links')
    parser.add_argument('-d', '--download-folder', help='download folder')
    parser.add_argument('-a', '--audio_only', action='store_true', help='download only audio')
    parser.add_argument('--no-metadata', action='store_true', help='don\'t add metadata and cover art to downloaded files')
    parser.add_argument('--ui', action='store_true', help='run UI instead of command line')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        try:
            ui.main()
        except Exception as e:
            print('An error occurred while trying to create the GUI:')
            print(e)
        return

    if args.download_folder:
        os.makedirs(args.download_folder, exist_ok=True)
        os.chdir(args.download_folder)
    
    path = os.getcwd()
    if args.ui:
        try:
            app = ui.DownloadTool()
        except Exception as e:
            print('An error occurred while trying to create the GUI:')
            print(e)
            return
        app.create_widgets()
        os.chdir(path)
        app.path_label.configure(text="Download Path: " + os.getcwd())
        urls = set(args.urls)
        app.url_textbox.insert("1.0", '\n'.join(list(urls)) + ('\n' if urls else ''))
        app.audio_only_var.set(args.audio_only)
        app.no_metadata_var.set(args.no_metadata)
        app.window.mainloop()
        return
    download(args.urls, audio_only=args.audio_only, no_metadata=args.no_metadata, debug=True)

if __name__ == '__main__':
    main()
