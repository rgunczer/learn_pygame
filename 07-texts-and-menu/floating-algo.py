import time
import math

# Set the initial y position
y = 0

# Set the amplitude and frequency of the motion
amplitude = 50
frequency = 0.1

# Set the start time
start_time = time.time()

while True:
    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Calculate the new y position
    y = amplitude * math.sin(frequency * elapsed_time)

    # Print the current y position
    print(f"[{y}], elapsed: [{elapsed_time}]")

    # Wait for a short amount of time before updating again
    time.sleep(0.01)
