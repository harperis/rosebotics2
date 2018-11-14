"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Isaac Harper.
"""
# ------------------------------------------------------------------------------
# Done: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this Done.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 2. With your instructor, discuss the "big picture" of laptop-robot
# Done:    communication:
# Done:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# Done:        user presses a button intended to make something happen on the
# Done:        ROBOT, the LAPTOP program sends a message to its MQTT client
# Done:        indicating what it wants the ROBOT to do, and the MQTT client
# Done:        SENDS that message TO a program running on the ROBOT.
# Done:
# Done:      - Another program runs on the ROBOT. It stays in a loop, responding
# Done:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# Done:        It also, in the background, listens for messages TO the ROBOT
# Done:        FROM the program running on the LAPTOP.  When it hears such a
# Done:        message, it calls the method in the DELAGATE object's class
# Done:        that the message indicates, sending arguments per the message.
# Done:
# Done:  Once you understand the "big picture", delete this Done (if you wish).
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 99
# Done:    to use YOUR robot's number instead of 99.
# Done:    Commit and push the change, then other team members Update Project.
# Done:    Then delete this Done.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Done: 4. Run this module.
# Done:    Study its code until you understand how the GUI is set up.
# Done:    Then delete this Done.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)

    root.mainloop()
    # --------------------------------------------------------------------------
    # Done: 5. Add code above that constructs a   com.MqttClient   that will
    # Done:    be used to send commands to the robot.  Connect it to this pc.
    # Done:    Test.  When OK, delete this Done.
    # --------------------------------------------------------------------------


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=30)
    frame.grid()

    high_five_button = ttk.Button(frame, text="Want a High Five")
    yes_bro_button = ttk.Button(frame, text="Yeah Bro")
    stop_moving_button = ttk.Button(frame, text="Stop moving")

    high_five_button.grid()
    yes_bro_button.grid()
    stop_moving_button.grid()

    high_five_button['command'] = \
        lambda: high_five(mqtt_client)

    yes_bro_button['command'] = \
        lambda: yeah_bro(mqtt_client)

    stop_moving_button['command'] = \
        lambda: stop_moving(mqtt_client)


def high_five(mqtt_client):
    mqtt_client.send_message('high_five')
    print("Sending 'high_five' to a robot")


def yeah_bro(mqtt_client):
    mqtt_client.send_message('too_slow')
    print("Sending 'too_slow' to a robot")


def stop_moving(mqtt_client):
    speed = 0
    mqtt_client.send_message('stop_moving', [speed])
    print("Sending 'stop_moving' to a robot", speed)

    # --------------------------------------------------------------------------
    # Done: 6. This function needs the entry box in which the user enters
    # Done:    the speed at which the robot should move.  Make the 2 changes
    # Done:    necessary for the entry_box constructed in  setup_gui
    # Done:    to make its way to this function.  When done, delete this Done.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Done: 7. For this function to tell the robot what to do, it needs
    # Done:    the MQTT client constructed in main.  Make the 4 changes
    # Done:    necessary for that object to make its way to this function.
    # Done:    When done, delete this Done.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Done: 8. Add the single line of code needed to get the string that is
    # Done:    currently in the entry box.
    # Done:
    # Done:    Then add the single line of code needed to "call" a method on the
    # :    LISTENER that runs on the ROBOT, where that LISTENER is the
    # :    LISTENER that runs on the ROBOT, where that LISTENER is the
    # Done:    "delegate" object that is constructed when the ROBOT's code
    # Done:    runs on the ROBOT.  Send to the delegate the speed to use
    # Done:    plus a method name that you will implement in the DELEGATE's
    # Done:    class in the module that runs on the ROBOT.
    # Done:
    # Done:    Test by using a PRINT statement.  When done, delete this Dine.
    # --------------------------------------------------------------------------


main()
