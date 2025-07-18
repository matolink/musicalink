from fastapi import APIRouter
from domain.Input import Input
from infrastructure.bootstrap import saver_use_case

router = APIRouter()


@router.post("/process/", tags=["users"])
async def process_input(ipt: Input):
    return saver_use_case.execute(ipt)
    


