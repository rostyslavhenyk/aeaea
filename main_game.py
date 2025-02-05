# Your new file!
from microbit import *
from bme688 import *
from OLED import *
import time
import music
import radio

userID = "D"
init_display()
radio.config(queue=5, group = 14, channel=56, power=4)
radio.on()

"""
def testing(action):
    CO2 = calc_air_quality()[2]
    if action == "warm me up":
        testing = True
        while testing:
            read_data_registers()
            temp = calc_temperature()
            print(temperature())
            print(temp)
            sleep(500)
    if action == "blow on me":
        testing = True
        while testing:
            read_data_registers()
            new_CO2 = calc_air_quality()[2]
            print(CO2)
            sleep(500)
    if action == "hide me":
        testing = True
        while testing:
            print(display.read_light_level())
            sleep(500)
"""

def check_action(action):
    gestures = ["tilt left", "tilt right", "shake", "face up", "face down"]
    buttons = ["button a", "button b", "touch me"]
    actions = [button_a.is_pressed(), button_b.is_pressed(), pin_logo.is_touched()]

    for _ in range(10):
        if action in gestures:
            gestures.remove(action)
            for i in range(len(gestures)):
                if accelerometer.current_gesture() == gestures[i]:
                    return "fail"
                elif accelerometer.current_gesture() == action:
                    return "pass"
        else:
            if action in buttons:  # Check if action is in buttons before indexing
                buttons_index = buttons.index(action)
                if actions[buttons_index]:
                    return "pass"
                else:
                    for i in range(len(actions)):
                        if i != buttons_index and actions[i]:
                            return "fail"
        sleep(100)
"""
def accelerator_tester(action):
    if check_action(action) == "pass":
        #music.play(music.BA_DING)
        display.show(Image.YES)
        return "1"
    elif check_action(action) == "fail":
        display.show(Image.NO)
        #music.play(music.FUNERAL)
        return "0"
    else:
        return None
"""
def game(round, action, simon):     ####
    show("Round: " + str(round), 0)

    if simon == "1":                ####
        show("Simon Says "+action, 1)
    else:
        show(action, 1)

    sleep(500)
    running = True
    success = "0"
    counter = 5

    while running:
        if counter <= 0:
            if simon == "1":    ####
                success = "0"
            else:
                success = "1"
            break
        display.show(str(counter),wait=False)

        if action.lower() == "shake":
            result = check_action(action)
            if result == "pass":
                display.show(Image.YES)
                success = "1"
                running = False
            elif result == "fail":
                display.show(Image.NO)
                success = "0"
                running = False
            else:
                counter -= 1


        elif action.lower() == "touch me":
            result = check_action(action)
            if result == "pass":
                display.show(Image.YES)
                success = "1"
                running = False
            elif result == "fail":
                display.show(Image.NO)
                success = "0"
                running = False
            else:
                counter -= 1

        elif action.lower() == "face up":
            result = check_action(action)
            if result == "pass":
                display.show(Image.YES)
                success = "1"
                running = False
            elif result == "fail":
                display.show(Image.NO)
                success = "0"
                running = False
            else:
                counter -= 1

        elif action.lower() == "face down":
            result = check_action(action)
            if result == "pass":
                display.show(Image.YES)
                success = "1"
                running = False
            elif result == "fail":
                display.show(Image.NO)
                success = "0"
                running = False
            else:
                counter -= 1

        elif action.lower() == "tilt left":
            result = check_action(action)
            if result == "pass":
                display.show(Image.YES)
                success = "1"
                running = False
            elif result == "fail":
                display.show(Image.NO)
                success = "0"
                running = False
            else:
                counter -= 1

        elif action.lower() == "tilt right":
            result = check_action(action)
            if result == "pass":
                display.show(Image.YES)
                success = "1"
                running = False
            elif result == "fail":
                display.show(Image.NO)
                success = "0"
                running = False
            else:
                counter -= 1

        elif action.lower() == "button a":
            result = check_action(action)
            if result == "pass":
                display.show(Image.YES)
                success = "1"
                running = False
            elif result == "fail":
                display.show(Image.NO)
                success = "0"
                running = False
            else:
                counter -= 1

        elif action.lower() == "button b":
            result = check_action(action)
            if result == "pass":
                display.show(Image.YES)
                success = "1"
                running = False
            elif result == "fail":
                display.show(Image.NO)
                success = "0"
                running = False
            else:
                counter -= 1

    if counter > 0 and simon == "0":        ####
        success = "0"

    radio.send(userID+success)




