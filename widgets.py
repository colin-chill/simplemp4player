import tkinter as tk
from tkinter import ttk

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

    # Label for time interface

    self.time_label = tk.Label(
        self,
        text="00:00:00 / 00:00:00",
        font=("Arial", 12, "bold"),
        fg="#555555",
        bg="#f0f0f0",
    )
    self.time_label.pack(pady=5)

    # Progress bar for video playback
    self.progress_bar = ttk.Progressbar(
        self,
        orient=tk.HORIZONTAL,
        mode="determinate",
        length=600,  # Adjust length as needed
    )
    self.progress_bar.pack(pady=5)

    self.control_buttons_frame = tk.Frame(self, bg="#f0f0f0")
    self.control_buttons_frame.pack(pady=5)

    self.control_buttons_frame = tk.Frame(self, bg="#f0f0f0")
    self.control_buttons_frame.pack(pady=5)

    # Volume label
    self.volume_label = tk.Label(
        self.control_buttons_frame,
        text="🔊",
        font=("Arial", 20, "bold"),
        fg="#555555",
        bg="#f0f0f0",
    )
    self.volume_label.pack(side=tk.LEFT, padx=0, pady=0)

    # Volume slider
    self.volume_slider = tk.Scale(
        self.control_buttons_frame,
        from_=0,
        to=100,
        orient=tk.HORIZONTAL,
        command=self.set_volume,
        length=100,
        showvalue=0,
        troughcolor="#f0f0f0",
        sliderlength=20,
    )
    self.volume_slider.set(50)  # Set default volume to 50
    self.volume_slider.pack(side=tk.LEFT, padx=0, pady=5)

    # Button for skipping backward 10 seconds
    self.skip_back_button = tk.Button(
        self.control_buttons_frame,
        text="⏪",
        font=("Arial", 12, "bold"),
        bg="#2196F3",
        fg="white",
        command=self.skip_backward,
    )
    self.skip_back_button.pack(side=tk.LEFT, padx=10, pady=5)

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

    # Button for skipping forward 10 seconds
    self.skip_forward_button = tk.Button(
        self.control_buttons_frame,
        text="⏩",
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        command=self.skip_forward,
    )
    self.skip_forward_button.pack(side=tk.LEFT, padx=10, pady=5)

    # Search and Download button
    self.search_download_button = tk.Button(
        self.control_buttons_frame,
        text="Search and Download",
        font=("Arial", 12, "bold"),
        bg="#FF5722",
        fg="white",
        command=self.search_and_download,
    )
    self.search_download_button.pack(side=tk.LEFT, padx=10, pady=5)

    # Button for closing current video to allow for new file selection
    self.close_button = tk.Button(
        self.control_buttons_frame,
        text="Close File",
        font=("Arial", 12, "bold"),
        bg="#F44336",
        fg="white",
        command=self.close_video,
    )
    self.close_button.pack(side=tk.LEFT, padx=10, pady=5)

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