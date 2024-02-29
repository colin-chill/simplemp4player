from tkinter import filedialog

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