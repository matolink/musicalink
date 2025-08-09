from application.use_cases.saver_use_case import SaverUseCase
from infrastructure.ytdlp_adapter import YtdlpAdapter
from infrastructure.music_tag_adapter import MusicTagAdapter

saver_use_case = SaverUseCase(YtdlpAdapter(),
                              MusicTagAdapter())
