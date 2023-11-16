from ctypes.wintypes import LONG
from decimal import Decimal


class Account:
    user_account_id: LONG
    balance: Decimal

    def __init__(self,user_account_id,balance) -> None:
        self.user_account_id = user_account_id
        self.balance = balance

        def get_user_account_id(self):
            return self.user_account_id

        def get_balance(self):
            return self.balance
