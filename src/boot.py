from board import *
import board
import digitalio
import storage


noStorage = False
noStoragePin = digitalio.DigitalInOut(board.GP15)
noStoragePin.switch_to_input(pull=digitalio.Pull.UP)
noStorageStatus = noStoragePin.value

if(board.board_id == 'waveshare_rp2040_zero'):
    # On Pi Pico, default to USB visible
    noStorage = not noStorageStatus

if(noStorage == True):
    # don't show USB drive to host PC
    storage.disable_usb_drive()
    print("Disabling USB drive")
else:
    # normal boot
    print("USB drive enabled")
