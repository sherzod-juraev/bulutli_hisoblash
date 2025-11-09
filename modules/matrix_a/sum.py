from numpy import array as nm_array
from fastapi import HTTPException, status

async def sum_array(
        array: list[list[float]]
) -> float:
    matrix = nm_array(array)
    if matrix.ndim != 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='2D matritsa kiritishingiz kerak'
        )
    if matrix.shape[0] != matrix.shape[1] and matrix.shape[0] < 3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Bunday shakl uchun a holat bajarilmaydi'
        )
    total = matrix[0, 1:-1].sum() + matrix[-1, 1:-1].sum() + matrix[:, 0].sum() + matrix[:, -1].sum()
    return total