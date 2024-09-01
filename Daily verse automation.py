import pyautogui as p
from time import sleep as t

# print(pyautogui.KEYBOARD_KEYS)        # for all the keybinds you can use with pyautogui

# https://pyautogui.readthedocs.io/en/latest/index.html
                                        # note: hotkey doesn't really work as it's described
                                        #    so you just have to do keyDown, press, keyUp


p.FAILSAFE=True                         # FAILSAFE: move cursor to top left corner to stop execution

def copy():
    p.keyDown('command')
    p.press('c')
    p.keyUp('command')
def paste():
    p.keyDown('command')
    p.press('v')
    p.keyUp('command')


'''
##################
ONLY TESTED ON 14" MACBOOK (3024 x 1964)
##################
'''



book_name = 'John'                       # change as necessary 



'''
For setup function:
- Uses Firefox browser
- Daily verse spreadsheet must be in first bookmark position
- Subsplash must be logged in and put in second bookmark position

At the end of the setup function, three main things should be the case:
1. Daily verse spreadsheet is the first tab
2. Verse is copied
3. Subsplash should be on Apps > Push Notifications
'''

def setup():
    # open browser on Mac using system search
    p.keyDown('command')
    p.press('space')
    p.keyUp('command')
    p.typewrite('fir')                   # Firefox
    p.press('enter')
    t(1)


    # enter full screen
    p.keyDown('ctrl')
    p.keyDown('command')
    p.press('f')
    p.keyUp('ctrl')
    p.keyUp('command')
    t(1)


    # saved bookmark for google sheet 
    p.moveTo(90, 134, duration = 0.2)
    # p.moveTo(180, 62, duration = 0.2) # first tab position
    p.click()

    t(7) # waiting for website to load...sometimes it takes REALLY long....fluke

    p.keyDown('command')
    p.press('f')
    p.keyUp('command')
    p.typewrite(book_name[:4])
    p.press('esc')
    p.press('right', presses=4)
    copy()

    # navigate to subsplash
    p.keyDown('command')
    p.press('t')
    p.keyUp('command')
    p.moveTo(187,138, duration = 0.1)
    p.click() 

    t(7)  # waiting for website to load....


    p.moveRel(0, 400, duration = 0.8)       # 187, 538  apps
    p.click()
    p.moveRel(0, -150)                      # 187, 388  push notification
    p.click()

def create_notification(book_name, chapters):
    for i in range(1, chapters+1):
        p.keyUp('fn')
        p.moveTo(1380, 188, duration = 0.2)       # create notification
        p.click()
        p.moveTo(1287, 391, duration=0.7)         # notification group dropdown
        p.click()
        p.moveTo(1287, 510, duration=0.4)         # select daily verse
        p.click()
        p.moveTo(357, 319, duration=0.2)          # verse textbox
        p.click()
        #p.hotkey('command', '1')
        paste()


        p.moveTo(457, 750)                      # attachment
        p.click()
        p.moveTo(1325, 293, duration=0.2)       # select media item

        p.click()
        p.moveTo(1189, 504, duration=0.2)       # search media item
        p.click()

        t(1)
        p.keyUp('fn')
        p.typewrite(book_name + ' ' + str(i), interval=0.06)
        t(0.5)
        p.press('enter')
        p.click(x=1189, y=570, duration=0.7)        # select media item     
        p.click(x=1189, y=190, duration=0.3)        # apply
        p.click(x=1189, y=290, duration=0.4)        # schedule
        #p.hotkey('command', '1')
        p.keyDown('command')
        p.press('1')
        p.keyUp('command')

        p.press('left', presses=2, interval=0.1)
        p.keyDown('command')
        p.press('c')
        p.keyUp('command')
        p.keyDown('command')
        p.press('2')
        p.keyUp('command')
        p.click(x=596, y=473, duration=0.2)     # date
        p.keyDown('command')
        p.press('a')
        p.keyUp('command')
        p.keyDown('command')
        p.press('v')
        p.keyUp('command')
        p.press('enter')
        p.click(x=816, y=473)
        p.keyDown('command')
        p.press('a')
        p.keyUp('command')
        p.press('backspace')
        p.keyUp('fn')                                       # needed because of pyautogui bug
        p.typewrite("8:00 am") 
        p.click(x=816, y=523, duration=0.6)
        p.click(x=976, y=728, duration=0.5)
        p.moveTo(414, 195, duration=1)
        p.click()
        
        p.keyDown('command')
        p.press('1')
        p.keyUp('command')
        p.press('right', presses=2, interval=0.1)
        p.press('down')
        p.keyDown('command')
        p.press('c')
        p.keyUp('command')
        p.keyDown('command')
        p.press('2')
        p.keyUp('command')


#setup()

t(2)                                    
create_notification(book_name, 21)      # change number of chapters to match book (Matt = 28, Mark = 16, etc...)







