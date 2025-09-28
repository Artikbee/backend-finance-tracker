import pytest

from domains.__common__.base_errors import FieldError
from domains.category.errors import CategoryNameMinError, CategoryNameMaxError
from domains.category.value_objects import CategoryName


@pytest.mark.value_objects
@pytest.mark.parametrize(
    ("value", "exc_class"),
    [
        ("", CategoryNameMinError),
        ("1", None),
        ("1" * 100, None),
        ("1" * 101, CategoryNameMaxError),
    ]

)
def test_category_name(
        value: str,
        exc_class: type[FieldError] | None,
) -> None:
    if exc_class:
        with pytest.raises(exc_class) as excinfo:
            _ = CategoryName(value)

        name_min_length = 1
        if len(value) < name_min_length:
            msg = "The category name length should not less than 1"
        else:
            msg = "The category name length should not exceed 100"
        assert excinfo.value.message == msg
    else:
        category_name = CategoryName(value)
        assert value == category_name.value
        assert isinstance(category_name, CategoryName)
