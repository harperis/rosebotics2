"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    polygon(5, 10)

# Interior angle formula: (n-2)*180//n


def polygon(n, side_length):
    print('start')
    robot = rb.Snatch3rRobot()
    for k in range(n):
        robot.drive_system.go_straight_inches(side_length)
        robot.drive_system.spin_in_place_degrees(180-((n-2)*180//n))
    print('end')


main()
