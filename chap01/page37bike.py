#!/usr/bin/python
# page37bike.py
# let's define the class Bike, and lets use "thebike" instead of "self", just to be sure that "self" is just a choice of word
class Bike():
    def __init__(thebike, colour, frame_material):
        thebike.bcolour = colour    # I avoid on purpose to use: thebike.colour = colour
        thebike.bframe_material = frame_material
    def brake(thebike):
        print("Braking!I am the ", thebike.bcolour)

# let's create a couple of instances
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')
# let's inspect the objects we have, instances of the Bike class.
print(red_bike.bcolour)          # prints: Red
print(red_bike.bframe_material)  # prints: Carbon fiber
print(blue_bike.bcolour)         # prints: Blue
print(blue_bike.bframe_material) # prints: Steel
# let's brake!
red_bike.brake()                # prints: Braking! I am the Red
