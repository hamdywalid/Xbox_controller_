##https://www.youtube.com/watch?v=F5Bq7HVJkX0
##https://github.com/kevinmcaleer/xbox_controller/blob/main/xbox_controller.py

# Remote control Explora
# Kevin McAleer
# 17 March 2022

# We use Pygame to access the Xbox One Controller
import pygame
import explorerhat
from time import sleep
from pygame.constants import JOYBUTTONDOWN
pygame.init()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

# Print out the name of the controller
print(pygame.joystick.Joystick(0).get_name())

# Xbox Joystick Axis:
# Axis 0 up down, down value is -1, up value is 1
# Axis 1 Left, Right, Left value is: -1, right value is 1
# center is always 0

# Main Loop
while True or KeyboardInterrupt:

    # Check for joystick events
    for event in pygame.event.get():
        if event.type ==JOYBUTTONDOWN:
            if event.button == 0:
                print("button 0 down")
            if event.button == 1:
                print("button 1 down")
            if event.button == 2:
                print("button 2 down")
            if event.button == 3:
                print("button 4 down")
            if event.button == 5:
                print("button 5 down")
            if event.button == 6:
                print("button 6 down")
            if event.button == 7:
                print("button 7 down")
            if event.button == 8:
                print("button 8 down")
        if event.type == pygame.JOYAXISMOTION:
            if event.axis < 2: # Left stick
                if event.axis == 0: # left/right
                    if event.value < -0.5:
                        print("left")
                        motor_speed = event.value * -1
                        print(f"motor_speed: {motor_speed}")
                        explorerhat.motor.one.backwards()
                        explorerhat.motor.two.forwards()
                        sleep(0.01)
                        explorerhat.motor.one.stop()
                        explorerhat.motor.two.stop()
                    if event.value > 0.5:
                        print("right")                        
                        explorerhat.motor.one.forwards()
                        explorerhat.motor.two.backwards()
                        sleep(0.01)
                        explorerhat.motor.one.stop()
                        explorerhat.motor.two.stop()
                if event.axis == 1: # up/down
                    if event.value < -0.5:
                        print("up")
                        explorerhat.motor.one.forwards()
                        explorerhat.motor.two.forwards()
                        sleep(0.01)
                        explorerhat.motor.one.stop()
                        explorerhat.motor.two.stop()

                    if event.value > 0.5:
                        print("down")
                        explorerhat.motor.one.backwards()
                        explorerhat.motor.two.backwards()
                        sleep(0.01)
                        explorerhat.motor.one.stop()
                        explorerhat.motor.two.stop()