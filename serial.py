"""Python serial number generator."""

class SerialGenerator():
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        '''Create  SerialGenerator'''
        self.initial = start
        self.current = start

    def generate(self):
        '''Returns value, starting at initial value first time it is called after initialization or reset, incrementing by one each time it is called.'''
        self.current = self.current+1
        return (self.current-1)

    def reset(self):
        '''Resets the generator to the initial number.'''
        self.current = self.initial





    
