from fastapi import FastAPI
from app.api.quote import router as quote_router

app = FastAPI(title="Quote API")
app.include_router(quote_router, prefix="/quote")
