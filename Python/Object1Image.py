import pyautogui

x=1
while x<=5:
    n = input("Enter 1 for capture:")
    if n == "1":
        pyautogui.screenshot(str(x) + '.jpg', region=(0, 150, 500, 400))
        x = x + 1




