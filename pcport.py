import serial
import matplotlib.pyplot as plt

plt.ion()
port = serial.Serial('COM9', 115200)
rounds = 0
messages = []       # Holds the points for each player -- ex: ["A12", "B10", "C18"]
scores = {
    "A":0,
    "B":0,
    "C":0,
    "D":0
}
g = plt.bar(scores.keys(), scores.values(), width=0.4, color="red")

def graph(rounds, info):
    global g

    g.remove()
    players = info.keys()
    score = info.values()
    g = plt.bar(players, score, width=0.4, color="red")
    title ="Round: "+str(rounds)
    plt.title(title)
    plt.xlabel("Players")
    plt.ylabel("Scores")
    plt.show()


while rounds <=10:
    message = port.readline().decode().strip()
    if message and message not in messages:
        messages.append(message)

    if len(messages) == 4:      #prints info after recieving the 3 scores
        for i in messages:
            scores[i[0]] = int(i[1:])
        messages.clear()
        rounds += 1

    graph(rounds, scores)
    plt.pause(0.001)
