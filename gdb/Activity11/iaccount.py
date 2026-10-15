from abc import ABC, abstractmethod

class IAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass