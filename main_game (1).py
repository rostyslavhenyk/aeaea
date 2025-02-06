from microbit import *
from bme688 import *
from OLED import *
import music
import radio
import random

userID = "A"
init_display()
init_sensor()
init_gas_sensor()
radio.config(queue=5, group = 14, channel=56, power=4)
radio.on()
def check_action(action):
    gestures = ["left", "right", "shake", "face up", "face down"]
    buttons = ["button a", "button b", "touch me"]
    actions = [button_a.is_pressed(), button_b.is_pressed(), pin_logo.is_touched()]

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
    """ if random.randint(0,100) < 80:
        simonSays = "Simon says "
    else:
        simonSays = """
def game(round, action, simon):
    show("Round: " + str(round), 0)
    sleep(200)
    if simon == "1":  
        show("Simon Says "+action, 1)
    else:
        show(action, 1)

    running = True
    success = "0"
    counter = 5
    calcedTemp = calc_temperature()
    CO2 = calc_air_quality()[2]

    while running:
        if counter <= 0:
            if simon == "1":   
                success = "0"
            else:
                success = "1"
            break
        display.show(str(counter),wait=False)

        for _ in range(10):
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
                    
            elif action.lower() == "warm me up":
                read_data_registers()
                tempCount = calc_temperature()
                show("{} C".format(tempCount), 6)
                sleep(50)
                if tempCount> calcedTemp+1:
                    display.show(Image.YES)
                    success = "1"
                    running = False
            elif action.lower() == "blow on me":
                read_data_registers()
                currentCO2 = calc_air_quality()[2]
                show("{}".format(currentCO2)+"ppm", 6)
                sleep(50)
                if CO2> currentCO2-15:
                    display.show(Image.YES)
                    success = "1"
                    running = False
            elif action.lower() == "shout":
                microphone.set_threshold(SoundEvent.LOUD, 180)
                microphone.set_threshold(SoundEvent.QUIET, 100)
                show(str(microphone.sound_level()),6)
                sleep(50)
                if microphone.current_event() == SoundEvent.LOUD:
                    display.show(Image.YES)
                    success = "1"
                    running = False
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
    
            elif action.lower() == "left":
                result = check_action(action)
                if result == "pass":
                    display.show(Image.YES)
                    success = "1"
                    running = False
                elif result == "fail":
                    display.show(Image.NO)
                    success = "0"
                    running = False
    
            elif action.lower() == "right":
                result = check_action(action)
                if result == "pass":
                    display.show(Image.YES)
                    success = "1"
                    running = False
                elif result == "fail":
                    display.show(Image.NO)
                    success = "0"
                    running = False
    
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
            sleep(100)
        counter -= 1
        
    show("",6)
    if counter > 0 and simon == "0":        ####
        success = "0"
    radio.send(userID+success)
    if counter == 0:
        display.show(Image.NO)
    



