from application.ports.out.saver_out_port import SaverOutPort
from domain.Song import Song


class SaverAdapter(SaverOutPort):
    def save(self, song: Song) -> bool:
        print(song.fs_name)
        print("hola desde download en ytdlpadapter")
        return True


