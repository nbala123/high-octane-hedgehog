import time
import board
import analogio
import digitalio

button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.OUTPUT

while True:
    button.value = True
