from src.domains.__common__.errors import DomainError


def test_domain_error() -> None:
    assert DomainError().message == "Domain error occurred"
