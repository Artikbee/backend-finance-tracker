import pytest

from domains.__common__.base_errors import FieldError
from domains.transaction.errors import TransactionDescriptionMinError, TransactionDescriptionMaxError
from domains.transaction.value_objects import TransactionDescription


@pytest.mark.value_objects
@pytest.mark.parametrize(
    ("value", "exc_class"),
    [
        ("", TransactionDescriptionMinError),
        ("f", None),
        ("f" * 100, None),
        ("f" * 101, TransactionDescriptionMaxError),
    ]

)
def test_transaction_description(
        value: str,
        exc_class: type[FieldError] | None,
) -> None:
    if exc_class:
        with pytest.raises(exc_class) as excinfo:
            _ = TransactionDescription(value)

        description_min_length = 1
        if len(value) < description_min_length:
            msg = "The description length should not less than 1"
        else:
            msg = "The description length should not exceed 100"
        assert excinfo.value.message == msg
    else:
        transaction_description = TransactionDescription(value)
        assert value == transaction_description.value
        assert isinstance(transaction_description, TransactionDescription)
