from fastapi import APIRouter, Depends, Query
from app.domain.models import Quote
from app.infrastructure.in_memory_repository import InMemoryQuoteRepository
from app.service.quote_service import QuoteService

router = APIRouter()

repo = InMemoryQuoteRepository()
service = QuoteService(repo)

@router.get("/random", response_model=Quote)
def get_random_quote():
    return service.get_random()

@router.get("", response_model=list[Quote])
def get_by_author(author: str = Query(...)):
    return service.get_by_author(author)

@router.post("", response_model=Quote)
def add_quote(quote: Quote):
    return service.add_quote(quote)
