from pad4pi import rpi_gpio
import random
import time
from pygame import mixer # Load the required library
import os
import random
import dircache


prevPath=""
currPath=""
def playSound(path):
    mixer.music.stop()
    mixer.music.load(path)
    mixer.music.play()

def getRandomFileinFolder(dir):
  filename = random.choice(dircache.listdir(dir))
  path = os.path.join(dir, filename)
  return path

def getaRandomFile():
  dir=random.randint(1,9)
  return getRandomFileinFolder(str(dir))

def getPath(key):
  global currPath
  global prevPath
  if ( key!="#" and key!="*" and key!="0"):
    path=getRandomFileinFolder(key)
  if (key=="0"):
    path=currPath 
  elif (key=="*"):
    path=getaRandomFile()
    # Some random sound
  elif (key=="#"):
    path=prevPath
 
  if ( key!="#" and key!="*" ):
    prevPath=currPath
    currPath=path
  return path



def processKey(key):
  print(key)
  path=getPath(key)
  playSound(path)

# Setup Keypad
KEYPAD = [
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"],
        ["*","0","#"]
]

ROW_PINS = [11,23,24,25] # BCM numbering
COL_PINS = [17,27,22] # BCM numbering
mixer.init()
factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
keypad.registerKeyPressHandler(processKey)
#raw_input("Press Enter to continue...")
while 1:
    time.sleep(10)
keypad.cleanup()
