from infrastructure.persistence.models.account import map_account_table
from infrastructure.persistence.models.category import map_category_table
from infrastructure.persistence.models.transaction import map_transaction_table
from infrastructure.persistence.models.user import map_user_table


def map_tables() -> None:
    map_user_table()
    map_account_table()
    map_category_table()
    map_transaction_table()
