# factory.py - это Паттерн Фабрика
# придумал задачу: создание разных типов уведомлений

# Factory (Фабрика) - создание объектов через специальный класс-фабрику
# пример: уведомления (SMS, Email, Push) создаются через NotificationFactory
# +: код не знает, как создаются объекты. Новый тип - меняем только фабрику

from abc import ABC, abstractmethod


# создам базовый класс уведомления
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


# делаю SMS уведомление
class SMSNotification(Notification):
    def send(self, message):
        print(f"[SMS] Отправляем: {message}")


# делаю Email уведомление
class EmailNotification(Notification):
    def send(self, message):
        print(f"[Email] Отправляем: {message}")


# делаю Push уведомление
class PushNotification(Notification):
    def send(self, message):
        print(f"[Push] Отправляем: {message}")


# создаю фабрику
class NotificationFactory:
    @staticmethod
    def create(type):
        if type == "sms":
            return SMSNotification()
        elif type == "email":
            return EmailNotification()
        elif type == "push":
            return PushNotification()
        else:
            print("Неизвестный тип уведомления")
            return None


# нужен сценарий использования
if __name__ == "__main__":
    # я создаю уведомления через фабрику
    sms = NotificationFactory.create("sms")
    sms.send("Ваш заказ подтвержден")
    
    email = NotificationFactory.create("email")
    email.send("Добро пожаловать!")
    
    push = NotificationFactory.create("push")
    push.send("Новое сообщение")