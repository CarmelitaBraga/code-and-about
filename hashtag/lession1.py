import pyautogui
import time
# import tadula --> converte pdf em pandas


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True #pausa o código quando coloca o mouse na posição (0,0)

pyautogui.press("win")
#time.sleep(3)
#pyautogui.position() coloca o cursor na posição desejada
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("significado do nome lavina")
pyautogui.press("enter")
time.sleep(8)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("gif message website")
pyautogui.press("enter")
time.sleep(12)
pyautogui.hotkey("ctrl", "shift", "w")


# pip3 install pyautogui
# sudo apt-get install python3-tk python3-dev
# sudo apt-get install scrot

# traz base de dados de um doc para o python: pandas, numpy, openpyxl

#import pandas

#table = pandas.read_excel(r"/home/carmelita/Downloads/nome-do-arquivo")
