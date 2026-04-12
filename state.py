# state.py - это Паттерн Состояние
# придумал задачу: статусы заказа в интернет-магазине

# объект меняет поведение в зависимости от внутреннего состояния
# +: логика переходов в самих состояниях, а не в куче if-else

from abc import ABC, abstractmethod


# создам базовое состояние
class OrderState(ABC):
    def next(self, order):
        pass
    
    def cancel(self, order):
        print("Заказ уже нельзя отменить")
    
    def get_status(self):
        return "Неизвестно"


# делаю Состояние 1: Новый заказ
class NewOrder(OrderState):
    def get_status(self):
        return "Новый"
    
    def next(self, order):
        print("Заказ подтвержден")
        order.state = ConfirmedOrder()
    
    def cancel(self, order):
        print("Заказ отменен")
        order.state = CancelledOrder()


# делаю Состояние 2: Подтвержден
class ConfirmedOrder(OrderState):
    def get_status(self):
        return "Подтвержден"
    
    def next(self, order):
        print("Заказ отправлен")
        order.state = ShippedOrder()
    
    def cancel(self, order):
        print("Заказ отменен")
        order.state = CancelledOrder()


# делаю Состояние 3: Отправлен
class ShippedOrder(OrderState):
    def get_status(self):
        return "Отправлен"
    
    def next(self, order):
        print("Заказ доставлен")
        order.state = DeliveredOrder()
    
    def cancel(self, order):
        print("Нельзя отменить доставляемый заказ")


# делаю Состояние 4: Доставлен
class DeliveredOrder(OrderState):
    def get_status(self):
        return "Доставлен"
    
    def next(self, order):
        print("Заказ уже доставлен")
    
    def cancel(self, order):
        print("Нельзя отменить доставленный заказ")


# делаю Состояние 5: Отменен
class CancelledOrder(OrderState):
    def get_status(self):
        return "Отменен"
    
    def next(self, order):
        print("Нельзя продолжить отмененный заказ")


# создаю контекст - Заказ
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.state = NewOrder()
    
    def next_status(self):
        self.state.next(self)
    
    def cancel(self):
        self.state.cancel(self)
    
    def get_status(self):
        return self.state.get_status()


# нужен сценарий использования
if __name__ == "__main__":
    # я создаю заказ
    order = Order(123)
    print(f"Статус: {order.get_status()}")
    
    order.next_status()
    print(f"Статус: {order.get_status()}")
    
    order.next_status()
    print(f"Статус: {order.get_status()}")
    
    order.next_status()
    print(f"Статус: {order.get_status()}")
