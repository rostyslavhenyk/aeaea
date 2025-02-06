from microbit import *
import random
import radio

NotReceived = True
radio.config(queue=5, group=14, channel=56, power=4)
uart.init(baudrate=115200)
radio.on()
userCount = 0
start = True
queue = []
leaderboard = {
    "A":0,
    "B":0,
    "C":0,
    "D":0
}
userA = False
userB = False
userC = False
userD = False

def simon():
    if random.randint(0,100) < 80:
        return "1"
    else:
        return "0"

while True:
    if start:
        if button_a.is_pressed():
            display.scroll("sent")
            radio.send("are you ready")
            start = False
        sleep(100)
        continue


    while userA == False or userB == False:
        message = radio.receive()
        if message == "userA":
            userA = True
        if message == "userB":
            userB = True
        #if message == "userC":
            #userC = True
        #if message == "userD":
            #userD = True

    radio.send("send the game")
    roundCount = radio.receive()
    for i in range(10):
        sleep(100)
        first = None
        gameForRound = str(random.randint(0,10))
        simonSays = simon()
        radio.send("type"+gameForRound+simonSays)
        while len(queue)<2:
            Rec = radio.receive()
            if Rec:
                queue.append(Rec)
        sleep(100)

        for j in range(len(queue)):
            if queue[j][1] == "1":
                first=queue[j][0]
                break

        if first:
            leaderboard[first] += 1

        for j in queue:
            if j.endswith("1"):
                leaderboard[j[0]] += 1

        queue.clear()
        for j in leaderboard.keys():
            msg = j+str(leaderboard[j])+"\n"
            uart.write(msg)
            sleep(50)
            
    max_score = max(leaderboard.values())
    for i in leaderboard.keys():
        if leaderboard[i] == max_score:
            radio.send('win'+i)
        elif leaderboard[i] != max_score:
            radio.send("lose"+i)
        sleep(200)
    
