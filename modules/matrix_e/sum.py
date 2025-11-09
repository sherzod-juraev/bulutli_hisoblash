from fastapi import HTTPException, status
from numpy import array as nm_array

async def romb_sum(
        array: list[list[float]],
        /
) -> float:
    matrix = nm_array(array)
    if matrix.ndim != 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Matritsa kiritishingiz kerak'
        )
    if matrix.shape[0] != matrix.shape[1] and matrix.shape[0] % 2 != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Matritsa uzunligi toq bolsin'
        )
    matrix_length = matrix.shape[0]
    range_start = matrix.shape[0] // 2
    total = 0
    for i, j in enumerate(range(range_start, -1, -1)):
        a = matrix[matrix_length-j-1,i:matrix_length-i].sum() if matrix_length - j - 1 != j else 0
        total += matrix[j,i:matrix_length-i].sum() + a
    return total