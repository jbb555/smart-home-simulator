# Smart Home Device System 🏠💡

A Python-based simulation of a smart home environment. This program models smart devices (Lights, Speakers, Thermostats) using object-oriented programming principles.

## Features
- Power on/off control for all smart devices
- Adjustable brightness for smart lights
- Temperature control with validation for thermostats
- Volume control for speakers
- SmartHome manager class with operator overloading to add devices
- Clean object-oriented structure with inheritance and method overriding

## Technologies
- Python 3.x
- OOP (Inheritance, Encapsulation, Polymorphism)
- Operator Overloading

## Example

```python
from smarthome import Light, Thermostat, Speaker, SmartHome

# Create devices
lamp = Light("Bedroom")
ac = Thermostat("Living Room")
speaker = Speaker("Kitchen")

# Add devices to SmartHome
my_home = SmartHome()
my_home = my_home + lamp + ac + speaker

# Turn on devices
lamp.turn_on()
ac.turn_on()
ac.adjust_temperature(72)
speaker.turn_on()
speaker.increase_volume()

# Show current home status
print(my_home)
