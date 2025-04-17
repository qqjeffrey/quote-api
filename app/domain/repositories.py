from abc import ABC, abstractmethod
from app.domain.models import Quote
from typing import List

class QuoteRepository(ABC):
    @abstractmethod
    def add(self, quote: Quote) -> Quote:
        pass

    @abstractmethod
    def get_by_author(self, author: str) -> List[Quote]:
        pass

    @abstractmethod
    def get_random(self) -> Quote:
        pass
