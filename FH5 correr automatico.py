import pyautogui
import time
import threading
import os

vezes = input("Quantas vezes quer repetir a corrida? ")
t= 490
v = 0
a = 0
time.sleep(5)

while v<int(vezes):
    while a<int(t):
        pyautogui.keyDown('w')

        a+=1
    pyautogui.keyUp('w')
    a=0
    v+=1
    if v==int(vezes):
        if int(vezes)>1:
            print("A corrida foi feita por",vezes,"vezes")
        else:
            print("A corrida foi feita por",vezes,"vez")
    else :
        time.sleep(10)
        pyautogui.press('x')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(8)
        pyautogui.press('enter')
        time.sleep(8)
