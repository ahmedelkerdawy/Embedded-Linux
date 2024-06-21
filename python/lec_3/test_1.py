# using pyautogui to open vscode and install some tools from extension

import pyautogui
from time import sleep

pyautogui.hotkey('win')
sleep(2)
pyautogui.typewrite("vs")
sleep(2)
pyautogui.press("enter")
sleep(2)
pyautogui.hotkey('ctrl','shift','x')
sleep(2)

pyautogui.moveTo(140 , 157)
sleep(2)

extentions = [" c++ testmate " , " clangd " , " c++ helper " , " cmake "," cmake tool "]
for extention in extentions:
    pyautogui.typewrite(extention)
    sleep(3)
    pyautogui.doubleClick(325 , 223)        #  install icon
    sleep(10)
    pyautogui.doubleClick(143,142)          #  extension view box
    sleep(3)
    pyautogui.press('delete' ,presses=15)
    sleep(6)
    if extention == " cmake tool ":
        break
    pyautogui.doubleClick(143,142)
 
 
 
 # to find position of cursor constanly    
'''
try:
    while True:
        x,y =pyautogui.position()
        print(f"x={x} , y = {y}")
except KeyboardInterrupt:
    printf("\n")

'''