# adapter.py - это Паттерн Адаптер
# придумал задачу: подключение старой системы оплаты к новому интерфейсу


# создам старую систему (нельзя менять)
class OldPaymentSystem:
    def make_payment(self, amount, currency):
        print(f"[Старая система] Платеж {amount} {currency}")
        return True
    
    def get_balance(self, user_id):
        print(f"[Старая система] Баланс пользователя {user_id}")
        return 1000


# нужен новый интерфейс
class PaymentInterface:
    def pay(self, amount):
        pass
    
    def check_balance(self):
        pass


# делаю адаптер
class PaymentAdapter(PaymentInterface):
    def __init__(self, old_system):
        self.old_system = old_system
    
    def pay(self, amount):
        # адаптирую вызов
        return self.old_system.make_payment(amount, "RUB")
    
    def check_balance(self):
        # адаптирую вызов
        return self.old_system.get_balance(1)


# нужен сценарий использования
if __name__ == "__main__":
    # я создаю старую систему
    old_sys = OldPaymentSystem()
    
    # создаю адаптер
    adapter = PaymentAdapter(old_sys)
    
    # работаю через новый интерфейс
    adapter.pay(500)
    adapter.check_balance()