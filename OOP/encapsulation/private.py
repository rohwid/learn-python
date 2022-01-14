# NOTES:
# _var_name  : protected (can inherits or access from child class)
#              See: _connected
# __var_name : private (can't be inherit or access from child class, except uses super() method)
#              See: __connected_by, __capacity and __remaining_pages varaible

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.__connected_by = connected_by
        self._connected = True

    def __str__(self):
        if not self._connected:
            return f'Device {self.name!r} is disconnected\n'    
        return f'Device {self.name!r} is connected by {self.__connected_by}'

    def disconnected(self):
        self._connected = False

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.__capacity = capacity
        self.__remaining_pages = capacity
    
    def __str__(self):
        if not self._connected:
            return f'Device {self.name!r} is disconnected'  
        return f'{super().__str__()} ({self.__remaining_pages} pages remaining)'

    def print(self, pages):
        if not self._connected:
            print('Your printer is not connected!')
        
        print(f'Print {pages} remaining pages..')
        self.__remaining_pages -= pages
        print(f'{self.__remaining_pages} of {self.__capacity} are available.')


printer1 = Device('Printer 1', 'USB')
print(printer1)
printer1.disconnected()
print(printer1)


printer2 = Printer('Printer 2', 'WIFI', 500)
print(printer2)
printer2.print(20)
printer2.disconnected()
print(printer2)
