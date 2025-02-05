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

while True:
    incoming = radio.receive()
    if incoming == "are you ready":
        show("are you ready",2)
        show("press b",3)
        while not button_b.is_pressed():
            pass
        show("",2)
        show("",3)
        radio.send("userA")
        display.show("A", wait=False)
    if incoming == "send the game":
        round = 1
        while round <= 10:
            roundInfo = None
            while not roundInfo:
                roundInfo = radio.receive()
            if roundInfo and roundInfo.startswith("type"):
                gameForRound = int(roundInfo[4:])                
                game(round, games[gameForRound])
                round += 1
            elif roundInfo and roundInfo in players:
                pass
        else:
            break


# show on third line waiting for other players (?)
#try to send the send the game signal multiple times
# "simon says" at the start of round task
#better formulate the round tasks
# have temp co2 and light level(?) on the screen at all times(?)
    