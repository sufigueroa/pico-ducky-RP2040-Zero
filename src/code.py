import supervisor


import time
import digitalio
from board import *
import board
from duckyinpython import *


# sleep at the start to allow the device to be recognized by the host computer
time.sleep(.5)

# turn off automatically reloading when files are written to the pico
#supervisor.disable_autoreload()
supervisor.runtime.autoreload = False

# if(board.board_id == 'waveshare_rp2040_zero'):
#     led = pwmio.PWMOut(board.LED, frequency=5000, duty_cycle=0)


progStatus = False
progStatus = getProgrammingStatus()
print("progStatus", progStatus)
if(progStatus == False):
    print("Finding payload")
    # not in setup mode, inject the payload
    payload = selectPayload()
    print("Running ", payload)
    runScript(payload)

    print("Done")
else:
    print("Update your payload")

led_state = False

async def main_loop():
    global led, button1

    button_task = asyncio.create_task(monitor_buttons(button1))
    pico_led_task = asyncio.create_task(blink_pico_led(led))
    await asyncio.gather(pico_led_task, button_task)

asyncio.run(main_loop())
