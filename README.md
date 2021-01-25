# bot_movement
This code tries to simulate a robot by having the following components:

In the bot folder:
## Body
located in body.py 
The Body class is responsible for being the interface to the robot and for keeping track of the robot x, y, psi coordinates in space. The Body is also responsible for information like current speed

## Encoder 
located in encoder.py
the Encoder class is responsible for simulating a motor and encoder. By making calls to set_power(power) the Body can simulate requesting motor movement. The Encoder also returns information such as current speed, distance traveled, etc.

## Brains
located in brains.py - the Brains class is responsible for path planning using information requested from the Body. 

## main.py
The main application and the entry point to the application
## bot_sprite.py 
Handles the sprite manipulation (drawing, calling on Body to update each tick) and isolates the pygame engine from the bot classes. 

The important functions in question at the moment are:
update_current_position in body.py line 83 which is responsible for the kinematics of the robot itself 
calculate_velocity in brains.py line 31 which is responsible for path planning
