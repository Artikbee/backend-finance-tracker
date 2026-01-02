import pytest

from domains.category.models import Category
from domains.category.value_objects import CategoryName
from domains.user.models import UserID


@pytest.mark.models
def test_create_category(category: Category) -> None:
    assert isinstance(category, Category)
    assert category.user_id == UserID(1)
    assert category.name == CategoryName("Food")
    assert category.oid is None


@pytest.mark.models
def test_update_name(category: Category) -> None:
    category.update_name(CategoryName("Travel"))
    assert category.name == CategoryName("Travel")
