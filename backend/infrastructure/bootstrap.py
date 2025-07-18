from application.use_cases.saver_use_case import SaverUseCase
from infrastructure.saver_adapter import SaverAdapter
from infrastructure.ytdlp_adapter import YtdlpAdapter

saver_use_case = SaverUseCase(SaverAdapter(), YtdlpAdapter())

