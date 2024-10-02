import os
from pytube import YouTube
from pydub import AudioSegment

# Function to download the audio from a YouTube video
def download_youtube_audio(youtube_url, output_path="downloads"):
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Download the YouTube video
        yt = YouTube(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Download and save as .mp4
        output_file = audio_stream.download(output_path)

        # Convert .mp4 to .mp3 using pydub
        base, ext = os.path.splitext(output_file)
        new_file = base + '.mp3'
        AudioSegment.from_file(output_file).export(new_file, format="mp3")

        # Optionally, remove the original .mp4 file
        os.remove(output_file)

        print(f"Downloaded and converted to MP3: {new_file}")
    except Exception as e:
        print(f"Error: {e}")


youtube_link = "https://www.youtube.com/watch?v=gLDIcr9Hjes"


download_youtube_audio(youtube_link)

