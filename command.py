# command.py - это Паттерн Команда
# придумал задачу: пульт управления умным домом

# суть: запрос инкапсулируется как объект с методами execute() и undo()

# execute() - выполняет команду (делает действие)
# undo() - отменяет команду

# +: можно отменять операции (undo), выполнять отложенно или в очереди



# создам команду
class Command:
    def execute(self):
        pass
    
    def undo(self):
        pass


# делаю получателя - Лампочка
class Light:
    def on(self):
        print("Свет включен")
    
    def off(self):
        print("Свет выключен")


# делаю получателя - Телевизор
class TV:
    def on(self):
        print("ТВ включен")
    
    def off(self):
        print("ТВ выключен")


# делаю конкретные команды
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
        self.was_on = False
    
    def execute(self):
        self.was_on = True
        self.light.on()
    
    def undo(self):
        if self.was_on:
            self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()


class TVOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv
    
    def execute(self):
        self.tv.on()
    
    def undo(self):
        self.tv.off()


# создаю пульт
class RemoteControl:
    def __init__(self):
        self.commands = []
        self.history = []
    
    def add_command(self, command):
        self.commands.append(command)
    
    def press_button(self, index):
        if index < len(self.commands):
            self.commands[index].execute()
            self.history.append(self.commands[index])
    
    def undo_last(self):
        if len(self.history) > 0:
            self.history.pop().undo()


# нужен сценарий использования
if __name__ == "__main__":
    # я создаю устройства
    light = Light()
    tv = TV()
    
    # создаю команды
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    tv_on = TVOnCommand(tv)
    
    # настраиваю пульт
    remote = RemoteControl()
    remote.add_command(light_on)
    remote.add_command(light_off)
    remote.add_command(tv_on)
    
    # использую пульт
    remote.press_button(0)  # включить свет
    remote.press_button(2)  # включить ТВ
    remote.undo_last()      # отменить последнее