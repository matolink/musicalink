from abc import ABC, abstractmethod
from domain.Input import Input
from domain.Song import Song


class TagEditorOutPort(ABC):
    @abstractmethod
    def process(self, ipt: Input, sng: Song):
        ...
