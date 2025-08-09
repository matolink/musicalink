from application.ports.out.tag_editor_out_port import TagEditorOutPort
from domain.Song import Song
from domain.Input import Input
import music_tag
import base64
import re


class MusicTagAdapter(TagEditorOutPort):
    def process(self, input: Input, song: Song):
        f = music_tag.load_file(song.fs_name)
        song.md_name = input.input_name
        song.md_artist = input.input_artist
        song.md_album = input.input_album
        song.md_lyrics = input.input_lyrics
        song.md_year = input.input_year
        if song.md_name:
            f['title'] = song.md_name
        if song.md_artist:
            f['artist'] = song.md_artist
        if song.md_album:
            f['album'] = song.md_album
        if song.md_lyrics:
            f['lyrics'] = song.md_lyrics
        if song.md_year:
            f['year'] = song.md_year
        if getattr(input, "input_art", None):
            img_data = re.sub(r"^data:image\/[a-zA-Z]+;base64,", "", input.input_art)
            song.md_artwork = base64.b64decode(img_data)
            f['artwork'] = song.md_artwork
            f['artwork'].first.raw_thumbnail([64, 64])
        f.save()
        return True
