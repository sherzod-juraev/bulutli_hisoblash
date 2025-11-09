from fastapi import APIRouter, status, Body
from typing import Annotated
from .sum import sum_array

a_router = APIRouter()


@a_router.post(
    '/',
    summary='The sum of the numbers passing through the boundary of a matrix',
    status_code=status.HTTP_200_OK,
    response_model=float
)
async def total(
        array: Annotated[list[list[float]], Body()]
) -> float:
    total = await sum_array(array)
    return float(total)