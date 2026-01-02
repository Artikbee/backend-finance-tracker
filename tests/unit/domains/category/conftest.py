import pytest

from domains.category.models import Category
from domains.category.value_objects import CategoryName
from domains.user.models import UserID


@pytest.fixture(scope="module")
def category() -> Category:
    return Category.create(
        user_id=UserID(1),
        name=CategoryName("Food"),
    )
