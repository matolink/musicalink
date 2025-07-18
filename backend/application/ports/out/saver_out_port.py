from abc import ABC, abstractmethod
from domain import Song


class SaverOutPort(ABC):
    @abstractmethod
    def save(self, song: Song) -> bool:
        ...
