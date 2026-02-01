from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict

# Ein Dekorator für professionelles Logging
def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"LOG [{datetime.now().strftime('%H:%M:%S')}]: {func.__name__} ausgeführt.")
        return result
    return wrapper

class Product(ABC):
    """Abstrakte Basisklasse (Interface)"""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Drink(Product):
    pass

class Food(Product):
    pass

class Table:
    def __init__(self, number: int):
        self._number = number
        self._orders: List[Product] = []

    @property
    def total_sum(self) -> float:
        """Berechnet die Summe dynamisch (Property)."""
        return sum(item.price for item in self._orders)

    @log_action
    def add_order(self, item: Product):
        self._orders.append(item)

    def reset(self):
        self._orders.clear()

    @property
    def is_occupied(self) -> bool:
        return len(self._orders) > 0
