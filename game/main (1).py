from microbit import *
from bme688 import *
from OLED import *
from main_game import *
import radio
games = ["shake", "left", "right", "button b", "button a", "face up", "face down", "warm me up", "touch me", "shout", "blow on me"]
radio.config(queue=5, group = 14, channel=56, power=4)
radio.on()
init_sensor()
init_gas_sensor()
init_display()
players = ["A1","A0","B0","B1","C0","C1","D1","D0"]
userID = "C"
while True:
    incoming = radio.receive()
    if incoming == "are you ready":
        show("are you ready",2)
        show("press b",3)
        while not button_b.is_pressed():
            pass
        show("",2)
        show("",3)
        radio.send("userC")
        display.show("C", wait=False)
    if incoming == "send the game":
        round = 1
        while round <= 10:
            roundInfo = None
            while not roundInfo:
                roundInfo = radio.receive()
            if roundInfo and roundInfo.startswith("type"):
                if len(roundInfo[4:]) == 2:
                    gameForRound = int(roundInfo[4])
                    simonSays = roundInfo[5]
                elif len(roundInfo[4:]) == 3:
                    gameForRound = int(roundInfo[4]+roundInfo[5])
                    simonSays = roundInfo[6]
                game(round, games[gameForRound], simonSays)
                round += 1
            elif roundInfo and roundInfo in players:
                pass


    if incoming == "win"+userID:
        show("",0)
        show("",1)
        show("Winner!",2)
        break
    elif incoming == "lose"+userID:
        show('',0)
        show("",1)
        show("Loser!",2)
        break
        


    