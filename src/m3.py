"""
  Capstone Project.  Code written by Isaac Harper.
  Fall term, 2018-2019.
"""

from ev3dev import ev3
from enum import Enum
import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    beep_when_sees_hand()


def beep_when_sees_hand():
    robot = rb.Snatch3rRobot()
    while True:
        inches = robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
        if inches < 15:
            print("Beeping:")
            ev3.Sound.beep().wait()


main()
