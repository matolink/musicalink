from application.ports.out.saver_out_port import SaverOutPort
from application.ports.out.downloader_out_port import DownloaderOutPort
from application.ports.out.tag_editor_out_port import TagEditorOutPort
from domain.Input import Input


class SaverUseCase:
    def __init__(self, saver: SaverOutPort,
                 downloader: DownloaderOutPort,
                 tag_editor: TagEditorOutPort):
        self.saver = saver
        self.downloader = downloader
        self.tag_editor = tag_editor

    def execute(self, ipt: Input) -> bool:
        song = self.downloader.download(ipt)
        self.saver.save(song)
        return self.tag_editor.process(ipt, song)

