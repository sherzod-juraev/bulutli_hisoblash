from fastapi import APIRouter, status
from .sum import romb_sum


e_router = APIRouter()


@e_router.post(
    '/',
    summary='Rombdagi sonlar yigindisi',
    status_code=status.HTTP_200_OK,
    response_model=float
)
async def romb(
        array: list[list[float]]
) -> float:
    total = await romb_sum(array)
    return total