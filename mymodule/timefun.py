import time

# LSL seems to use this one
print(time.clock_gettime(time.CLOCK_MONOTONIC_RAW))


print(time.monotonic())
print(time.time())


