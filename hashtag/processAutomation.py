import pyautogui as pyai
import pandas as pd
import pyperclip
import time
from datetime import date, timedelta


pyai.PAUSE = 1
pyai.FAILSAFE = True

pyai.press("win")
pyai.write("firefox")
pyai.press("enter")
pyai.hotkey("ctrl", "t")

pyai.write("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyai.press("enter")

time.sleep(5)

pyai.click(x =396, y=337, clicks = 2)
time.sleep(1)
pyai.click(x =396, y=337, button="right")
time.sleep(1)
pyai.click(x=457, y=684)

table = pd.read_excel("/home/carmelita/Downloads/Vendas - Dez.xlsx")

unitValue = table["Valor Unitário"].sum()
finalValue = table["Valor Final"].sum()

msg = f"""
Good morning!

Yesterday's revenue was about U$ {finalValue},00.
The total sum of items sold: {unitValue}.

Best regards,
C.B."""

pyai.press("win")
pyai.write("firefox")
pyai.press("enter")
pyai.hotkey("ctrl", "t")
pyai.write("https://mail.google.com/mail/u/0/#inbox")
pyai.press("enter")
time.sleep(3)
pyai.click(x=141, y=243)

time.sleep(1)
pyai.write("carmelitabraga8@gmail.com")
pyai.press("enter")
pyai.press("tab")
pyai.write(f"Report of the {date.today() - timedelta(days=1)}")
pyai.press("tab")
pyai.write(msg)
pyai.click(x=841, y=735)