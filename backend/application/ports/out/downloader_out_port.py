from abc import ABC, abstractmethod
from domain.Input import Input
from domain.Song import Song


class DownloaderOutPort(ABC):
    @abstractmethod
    def download(self, ipt: Input) -> Song:
        ...
