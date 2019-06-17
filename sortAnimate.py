import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

fig, ax = plt.subplots()

def initXData():
    return list(range(500))

def initYData():
    y = list(range(500))
    random.shuffle(y)
    y = list(y)
    return y

xdata = initXData()
ydata = initYData()

def init():
    xdata = initXData()
    ydata = initYData()
    return plt.bar(xdata, ydata)

def swap(myList, pos1, pos2):
    myList[pos1], myList[pos2] = myList[pos2], myList[pos1] 
    return myList

def bubbleSortStep(myList):
    for x in range(len(myList) - 1):
        if myList[x] > myList[x+1]:
            swap(myList, x, x+1)

def update(frame):
    bubbleSortStep(ydata)
    fig.clear()
    ln = plt.bar(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, interval=3, blit=0)
plt.show()