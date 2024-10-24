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


def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    print(f'Downloading playlist: {playlist.title}')
    
    for video_url in playlist:
        download_video(video_url)

    print(f'Finished downloading playlist: {playlist.title}')


if __name__ == '__main__':
    url = input('Enter the YouTube playlist URL: ')
    download_playlist(url)

