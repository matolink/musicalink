from pydantic.dataclasses import dataclass


@dataclass
class Song:
    fs_name: str
    bytes: str | None = None
    md_artist: str | None = None
    md_album: str | None = None
    md_name: str | None = None
    md_img: str | None = None
    md_lyrics: str | None = None
