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
        return f'{super().__str__()!r}'

    def action(self, pages = None):
        if not self.connected:
            print('Your printer is not connected!')
        
        self.remaining_pages -= pages
        print(f'{self.name} is printing {self.capacity}.. ({self.remaining_pages} pages remaining)\n')

class Scanner(Device):
    def __init__(self, name, connected_by):
        super().__init__(name, connected_by)
    
    def __str__(self):
        return f'{super().__str__()!r}'

    def action(self):
        if not self.connected:
            print('Your scanner is not connected!')
        
        print(f'Scanning the document..\n')


if __name__ == "__main__":

    devices = {
        'printer': [Printer('Printer 1', 'USB', 500), Printer('Printer 2', 'WIFI', 1500)],
        'scanner': [Scanner('Scanner 1', 'USB'), Scanner('Scanner 2', 'WIFI')]
    }

    for device in devices['printer']:
        print(device)
        device.action(5)

    for device in devices['scanner']:
        print(device)
        device.action()