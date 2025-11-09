from fastapi import APIRouter, status
from .sum import dioganal_sum


d_router = APIRouter()


@d_router.post(
    '/',
    summary='Matritsaning dioganal elementlari yigindisi',
    status_code=status.HTTP_200_OK,
    response_model=float
)
async def dioganal(
        array: list[list[float]]
) -> float:
    sum = await dioganal_sum(array)
    return sum