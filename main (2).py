from microbit import *
import random 
import radio 

NotReceived = True
radio.config(queue=5, group=14, channel=56, power=4)
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
#userC = False
#userD = False
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
          #  userD = True
        

    
    radio.send("send the game")
    roundCount = radio.receive()
    for i in range(10):
        sleep(100)
        gameForRound = str(random.randint(7,8))
        radio.send("type"+gameForRound)
        while len(queue)<2:
            Rec = radio.receive()
            if Rec:
                queue.append(Rec)
                print(queue)
        sleep(100)
        leaderboard[queue[0][0]] += 1 
        
        for i in queue:
            if i.endswith("1"):
                leaderboard[i[0]] += 1
        
        queue.clear()

    print("Leaderboard:")
    for i in leaderboard.keys():
        print(i,":",leaderboard[i])


        
        
