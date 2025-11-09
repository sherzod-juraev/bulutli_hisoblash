from fastapi import APIRouter


# import routers
from .matrix_a import a_router
from .matrix_b import b_router
from .matrix_d import d_router
from .matrix_e import e_router

api_router = APIRouter()

api_router.include_router(
    a_router,
    prefix='/a',
    tags=['A matrix']
)

api_router.include_router(
    b_router,
    prefix='/b',
    tags=['B matrix']
)

api_router.include_router(
    d_router,
    prefix='/d',
    tags=['D matrix']
)

api_router.include_router(
    e_router,
    prefix='/e',
    tags=['E matrix']
)