# Author: Colin Chillingworth
# Simple mp4 player

import tkinter as tk
import vlc
from tkinter import filedialog

class Mp4Player(tk.Tk):
    """
    A simple MP4 player application using tkinter and VLC.
    """

    def __init__(self):
        """
        Initialize the MP4 player window.
        """
        super().__init__()
        self.title("Mp4 Player")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")
        self.initialize_player()

    def initialize_player(self):
        """
        Initialize the VLC media player.
        """
        self.instance = vlc.Instance()
        self.media_player = self.instance.media_player_new()
        self.current_file = None
        self.playing_video = False
        self.video_paused = False
        self.create_widgets()

    def create_widgets(self):
        """
        Create GUI widgets.
        """
        self.media_canvas = tk.Canvas(self, bg="black", width=800, height=400)
        self.media_canvas.pack(pady=10, fill=tk.BOTH, expand=True)

        # Button for file selection
        self.select_file_button = tk.Button(
            self,
            text="Select File",
            font=("Arial", 12, "bold"),
            command=self.select_file,
        )
        self.select_file_button.pack(pady=5)
        self.control_buttons_frame = tk.Frame(self, bg="#f0f0f0")
        self.control_buttons_frame.pack(pady=5)

        # Button for pausing video
        self.pause_button = tk.Button(
            self.control_buttons_frame,
            text="Pause",
            font=("Arial", 12, "bold"),
            bg="#FF9800",
            fg="white",
            command=self.pause_video,
        )
        self.pause_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Button for closing current video to allow for new file selection
        self.stop_button = tk.Button(
            self.control_buttons_frame,
            text="Stop",
            font=("Arial", 12, "bold"),
            bg="#F44336",
            fg="white",
            command=self.stop,
        )
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=5)

        # Button to quit the player
        self.quit_button = tk.Button(
            self.control_buttons_frame,
            text="Quit",
            font=("Arial", 12, "bold"),
            bg="#607D8B",
            fg="white",
            command=self.quit_program,
        )
        self.quit_button.pack(side=tk.LEFT, padx=10, pady=5)

    def select_file(self):
        """
        Open a file dialog to select an MP4 file.
        """
        file_path = filedialog.askopenfilename(
            filetypes=[("Media Files", "*.mp4 *.avi")]
        )
        if file_path:
            self.current_file = file_path
            self.play_video()

    def play_video(self):
        """
        Play the selected video.
        """
        if not self.playing_video:
            media = self.instance.media_new(self.current_file)
            self.media_player.set_media(media)
            self.media_player.set_hwnd(self.media_canvas.winfo_id())
            self.media_player.play()
            self.playing_video = True

    def pause_video(self):
        """
        Pause or resume the video playback.
        """
        if self.playing_video:
            if self.video_paused:
                self.media_player.play()
                self.video_paused = False
                self.pause_button.config(text="Pause", bg="#FF9800")
            else:
                self.media_player.pause()
                self.video_paused = True
                self.pause_button.config(text="Resume", bg="#4CAF50")

    def stop(self):
        """
        Stop the video playback.
        """
        if self.playing_video:
            self.media_player.stop()
            self.playing_video = False

    # Quit the program
    def quit_program(self):
        """
        Quit the MP4 player application.
        """
        self.destroy()

if __name__ == "__main__":
    app = Mp4Player()
    app.mainloop()