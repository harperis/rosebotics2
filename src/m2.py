"""
  Capstone Project.  Code written by Isaac Harper and Russel Staple.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    follow_line(50)
    """ Runs YOUR specific part of the project """


def test_color(color):
    robot = rb.Snatch3rRobot()
    while True:
        robot.drive_system.start_moving()
        if robot.color_sensor.get_color() == color:
            break
    robot.drive_system.stop_moving()


def follow_line(speed):
    robot = rb.Snatch3rRobot()
    while True:
        while True:
            robot.drive_system.start_moving(speed, speed)
            if robot.color_sensor.get_reflected_intensity() > 10:
                break
        robot.drive_system.stop_moving()
        robot.drive_system.spin_in_place_degrees(20)
        if robot.color_sensor.get_color() == 7:
            break
    robot.drive_system.stop_moving()


main()
