# Author: Colin Chillingworth
# Simple mp4 player

import tkinter as tk
from tkinter import ttk
import vlc
from file_dialogs import select_file
from widgets import create_widgets
from functions import play_video, pause_video, close_video, quit_program, update_time, format_time, update_time_label, skip_backward, skip_forward, set_volume
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
        self.status_var = tk.StringVar()
        create_widgets(self)

    select_file = select_file
    create_widgets = create_widgets
    play_video = play_video
    pause_video = pause_video
    close_video = close_video
    quit_program = quit_program
    update_time = update_time
    format_time = format_time
    update_time_label = update_time_label
    skip_forward = skip_forward
    skip_backward = skip_backward
    set_volume = set_volume

    def format_time(self, seconds):
        """
        Convert seconds into a formatted time string.
        """
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return "{:02d}:{:02d}:{:02d}".format(int(h), int(m), int(s))

if __name__ == "__main__":
    app = Mp4Player()
    app.mainloop()