"""
  Capstone Project.  Code for testing basics.
  Author:  David Mutchler, based on work by Dave Fisher and others.
  READ and RUN this module but ** DO NOT MODIFY IT. **
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
#    run_test_drive_system()
#   run_test_touch_sensor()
    run_test_color_sensor()


def run_test_drive_system():
    """ Tests the  drive_system  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()
    print('start')
    robot.drive_system.spin_in_place_degrees(360)
    print('end')

def run_test_touch_sensor():
    """ Tests the  touch_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  touch_sensor  of the robot.")
    print("Repeatedly press and release the touch sensor.")
    print("Press Control-C when you are ready to stop testing.")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),
              "Touch sensor value is: ", robot.touch_sensor.get_value())
        time.sleep(0.5)
        count = count + 1


def run_test_color_sensor():
    """ Tests the  color_sensor  of the Snatch3rRobot. """
    robot = rb.Snatch3rRobot()
    print()
    print("Testing the  color_sensor  of the robot.")
    print("Repeatedly move the robot to different surfaces.")
    print("Press Control-C when you are ready to stop testing.")
    time.sleep(1)
    count = 1
    while True:
        print("{:4}.".format(count),
              "Color sensor value/color/intensity is: ",
              "{:3} {:3} {:3}".format(robot.color_sensor.get_value()[0],
                                      robot.color_sensor.get_value()[1],
                                      robot.color_sensor.get_value()[2]),
              "{:4}".format(robot.color_sensor.get_color()),
              "{:4}".format(robot.color_sensor.get_reflected_intensity()))
        time.sleep(0.5)
        count = count + 1



main()
