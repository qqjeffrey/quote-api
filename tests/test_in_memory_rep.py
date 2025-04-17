from app.infrastructure.in_memory_repository import InMemoryQuoteRepository
from app.domain.models import Quote

def test_get_random_empty_list():
    repo = InMemoryQuoteRepository()
    result = repo.get_random()
    assert result.text == "No quotes yet"
    assert result.author == "System"