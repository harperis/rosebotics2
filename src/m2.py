"""
  Capstone Project.  Code written by Isaac Harper.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    test_color(1)
    """ Runs YOUR specific part of the project """


def test_color(color):
    robot = rb.Snatch3rRobot()
    if not robot.color_sensor.get_color() == color:
        while True:
            robot.drive_system.start_moving()
            print('False')
            if robot.color_sensor.get_color() == color:
                break
            robot.drive_system.stop_moving()
            print('True')









main()
