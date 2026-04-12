# message_bus.py - это Паттерн Шина сообщений
# придумал задачу: обмен сообщениями между компонентами

# суть: обмен событиями через центр, отправители и получатели не знают друг друга
# Пример: заказ создан → шина уведомляет подписчиков (отправить email, sms, аналитика)
# +: компоненты не зависят друг от друга, легко добавить нового подписчика


# создам шину сообщений
class MessageBus:
    def __init__(self):
        self.subscribers = {}
    
    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)
        print(f"Подписка на событие: {event_type}")
    
    def unsubscribe(self, event_type, callback):
        if event_type in self.subscribers:
            self.subscribers[event_type].remove(callback)
    
    def publish(self, event_type, data):
        print(f"\nПубликация события: {event_type}")
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(data)


# делаю подписчиков
class EmailService:
    def on_order_created(self, data):
        print(f"[Email] Отправка письма о заказе #{data['order_id']}")
    
    def on_order_shipped(self, data):
        print(f"[Email] Отправка письма о доставке #{data['order_id']}")


class SMSService:
    def on_order_created(self, data):
        print(f"[SMS] Отправка СМС о заказе #{data['order_id']}")


class AnalyticsService:
    def on_order_created(self, data):
        print(f"[Analytics] Логирование заказа #{data['order_id']}")
    
    def on_order_shipped(self, data):
        print(f"[Analytics] Логирование доставки #{data['order_id']}")


# нужен сценарий использования
if __name__ == "__main__":
    # я создаю шину
    bus = MessageBus()
    
    # создаю сервисы
    email = EmailService()
    sms = SMSService()
    analytics = AnalyticsService()
    
    # подписываю сервисы на события
    bus.subscribe("order_created", email.on_order_created)
    bus.subscribe("order_created", sms.on_order_created)
    bus.subscribe("order_created", analytics.on_order_created)
    bus.subscribe("order_shipped", email.on_order_shipped)
    bus.subscribe("order_shipped", analytics.on_order_shipped)
    
    # публикую события
    bus.publish("order_created", {"order_id": 1001})
    bus.publish("order_shipped", {"order_id": 1001})