import pyautogui
import tkinter as tk

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

xCorner1 = width * 0.25
yCorner1 = height * 0.25
xCorner2 = width * 0.75
yCorner2 = height * 0.25
xCorner3 = width * 0.25
yCorner3 = height * 0.75
xCorner4 = width * 0.75
yCorner4 = height * 0.75

while True:
    pyautogui.moveTo(xCorner1, yCorner1, duration = 2.5)
    pyautogui.moveTo(xCorner2, yCorner2, duration = 2.5)
    pyautogui.moveTo(xCorner3, yCorner3, duration = 2.5)
    pyautogui.moveTo(xCorner4, yCorner4, duration = 2.5)