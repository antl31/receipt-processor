from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import init_db
from app.views.receipt import router as receipt_router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    # Load the DB
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(receipt_router)
