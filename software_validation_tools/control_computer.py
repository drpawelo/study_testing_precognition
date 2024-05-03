# very first rough test
# needs "pip install pyautogui"

import pyautogui as pg
import time
import random
from datetime import datetime

import winsound
frequency = 2500 # Set Frequency To 2500 Hertz
duration = 100 # Set Duration To 1000 ms == 1 second


print("let's start")



# variables
now = datetime.now()

time_int= ""
experimenter = "98"
random_number = 0
participant = ""
experimenter = "auto script"
time_string = ""

def reset_variables():
    global time_int
    global experimenter 
    global random_number
    global participant 
    global experimenter
    global time_string 

    now = datetime.now()
    time_int= now.strftime("%S%M%H%d%m") 
    experimenter = "98"
    random_number = random.randint(100,999)
    participant = f"{experimenter}{random_number}{time_int}"
    experimenter = "auto script"
    time_string = now.strftime("%m-%d-%Y %H-%M-%S")
    print("participant",participant)


def open_terminal():
    pg.hotkey('ctrl', 'shift', "'")   
    sleep_dot(1)


def open_sesame(): 
    pg.hotkey('win', 'd') 
    print(pg.size()[1])
    pg.moveTo(pg.size()[0] -50, 50)
    pg.doubleClick()
    sleep_dot(6)
    section_buzz()
    


def close_sesame():
    sleep_short()
    pg.moveTo(pg.size()[0] -50, pg.size()[1]/2)
    pg.click()
    sleep_short()
    pg.hotkey('alt', 'f4')   
    sleep_short()
    section_buzz()
    sleep_dot(9)
    section_buzz()



def refocus_mouse():
    sleep_short()
    pg.moveTo(pg.size()[0] / 2, pg.size()[1] / 2)
    pg.doubleClick()


def enter_ratings():
    positions = [(160,230),(610,230),(160,500),(610,500)]
    ratings = [1,2,3,4]
    random.shuffle(ratings)
    for index in range(len(positions)):
        pg.moveTo(positions[index][0], positions[index][1])
        pg.doubleClick()
        type_slowly(ratings[index], withEnter=False)
    sleep_short()
    done_button = (860,630)
    pg.moveTo(done_button[0], done_button[1])
    pg.doubleClick()
    sleep_dot(1)




def participate_in_study(): 
    pg.hotkey('ctrlleft','r')  
    sleep_dot(2)
    # rand_number = random.randint(10000, 99999)

    pg.typewrite(participant)
    press_and_wait('enter')
    press_and_wait('enter')
    section_buzz()
    sleep_dot(3)

    refocus_mouse()
    sleep_short("starting study")
    press_and_wait()
    press_and_wait()
    press_and_wait('p')
    press_and_wait('i')

    refocus_mouse()
    type_slowly(participant)

    refocus_mouse()
    type_slowly(experimenter)

    refocus_mouse()
    type_slowly(time_string)

    section_buzz()
    # intros
    press_and_wait()
    press_and_wait()
    press_and_wait()


    # audio
    section_buzz()
    sleep_dot(3)

    section_buzz()
    press_and_wait()
    press_and_wait()
    press_and_wait()
    press_and_wait()
    press_and_wait()
    section_buzz()


    section_buzz()
    # videos (3,2,1,video 1s) x4 (together 12 seconds)
    sleep_dot(13)
    section_buzz()

    press_and_wait()
    press_and_wait()

    # ratings
    # click DONE
    enter_ratings()
    sleep_short()


    press_and_wait()
    press_and_wait()
    press_and_wait()

    # winning video
    sleep_dot(2)

    press_and_wait()
    # end
    sleep_dot(2)
    
    press_and_wait()
    press_and_wait()
    press_and_wait()




def type_slowly(word, withEnter = True):
    for letter in f"{word}":
        time.sleep(0.05)
        winsound.Beep(int(frequency*1.5), int(duration/5))
        pg.press(letter)
    if withEnter:
        press_and_wait('enter')
    sleep_short()




def sleep_dot(seconds):
    print(f"wait {seconds} seconds", end="")
    for which in range(seconds):
        winsound.Beep(frequency, duration *2)
        time.sleep(1)
        print(">", end='')
    winsound.Beep(int(frequency/2), duration *3)
    print()

def press_and_wait(key='space'):
    pg.press(key)
    winsound.Beep(int(frequency*0.8), int(duration))
    winsound.Beep(int(frequency*0.9), int(duration))
    winsound.Beep(int(frequency*1.0), int(duration*3))
    # time.sleep(0.5)

def sleep_short(message = ""):
    print(message)
    winsound.Beep(frequency, duration*5)
    # time.sleep(0.5)
        
def section_buzz():
    winsound.Beep(int(frequency/3*4), duration )
    winsound.Beep(int(frequency), duration )
    winsound.Beep(int(frequency/3*2), duration )
    winsound.Beep(int(frequency/3*1), duration )



def run_experiment_once():
    reset_variables()
    open_terminal()
    open_sesame()
    participate_in_study()
    close_sesame()
    
def run_experiment_many_times(how_many_times): 
    for itteration in range(how_many_times):
        run_experiment_once()
    

run_experiment_many_times(2000)