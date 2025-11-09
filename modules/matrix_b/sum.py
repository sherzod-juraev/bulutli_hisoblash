from fastapi import HTTPException, status
from numpy import array as nm_array


async def dioganal_sum(
        array: list[list[float]],
        /
) -> float:
    matrix = nm_array(array)
    if matrix.ndim != 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='matritsa kiritilishi kerak'
        )
    if matrix.shape[0] % 2 != 1 and matrix.shape[0] != matrix.shape[1]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Array uzunligi toq bolishi kerak'
        )
    total = 0
    matrix_length = matrix.shape[0]
    for i in range(matrix_length):
        a = matrix[matrix_length - i - 1][i] if (matrix_length - i - 1) != i else 0
        total += matrix[i][i] + a
    return total