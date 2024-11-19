from pytube import Playlist, YouTube
import yt_dlp

'''
source /media/HDD/virtualenvs/experiments/bin/activate
'''
def download_video(video_url):
    ydl_opts = {}
    print(f'Downloading: {video_url}')

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


if __name__ == '__main__':
    url = input('Enter the YouTube video URL: ')
    download_video(url)

