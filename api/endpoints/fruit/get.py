from cache import REDIS
from fastapi.responses import JSONResponse, PlainTextResponse
from loguru import logger

DOC = {
    200: {
        "description": "API response successfully",
        "content": {"application/json": {"example": {"name": "apple"}}},
    },
    400: {
        "description": "API response successfully",
        "content": {"text/plain": {"example": "Bad Request"}},
    },
}


def get(name: str):
    try:
        return JSONResponse({"name": name, "count": int(REDIS.get(name).decode())}, 200)
    except Exception as error:
        logger.warning(error)
        return PlainTextResponse("Bad Request", 400)
