from domains.__common__.base_errors import DomainError


def test_domain_error() -> None:
    assert DomainError().message == "Domain error occurred"
