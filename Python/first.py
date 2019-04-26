#from mss import mss
#with mss() as sct #   sct.shot()
import pyautogui
import  time

x=1
while True:
    time.sleep(5)
    pyautogui.screenshot('/Users/tisha/PycharmProjects/screenshot'+str(x)+'.jpg')
    x=x+1