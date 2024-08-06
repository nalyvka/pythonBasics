from threading import Thread
from time import *

def box(delayTime):
    while True:
        print('---------Box Is Open')
        sleep(delayTime)
        print('---------Box Is Closed')
        sleep(delayTime)


def LED(delayTime):
    while True:
        print('LED Is On')
        sleep(delayTime)
        print('LED Is Off')
        sleep(delayTime)

#arguments to pass to the functions
delay_box = 3
delayLED = 1

boxThread = Thread(target=box, args=(delay_box,))
LED_Thread = Thread(target=LED, args=(delayLED,))

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
