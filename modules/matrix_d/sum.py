from numpy import array as nm_array
from fastapi import HTTPException, status


async def dioganal_sum(
        array: list[list[float]]
) -> float:
    matrix = nm_array(array)
    if matrix.ndim != 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='matritsa kiritilishi kerak'
        )
    if matrix.shape[0] % 2 != 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Array uzunligi toq bolishi kerak'
        )
    matrix_length = matrix.shape[0]
    range_length = matrix.shape[0] // 2 + 1
    total = 0
    for i in range(range_length):
        a = matrix[matrix_length-i-1,i:matrix_length-i].sum() if (matrix_length-i-1) != i else 0
        total += matrix[i,i:matrix_length-i].sum() + a
    return total