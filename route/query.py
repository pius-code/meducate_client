from fastapi import APIRouter
from core.query_processor import process_query

router = APIRouter(prefix="/query", tags=["use the mcp"])


@router.post(
    "/",
    summary="Use this to use meducate's mcp tools",
    description="Does magic",  # noqa
)
async def query_meducate(query: str):
    print("hii, you hit the query route")
    result = await process_query(query)
    return result
