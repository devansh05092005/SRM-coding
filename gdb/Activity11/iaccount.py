from abc import ABC, abstractmethod
class IAccount(ABC):

    @property
    @abstractmethod
    def account_number(self):
        pass

    @property
    @abstractmethod
    def account_holder(self):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass