from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(str(url))
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res = streams.get_highest_resolution()
        highest_res.download(output_path=save_path)
        print('Video downloaded sucessfully')
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    
    if folder:
        print(f"Selected folder: {folder}")
    
    return folder


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    url = input('Enter the video URL: ')
    path = open_file_dialog()

    if not path:
        print("invalid save location. Exiting...")
    else:
        print(f"Downloading video to {path}...")
        download_video(url, path)
        
