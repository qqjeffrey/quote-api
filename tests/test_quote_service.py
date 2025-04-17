import pytest
from unittest.mock import MagicMock
from app.domain.models import Quote
from app.service.quote_service import QuoteService

def test_add_quote():
    mock_repo = MagicMock()
    service = QuoteService(mock_repo)
    
    quote = Quote(text="Test quote", author="Tester")
    mock_repo.add.return_value = quote

    result = service.add_quote(quote)

    mock_repo.add.assert_called_once_with(quote)
    assert result.text == "Test quote"
    assert result.author == "Tester"


def test_get_random():
    mock_repo = MagicMock()
    service = QuoteService(mock_repo)

    expected = Quote(text="Random", author="AI")
    mock_repo.get_random.return_value = expected

    result = service.get_random()

    mock_repo.get_random.assert_called_once()
    assert result == expected