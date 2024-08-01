from downloader import download
from tkinter import filedialog
import customtkinter as ctk
import threading
import os


class DownloadTool:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Download Tool")
        self.window.geometry("475x375")
        self.window.resizable(False, False)
        script_directory = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_directory, 'icon.ico')
        self.window.iconbitmap(icon_path)

        self.url_textbox = None
        self.download_folder = None
        self.audio_only_var = None
        self.no_metadata_var = None
        self.debug_var = None

        self.download_result = 0
        self.download_button_color = None
    
    def change_path(self):
        if (directory := filedialog.askdirectory()):
            os.chdir(directory)
        self.path_label.configure(text="Download Path: " + os.getcwd())
    
    def download(self):
        self.download_button.configure(state=ctk.DISABLED, text="Downloading...")  # Disable the download button
        urls = self.url_textbox.get("1.0", "end-1c").split()
        
        thread = threading.Thread(target=self.download_thread, args=(urls,), kwargs={"audio_only": self.audio_only_var.get(), "no_metadata": self.no_metadata_var.get(), "debug": self.debug_var.get()})
        thread.start()
        self.window.after(100, self.check_thread_status, thread)  # Start checking the thread status after 100ms

    def download_thread(self, urls, **kwargs):
        self.download_button.configure(fg_color=self.download_button_color)
        self.download_result = download(urls, **kwargs)

    def check_thread_status(self, thread):
        if thread.is_alive():
            self.window.after(100, self.check_thread_status, thread)  # Schedule another check after 100ms
        else:
            self.download_button.configure(state=ctk.NORMAL, text="Download")  # Enable the download button
            if self.download_result != 0:
                self.download_button.configure(fg_color="red")

    def create_widgets(self):
        # URL entry box
        url_label = ctk.CTkLabel(self.window, text="Enter URLs (separated by spaces):")
        url_label.pack(pady=5)
        self.url_textbox = ctk.CTkTextbox(self.window, width=400, height=125)
        self.url_textbox.pack(pady=5)

        # Download options
        options_frame = ctk.CTkFrame(self.window)
        options_frame.pack(pady=10)
        self.audio_only_var = ctk.BooleanVar(value=False)
        audio_only_checkbox = ctk.CTkCheckBox(options_frame, text="Audio Only", variable=self.audio_only_var)
        audio_only_checkbox.pack(side=ctk.LEFT, padx=5, pady=5)
        self.no_metadata_var = ctk.BooleanVar(value=False)
        no_metadata_checkbox = ctk.CTkCheckBox(options_frame, text="No Metadata", variable=self.no_metadata_var)
        no_metadata_checkbox.pack(side=ctk.LEFT, padx=5, pady=5)
        
        # Download path selection
        os.chdir(os.path.expanduser('~\\Downloads'))
        path_frame = ctk.CTkFrame(self.window)
        path_frame.pack(pady=10)
        self.path_label = ctk.CTkLabel(path_frame, text="Download Path: " + os.getcwd(), wraplength=300)
        self.path_label.pack(side=ctk.LEFT, padx=5, pady=5)
        change_path_button = ctk.CTkButton(path_frame, text="Change Path", command=self.change_path)
        change_path_button.pack(side=ctk.LEFT, padx=5, pady=5)

        # Debug checkbox at the bottom left
        download_frame = ctk.CTkFrame(self.window)
        download_frame.pack(side=ctk.BOTTOM, pady=20)
        self.debug_var = ctk.BooleanVar(value=False)
        debug_checkbox = ctk.CTkCheckBox(download_frame, text="Debug", variable=self.debug_var)
        debug_checkbox.pack(padx=5, pady=5, side=ctk.RIGHT)

        # Download button
        self.download_button = ctk.CTkButton(download_frame, text="Download", command=self.download, width=180, height=40)
        self.download_button_color = self.download_button.cget('fg_color')
        self.download_button.pack(padx=5, pady=5, side=ctk.LEFT, anchor=ctk.SW)
        
    
    def run(self):
        self.create_widgets()
        self.window.mainloop()

def main():
    app = DownloadTool()
    app.run()

if __name__ == "__main__":
    main()
