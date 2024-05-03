# very first rough test
import pyautogui as pg
import time
 
def example_click_and_type():
    pg.click(807, 979)
    pg.typewrite("hello")
    pg.typewrite(["enter"])
    time.sleep(1)
     
    # time.sleep(1)
    pg.click(1111, 605)
     
a=3
time.sleep(1)
while(a>0):
    example_click_and_type()
    a=a-1