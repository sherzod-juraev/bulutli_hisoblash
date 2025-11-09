from fastapi import APIRouter, status
from .sum import dioganal_sum


b_router = APIRouter()


@b_router.post(
    '/',
    summary='dioganaldagi sonlar yigindisini hisoblash',
    status_code=status.HTTP_200_OK,
    response_model=float
)
async def dioganal(
        array: list[list[float]]
) -> float:
    total = await dioganal_sum(array)
    return total