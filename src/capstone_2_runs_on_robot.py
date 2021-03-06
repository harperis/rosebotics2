"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Isaac Harper.
"""
# ------------------------------------------------------------------------------
# Done: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this Done.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 2. With your instructor, review the "big picture" of laptop-robot
# Done:    communication, per the comment in mqtt_sender.py.
# Done:    Once you understand the "big picture", delete this Done.
# ------------------------------------------------------------------------------

import rosebotics_even_newer as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # Done: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this Done.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # Done: 4. Add code that constructs a   com.MqttClient   that will
    # Done:    be used to receive commands sent by the laptop.
    # Done:    Connect it to this robot.  Test.  When OK, delete this Done.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    # --------------------------------------------------------------------------
    # Done: 5. Add a class for your "delegate" object that will handle messages
    # Done:    sent from the laptop.  Construct an instance of the class and
    # Done:    pass it to the MqttClient constructor above.  Augment the class
    # Done:    as needed for that, and also to handle the go_forward message.
    # Done:    Test by PRINTING, then with robot.  When OK, delete this Done.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Done: 6. With your instructor, discuss why the following WHILE loop,
    # Done:    that appears to do nothing, is necessary.
    # Done:    When you understand this, delete this Done.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # Done: 7. Add code that makes the robot beep if the top-red button
        # Done:    on the Beacon is pressed.  Add code that makes the robot
        # Done:    speak "Hello. How are you?" if the top-blue button on the
        # Done:    Beacon is pressed.  Test.  When done, delete this Done.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            print("Beeping:")
            ev3.Sound.beep().wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            print("Speaking:")
            ev3.Sound.speak("Hello. How are you?").wait()


class RemoteControlEtc(object):
    """
    Stores a Robot.
      :type robot: rb.Snatch3rRobot
    """
    def __init__(self, robot):
        self.robot = robot

    def high_five(self):
        self.robot.drive_system.start_moving(40, 40)
        while True:
            inches = self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
            if inches < 70:
                self.robot.drive_system.stop_moving()
                print('Speaking')
                ev3.Sound.set_volume(75)
                ev3.Sound.speak('High Five Bro?').wait()
                break

    def too_slow(self):
        while True:
            inches = self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches()
            if inches < 40:
                speed = -100
                self.robot.drive_system.move_for_seconds(1, speed, speed)
                print('Speaking')
                ev3.Sound.set_volume(75)
                ev3.Sound.speak('Ha ha, Too Slow Bro!').wait()
                break

    def stop_moving(self, speed_string):
        speed = int(speed_string)
        print('Robot should stop moving.')
        self.robot.drive_system.start_moving(speed, speed)


main()

