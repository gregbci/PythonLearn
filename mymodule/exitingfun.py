import signal
import sys
import time

terminate = False

def signal_handling(signum, frame):
    global terminate
    terminate = True

signal.signal(signal.SIGINT,signal_handling)

count = 1
while True:

    print("count = ", count)
    time.sleep(1)
    count += 1

    if terminate:
        print("I'll be back")
        break

print("bye")
