import time
import pyautogui
# memungkinkan script Python kita mengontrol mouse dan keyboard untuk 
# mengotomatiskan interaksi dengan aplikasi lain. 

time.sleep(4)
f = open('animals.txt')

for line in f :
    pyautogui.typewrite(line)
    pyautogui.presso('enter')