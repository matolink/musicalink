from application.ports.out.saver_out_port import SaverOutPort
from application.ports.out.downloader_out_port import DownloaderOutPort
from domain.Input import Input


class SaverUseCase:
    def __init__(self, saver: SaverOutPort, downloader: DownloaderOutPort):
        self.saver = saver
        self.downloader = downloader

    def execute(self, ipt: Input) -> bool:
        song = self.downloader.download(ipt)
        return self.saver.save(song)

