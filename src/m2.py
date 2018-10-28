"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    drive_until_color(1)
    """ Runs YOUR specific part of the project """


def drive_until_color(color):
    print('start')
    robot = rb.Snatch3rRobot()
    if not robot.color_sensor.get_color() == color:
        while True:
            robot.drive_system.go_straight_inches(1)
            break
        robot.drive_system.stop_moving()
    print('end')









main()
