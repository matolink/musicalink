from application.ports.out.tag_editor_out_port import TagEditorOutPort
from domain.Song import Song
from domain.Input import Input
import music_tag


class MusicTagAdapter(TagEditorOutPort):
    def process(self, input: Input, song: Song):
        f = music_tag.load_file(song.fs_name)
        song.md_name = input.input_name
        song.md_artist = input.input_artist
        song.md_album = input.input_album
        song.md_lyrics = input.input_lyrics
        if song.md_name:
            f['title'] = song.md_name
        if song.md_artist:
            f['artist'] = song.md_artist
        if song.md_album:
            f['album'] = song.md_album
        if song.md_lyrics:
            f['lyrics'] = song.md_lyrics
        # if song.md_img:
        #     with open(song.md_img, 'rb') as img_file:
        #         f['artwork'] = img_file.read()
        f.save()
        return True
