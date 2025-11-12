from fastapi import APIRouter
from route.query import router as query_router


router = APIRouter()
router.include_router(query_router)
