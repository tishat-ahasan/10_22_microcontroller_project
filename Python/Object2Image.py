import pyautogui

x=6
while x<=10:
    n = input("Enter 1 for capture:")
    if n == "1":
        pyautogui.screenshot(str(x) + '.jpg', region=(0, 150, 500, 400))
        x = x + 1



