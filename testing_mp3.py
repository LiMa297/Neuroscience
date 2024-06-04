import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize pygame mixer
pygame.mixer.init()


class MP3Player:
    def __init__(self, root):
        self.root = root
        self.root.title("MP3 Player")
        self.root.geometry("300x200")

        # Frame for buttons
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.play_button = tk.Button(self.frame, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self.frame, text="Pause", command=self.pause_music)
        self.pause_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.frame, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT)

        self.load_music_button = tk.Button(self.frame, text="Load Music Folder", command=self.load_music_folder)
        self.load_music_button.pack(side=tk.LEFT)

        self.music_files = []
        self.current_track = 0

        # Automatically load and play music from a folder
        self.load_music_folder(auto_start=True)

    def load_music_folder(self, auto_start=False):
        # Replace with your music folder path or use a file dialog
        music_folder = "C:/Users/eliwa/OneDrive/Desktop/MP3_Music"
        # music_folder = ""C:\Users\eliwa\OneDrive\Desktop\MP3_Music""  # for hard-coded path

        if not music_folder:
            return

        self.music_files = [os.path.join(music_folder, file) for file in os.listdir(music_folder) if
                            file.endswith(".mp3")]

        if not self.music_files:
            messagebox.showerror("Error", "No MP3 files found in the selected folder.")
            return

        if auto_start:
            self.play_music(auto_start=True)

    def play_music(self, auto_start=False):
        if not self.music_files:
            messagebox.showerror("Error", "No music files loaded.")
            return

        if not pygame.mixer.music.get_busy() or auto_start:
            pygame.mixer.music.load(self.music_files[self.current_track])
            pygame.mixer.music.play()
            print(f"Now playing: {self.music_files[self.current_track]}")

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()


# Create tkinter window
root = tk.Tk()
player = MP3Player(root)
root.mainloop()