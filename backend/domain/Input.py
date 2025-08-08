from pydantic.dataclasses import dataclass


@dataclass
class Input:
    url: str
    input_name: str | None = None
    input_artist: str | None = None
    input_album: str | None = None
    input_lyrics: str | None = None
