from app.domain.models import Quote
from app.domain.repositories import QuoteRepository
from typing import List

class QuoteService:
    def __init__(self, repo: QuoteRepository):
        self.repo = repo

    def add_quote(self, quote: Quote) -> Quote:
        return self.repo.add(quote)

    def get_by_author(self, author: str) -> List[Quote]:
        return self.repo.get_by_author(author)

    def get_random(self) -> Quote:
        return self.repo.get_random()
