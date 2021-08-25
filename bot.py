import time 
from datetime import datetime 
import pyautogui
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb
lst=[
    ['https://teams.microsoft.com/l/meetup-join/19%3a214fd9df94fb4067a3609c2f2f5a06e0%40thread.tacv2/1627312110316?context=%7b%22Tid%22%3a%22c98c4c52-9ee2-4495-b36d-dcb3b3658d60%22%2c%22Oid%22%3a%22521a1318-bf0d-4b63-a798-791ac373c4a6%22%7d','11:35','12:20']
]
keyboard= Controller()

is_class_started =False
for lecture  in lst:
    while True :
        if is_class_started==False:
            if (datetime.now().hour == int(lecture[1].split(':')[0])and 
                datetime.now().minute == int(lecture[1].split(':')[1])):
                wb.open(lecture[0])
                is_class_started=True
                time.sleep(20)
                pyautogui.press('right')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
        elif   (datetime.now().hour == int(lecture[2].split(':')[0]) and
                datetime.now().minute == int(lecture[2].split(':')[1])):
                is_class_started=False
                pyautogui.hotkey('ctrl','shift','b')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                time.sleep(3)
                pyautogui.hotkey('alt','f4')
                #time.sleep(3)
                #pyautogui.hotkey('alt','f4')
                break
