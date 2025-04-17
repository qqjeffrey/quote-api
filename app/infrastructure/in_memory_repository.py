import random
from typing import List
from app.domain.models import Quote
from app.domain.repositories import QuoteRepository

class InMemoryQuoteRepository(QuoteRepository):
    def __init__(self):
        self.quotes: List[Quote] = []

    def add(self, quote: Quote) -> Quote:
        self.quotes.append(quote)
        return quote

    def get_by_author(self, author: str) -> List[Quote]:
        return [q for q in self.quotes if q.author == author]

    def get_random(self) -> Quote:
        return random.choice(self.quotes) if self.quotes else Quote(text="No quotes yet", author="System")
