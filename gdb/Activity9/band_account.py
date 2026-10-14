from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    @abstractmethod
    def calculate_interest(self) -> float:
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        pass

    def display_account_info(self) -> None:
        print(f"Account Number: {self._account_number}")
        print(f"Account Type: {self.get_account_type()}")
        print(f"Balance: Rs {self._balance}")
