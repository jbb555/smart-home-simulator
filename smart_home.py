class SmartDevice:
    '''A parent class that initializes names and status. Allows devices to be turned on, off and returns a string that shows the name of the device and whether it on or not.'''

    def __init__(self, name):
        '''Initializes the device with a given name and sets the status to False(off) by default'''
       
        self.name = name
        self.status = False


    def turn_on(self):
        '''Turns the device on by setting the status attribute to true'''
        self.status = True
            
    def turn_off(self):
        '''Turns the device off by setting the status attribute to False'''
        self.status = False
    
    def __str__(self):
        '''Returns a string representation of the device, showing the name and its current on/off status'''
        status_str = 'ON' if self.status else 'OFF'
        
        return f'{self.name}: {status_str}'

class Light(SmartDevice):
    '''A child class that is specfic to lights and can adjust the brightness of the room'''
    def __init__(self, name):
        '''initialzies the parent classes while adding brightness'''
        self.name = name
        self.status = False
        self.brightness = 100

    def adjust_brightness(self, level):
        '''Adjusts the brightness of the light. The brightness is only changed if the level is between 1 and 100 (inclusive) If the level is outside the range, the brightness remains unchanged.'''
        if 1 <= level <= 100:
            self.brightness = level

    def __str__(self):
        '''Returns a string representation of the light, showing the name, its current on/off status, and its brightness level.'''
        status_str = 'ON' if self.status else 'OFF'
        return f'{self.name} Light: {status_str}, Brightness: {status_str}'

class Thermostat(SmartDevice):
    '''A child class that allows the change of temperature in a room'''

    def __init__(self, name):
        '''initializes the parent class structure and adds the default value for temperature'''
        self.name = name
        self.status = False
        self.temperature = 65.0

    def adjust_temperature(self, temp):
        '''Adjusts the temperature of the thermostat. It uses the private helper method to ensure the tmeperature is within a reasonable range. If the temperature is within this range, it updates the temperature attrivute. If not temperature remains unchanged.'''
        if self._check_temperature_limits(temp):
            self.temperature = temp

    def __str__(self): 
        '''Returns a string representation of the thermostat, showing the name, its current on/off status, and the current temperature.'''
        status_str = 'ON' if self.status else 'OFF'
        return f'{self.name} Thermostat:{status_str}, Temperature: {self.temperature}' 

    def _check_temperature_limits(self, temp):
        '''Checks if the given temperature is within the acceptable range. This is a private method used internally to validate temperature adjustments'''
        return 55.0 <= temp <= 80.0
    
class Speaker(SmartDevice):
    '''Changing the volume of a speaker increasing it or decreasing it'''
    def __init__(self, name):
        ''''initializes the volume and attributes from the parent class'''
        self.name = name
        self.status = False
        self.volume = 3
    
    def increase_volume(self):
        '''Increases the volume by 1, with a maximum volume of 10'''
        if self.volume < 10:
            self.volume += 1

    def decrease_volume(self):
        '''Decrease the volume by 1, with a minimum volume of 1'''
        if self.volume > 1:
            self.volume -= 1


    def __str__(self):
        '''Returns a string represenatino of the pseaker, showing the name, its current on/off status, and its volume setting'''
        status_str = 'ON' if self.status else 'OFF'
        return f'{self.name} Speaker: {status_str}, Volume: {self.volume}'
    
class SmartHome:
        
        def __init__(self):
            '''initializes empty list of devices'''
            self.devices = []

        def __add__(self, other):
            '''__add__ overloads the + operator to allow devices to be added to the SmartHome instance. This method appends the device to the devices list in the smarthome'''
            self.devices.append(other)
            return self
        
        def turn_off_all(self):
            '''Turns off all devices for the smart home instance.'''
            for device in self.devices:
                device.turn_off()
        def __str__(self):
            '''Returns a string listing the name and status of each device in the SmartHome instance.'''
            return '\n'.join(str(device) for device in self.devices)
                



