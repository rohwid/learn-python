class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f'Device {self.name!r} is connected by {self.connected_by}'

    def disconnected(self):
        self.connected = False
        print('Disconnected')

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity
    
    def __str__(self):
        return f'{super().__str__()} ({self.remaining_pages} pages remaining)'

    def print(self, pages):
        if not self.connected_by:
            print('Your printer is not connected!')
        
        print(f'Print {pages} remaining')
        self.remaining_pages -= pages

printer1 = Device('Printer 1', 'USB')
print(printer1)

printer1.disconnected()

printer2 = Printer('Printer 2', 'WIFI', 500)
printer2.print(20)

print(printer2)

printer2.disconnected()