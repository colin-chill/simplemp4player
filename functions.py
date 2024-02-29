
import time

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
        self.update_time()


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


def close_video(self):
    """
    close the current video playback.
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

def update_time(self):
    """
    Update the time interface with the current playback time.
    """
    while self.playing_video:
        length = self.media_player.get_length() / 1000
        time_pos = self.media_player.get_time() / 1000
        self.status_var.set(
            f"{self.format_time(time_pos)} / {self.format_time(length)}"
        )
        self.update_time_label()

        # Update progress bar
        if length > 0:
            progress = (time_pos / length) * 100
            self.progress_bar["value"] = progress

        self.update()
        time.sleep(0.1)

def update_time_label(self):
    """
    Update the time label with the current status.
    """
    self.time_label.config(text=self.status_var.get())

def format_time(seconds):
    """
    Convert seconds into a formatted time string.
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "{:02d}:{:02d}:{:02d}".format(int(h), int(m), int(s))

def skip_forward(self):
    """
    Skip forward 10 seconds in the video.
    """
    if self.playing_video:
        current_time = self.media_player.get_time()
        new_time = current_time + 10000  # 10 seconds in milliseconds
        self.media_player.set_time(new_time)

def skip_backward(self):
    """
    Skip backward 10 seconds in the video.
    """
    if self.playing_video:
        current_time = self.media_player.get_time()
        new_time = current_time - 10000  # 10 seconds in milliseconds
        self.media_player.set_time(new_time)

def set_volume(self, volume):
    """
    Set the volume of the media player.
    """
    volume_level = int(volume)
    self.media_player.audio_set_volume(volume_level)
