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
    robot.color_sensor.wait_until_color_is(color)
    print('True')


main()
