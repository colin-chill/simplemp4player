import tkinter as tk
from tkinter import simpledialog
from youtube_search import YoutubeSearch
from pytube import YouTube


def search_and_download(self):
    """
    Search for a song on YouTube and download the selected video as an MP4.
    """
    # Get the song title from user input
    song_title = simpledialog.askstring("Search Song on YouTube", "Enter the song title:")

    if not song_title:
        return

    # Search for the song on YouTube
    results = YoutubeSearch(song_title, max_results=3).to_dict()

    # Display search results to user
    result_titles = [f"{i + 1}. {result['title']}" for i, result in enumerate(results)]
    result_msg = "\n".join(result_titles)
    selected_result = simpledialog.askinteger("Select Video", f"Select a video to download:\n{result_msg}\n")

    if selected_result is None or selected_result < 1 or selected_result > len(results):
        return

    # Get the selected video URL
    video_url = f"https://www.youtube.com/watch?v={results[selected_result - 1]['id']}"

    # Download the video as an MP4 file in the 'downloads' folder
    yt = YouTube(video_url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

    if stream:
        stream.download(output_path='videos/')
        tk.messagebox.showinfo("Download Complete", "Video downloaded successfully!")
    else:
        tk.messagebox.showerror("Error", "Could not download video.")

