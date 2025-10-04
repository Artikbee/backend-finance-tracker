from decimal import Decimal

from pydantic import BaseModel

from domains.transaction.enums import TransactionType


class CreateTransactionSchema(BaseModel):
    category_id: int
    transaction_type: TransactionType
    amount: Decimal
    description: str
