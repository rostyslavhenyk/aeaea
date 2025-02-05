from microbit import *
from bme688 import *
from OLED import *
from main_game import *
import radio

games = ["shake", "tilt left", "tilt right", "Press button B", "Press button A", "flip"]
radio.config(queue=5, group = 14, channel=56, power=4)
radio.on()
init_display()
players = ["A1","A0","B0","B1","C0","C1"]

while True:
    incoming = radio.receive()
    if incoming == "are you ready":
        show("are you ready",2)
        show("press b",3)
        while not button_b.is_pressed():
            pass
        show("",2)
        show("",3)
        radio.send("userD")
    if incoming == "send the game":
        round = 1
        while round <= 10:
            roundInfo = None
            while not roundInfo:
                roundInfo = radio.receive()
            if roundInfo and roundInfo.startswith("type"):
                if len(roundInfo[4:]) == 2:
                    gameForRound = int(roundInfo[4])
                    simonSays = int(roundInfo[5])
                elif len(roundInfo[4:]) == 3:
                    gameForRound = int(roundInfo[4]+roundInfo[5])
                    simonSays = int(roundInfo[6])
                game(round, games[gameForRound], simonSays)
                round += 1
            elif roundInfo and roundInfo in players:
                pass
        else:
            break


# show on third line waiting for other players (?)
#try to send the send the game signal multiple times
# "simon says" at the start of round task
#better formulate the round tasks

