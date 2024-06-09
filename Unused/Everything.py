import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox
import asyncio
from idun_guardian_sdk import GuardianClient, FileTypes



"""def handle_drowsy(data):
    print(data.message)
    if data.get('stateless_z_scores'):
        # Extract the first dictionary in the list
        z_scores = data['stateless_z_scores'][0]

        # Extract the beta value
        beta = z_scores.get('Beta')
        if beta is not None:
            if beta < 1.0 or beta > 2.4:
                print(f"Beta out of range: {beta}")
                MP3Player.play_music()
            else:
                print(f"Beta in range: {beta}")
        else:
            print("Beta value is not available in the data.")

    else:
        print("stateless_z_scores is empty or not available.")
"""


is_beta_in_range = True

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
        self.load_music_folder(auto_start=False)
        # time.sleep(15)
        # self.stop_music()

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

    def play_music(self, auto_start=True):
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




my_api_token = "idun_QN0Cq1f2G3mpJjjblfC_hdW-AwftSG7jBaSpQU-XpHONk6IRXN4x13Yp"
RECORDING_TIMER = 100000    # 60 * 15  # 15 min


def print_data(data):
    print(data.message)


def check_beta(data):
    # Ensure 'stateless_z_scores' is a non-empty list
    # print(data.message)
    # print('hugo')
    # print(data.message.get('stateless_z_scores'))
    if data.message.get('stateless_z_scores'):
        # Extract the first dictionary in the list
        z_scores = data.message['stateless_z_scores'][0]
        # Extract the beta value
        beta = z_scores.get('Beta')
        if beta is not None:
            if beta < 1.0 or beta > 2.4:
                is_beta_in_range= False;
                print(f"Beta out of range: {beta}")

            else:
                is_beta_in_range = True
                print(f"Beta in range: {beta}")
        else:
            print("Beta value is not available in the data.")
    else:
        print("stateless_z_scores is empty or not available.")


if __name__ == "__main__":
    pygame.init()
    # Initialize pygame mixer
    pygame.mixer.init()
    # Create tkinter window
    root = tk.Tk()
    player = MP3Player(root)
    root.mainloop()
    root.after(15000, root.destroy())


    client = GuardianClient(api_token=my_api_token)
    client.address = asyncio.run(client.search_device())

    # subscribe_live_insights(raw_eeg=False, filtered_eeg=True, handler=print_data)
    client.subscribe_realtime_predictions(fft=True, jaw_clench=False, handler=check_beta)

    asyncio.run(client.start_recording(recording_timer=RECORDING_TIMER))
    rec_id = client.get_recording_id()

    print("RecordingId", rec_id)
    client.update_recording_tags(recording_id=rec_id, tags=["tag1", "tag2"])
    client.update_recording_display_name(recording_id=rec_id, display_name="todays_recordings")

    while 1:
        if is_beta_in_range:
            print("beta in range")
        else:
            print("beta out of range")
            player.play_music(auto_start=True)


