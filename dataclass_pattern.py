# dataclass_pattern.py - это Паттерн Dataclass
# придумал задачу: свой базовый класс для моделей данных

# суть - упрощение создания классов для хранения данных

# to_dict() - преобразует объект в словарь (для JSON или сохранения в БД)
# update() - обновляет поля объекта новыми значениями
# __str__() - возвращает красивое строковое представление объекта (для print)


# +: меньше шаблонного кода, быстрое создание моделей без ручного написания конструкторов


# создам базовый класс для моделей
class BaseModel:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        attrs = []
        for key, value in self.__dict__.items():
            attrs.append(f"{key}={value}")
        return f"{self.__class__.__name__}({', '.join(attrs)})"
    
    def to_dict(self):
        return self.__dict__.copy()
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


# делаю конкретные модели
class User(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Product(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def get_price_with_tax(self):
        return self.price * 1.2


class Order(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = []
    
    def add_item(self, product):
        self.items.append(product)
    
    def get_total(self):
        return sum([item.price for item in self.items])


# нужен сценарий использования
if __name__ == "__main__":
    # я создаю пользователя
    user = User(id=1, first_name="Иван", last_name="Петров", email="ivan@test.ru")
    print(user)
    print(f"ФИО: {user.get_full_name()}")
    
    # создаю товары
    product1 = Product(id=1, name="Телефон", price=50000)
    product2 = Product(id=2, name="Чехол", price=1000)
    
    print(product1)
    print(f"Цена с налогом: {product1.get_price_with_tax()}")
    
    # создаю заказ
    order = Order(id=100, user_id=1)
    order.add_item(product1)
    order.add_item(product2)
    
    print(order)
    print(f"Итого: {order.get_total()}")
    
    # обновляю данные
    user.update(email="new@test.ru")
    print(user)
    
    # конвертирую в словарь
    print(user.to_dict())