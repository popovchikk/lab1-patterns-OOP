# decorator.py - это Паттерн Декоратор
# придумал задачу: кофе с разными добавками


# создам базовый класс
class Coffee:
    def get_cost(self):
        return 100
    
    def get_description(self):
        return "Кофе"


# делаю декоратор
class CoffeeDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def get_cost(self):
        return self.coffee.get_cost()
    
    def get_description(self):
        return self.coffee.get_description()


# делаю конкретные декораторы
class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 30
    
    def get_description(self):
        return self.coffee.get_description() + " + молоко"


class SugarDecorator(CoffeeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 10
    
    def get_description(self):
        return self.coffee.get_description() + " + сахар"


class CreamDecorator(CoffeeDecorator):
    def get_cost(self):
        return self.coffee.get_cost() + 40
    
    def get_description(self):
        return self.coffee.get_description() + " + сливки"


# нужен сценарий использования
if __name__ == "__main__":
    # я создаю простой кофе
    coffee = Coffee()
    print(f"{coffee.get_description()} = {coffee.get_cost()} руб.")
    
    # добавляю молоко
    coffee = MilkDecorator(coffee)
    print(f"{coffee.get_description()} = {coffee.get_cost()} руб.")
    
    # добавляю сахар
    coffee = SugarDecorator(coffee)
    print(f"{coffee.get_description()} = {coffee.get_cost()} руб.")
    
    # добавляю сливки
    coffee = CreamDecorator(coffee)
    print(f"{coffee.get_description()} = {coffee.get_cost()} руб.")