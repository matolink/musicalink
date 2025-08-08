from application.ports.out.downloader_out_port import DownloaderOutPort
from domain.Input import Input
from domain.Song import Song
import yt_dlp
import os


class YtdlpAdapter(DownloaderOutPort):
    def download(self, ipt: Input) -> Song:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': './songs/%(title)s - [%(id)s].%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'
            }],
            'quiet': False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(ipt.url, download=True)
            file_path = ydl.prepare_filename(info)
            file_path = os.path.splitext(file_path)[0] + ".mp3"

        return Song(file_path)

