from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def videoDownload(URL, savePath):
    try:
        YT = YouTube(URL)
        streams = YT.streams.filter(progressive=True, file_extension="mp4")
        highestResolutionStream = streams.getHighestResolution()
        highestResolutionStream.download(outputPath=savePath)
        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def openFileDialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    videoURL = input("Please enter a YouTube url: ")
    saveDirectory = openFileDialog()

    if saveDirectory:
        print("Started download...")
        videoDownload(videoURL, saveDirectory)
    else:
        print("Invalid save location.")