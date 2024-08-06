from threading import Thread
from time import *

def box():
    while True:
        print('---------Box Is Open')
        sleep(3)
        print('---------Box Is Closed')
        sleep(3)


def LED():
    while True:
        print('LED Is On')
        sleep(1)
        print('LED Is Off')
        sleep(1)

#creating threads
boxThread = Thread(target=box)
LED_Thread = Thread(target=LED)


#??? - don't quite understand this yet
boxThread.daemon=True
LED_Thread.daemon=True

#starting the threads?
boxThread.start()
LED_Thread.start()

#some funsies to make the terminal more chaotic
i=0
while True:
    print(i)
    i=i+1
    sleep(.1)
