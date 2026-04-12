# strategy.py - это Паттерн Стратегия
# придумал задачу: расчет скидки для покупателя разными способами

# суть паттерна: мы можем менять алгоритм расчета скидки во время выполнения программы
# не изменяя сам класс корзины покупок.

# +: можно легко добавлять новые виды скидок, не меняя существующий код.

from abc import ABC, abstractmethod


# создам интерфейс стратегии
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, price):
        pass


# делаю Стратегию 1: Без скидки
class NoDiscount(DiscountStrategy):
    def calculate(self, price):
        return price


# делаю Стратегию 2: Скидка 10%
class TenPercentDiscount(DiscountStrategy):
    def calculate(self, price):
        return price * 0.9


# делаю Стратегию 3: Скидка 20% для пенсионеров
class PensionerDiscount(DiscountStrategy):
    def calculate(self, price):
        return price * 0.8


# создаю контекст - корзина покупателя
class ShoppingCart:
    def __init__(self, strategy):
        self.strategy = strategy
        self.items = []
    
    def add_item(self, name, price):
        self.items.append((name, price))
    
    def get_total(self):
        total = sum([price for name, price in self.items])
        return self.strategy.calculate(total)


# нужен сценарий использования
if __name__ == "__main__":
    # я создаю корзину с обычной ценой
    cart = ShoppingCart(NoDiscount())
    cart.add_item("Молоко", 100)
    cart.add_item("Хлеб", 50)
    print(f"Без скидки: {cart.get_total()} руб.")
    
    # меняю стратегию на скидку 10%
    cart.strategy = TenPercentDiscount()
    print(f"Скидка 10%: {cart.get_total()} руб.")
    
    # меняю стратегию на скидку для пенсионеров
    cart.strategy = PensionerDiscount()
    print(f"Скидка пенсионерам: {cart.get_total()} руб.")