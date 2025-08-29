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
ONLY TESTED ON 13" MACBOOK AIR (3024 x 1964)
##################
'''

book_abbr_dict = {"Matthew" : "Matt", "Mark" : "Mark", "Luke" : "Luke", "John" : "John", "Acts" : "Acts", "Romans" : "Rom", "1 Corinthians" : "1 Cor", "2 Corinthians" : "2 Cor", "Galatians" : "Gal", "Ephesians" : "Eph", "Philippians" : "Phi", "Colossians" : "Col", "1 Thessalonians" : "1 Thes", "2 Thessalonians" : "2 Thes", "1 Timothy" : "1 Tim", "2 Timothy" : "2 Tim", "Titus" : "Titus", "Philemon" : "Phil", "Hebrews" : "Heb", "James" : "James", "1 Peter" : "1 Pet", "2 Peter" : "2 Pet", "1 John" : "1 John", "2 John" : "2 John", "3 John" : "3 John", "Jude" : "Jude", "Revelation" : "Rev"}
book_length_dict = {"Matthew" : 28, "Mark" : 16, "Luke" : 24, "John" : 21, "Acts" : 28, "Romans" : 16, "1 Corinthians" : 16, "2 Corinthians" : 13, "Galatians" : 6, "Ephesians" : 6, "Philippians" : 4, "Colossians" : 4, "1 Thessalonians" : 5, "2 Thessalonians" : 3, "1 Timothy" : 6, "2 Timothy" : 4, "Titus" : 3, "Philemon" : 1, "Hebrews" : 13, "James" : 5, "1 Peter" : 5, "2 Peter" : 3, "1 John" : 5, "2 John" : 1, "3 John" : 1, "Jude" : 1, "Revelation" : 22}

starting_book = 'Revelation'             # change as necessary, should be the nonabbreviated version, reference book_abbr_dict above
starting_chapter = 19


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

def setup(search_query):
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
    p.moveTo(115, 99, duration = 0.2)
    # p.moveTo(180, 62, duration = 0.2) # first tab position
    p.click()

    t(7) # waiting for website to load...sometimes it takes REALLY long....fluke

    p.keyDown('command')
    p.press('f')
    p.keyUp('command')
    p.typewrite(search_query)
    p.press('esc')
    # p.press('right', presses=4)
    copy()

    # navigate to subsplash
    p.keyDown('command')
    p.press('t')
    p.keyUp('command')
    p.moveTo(219,99, duration = 0.1)
    p.click() 

    t(7)  # waiting for website to load....


    p.moveTo(70, 500, duration = 1.1)       # 187, 538  apps
    t(1)
    p.click()
    p.moveRel(0, -150, duration=0.5)        # 187, 388  push notification
    p.click()

def create_notification(starting_book, starting_chapter):
    books = list(book_abbr_dict.keys())  # Get all book names in order
    start_index = books.index(starting_book)  # Find index of the starting book

    for book in books[start_index:]:  # Iterate from starting book onwards
        chapters = book_length_dict[book]  # Get number of chapters

        for i in range(starting_chapter, chapters + 1):  # Iterate through all chapters
            p.keyUp('fn')
            p.moveTo(1296, 153, duration=0.5)  # Create notification
            p.click()
            p.moveTo(1245, 352, duration=0.8)  # Notification group dropdown
            p.click()
            p.moveTo(1229, 486, duration=0.5)  # Select daily verse
            p.click()
            p.moveTo(586, 321, duration=0.3)  # Verse textbox
            p.click()
            paste()

            p.moveTo(556, 722)  # Attachment
            p.click()
            p.moveTo(1251, 252, duration=0.2)  # Select media item
            p.click()
            p.moveTo(1145, 467, duration=0.2)  # Search media item
            p.click()

            t(1)
            p.keyUp('fn')
            p.typewrite(f"{book} {i}", interval=0.06)
            t(0.5)
            p.press('enter')
            p.click(x=1205, y=525, duration=0.7)  # Select media item     
            p.click(x=1100, y=150, duration=0.3)  # Apply
            p.click(x=1275, y=250, duration=0.4)  # Schedule

            p.keyDown('command')
            p.press('1')
            p.keyUp('command')
            p.press('left', presses=3, interval=0.1)
            p.keyDown('command')
            p.press('c')
            p.keyUp('command')
            p.keyDown('command')
            p.press('2')
            p.keyUp('command')
            p.click(x=560, y=405, duration=0.2)  # Date
            p.keyDown('command')
            p.press('a')
            p.keyUp('command')
            p.keyDown('command')
            p.press('v')
            p.keyUp('command')
            p.press('enter')
            p.click(x=860, y=405)  # Time
            p.keyDown('command')
            p.press('a')
            p.keyUp('command')
            p.press('backspace')
            p.keyUp('fn')  # Needed because of PyAutoGUI bug
            p.typewrite("8:00 am") 
            p.click(x=940, y=665, duration=0.6)  # Schedule
            p.click(x=345, y=155, duration=0.5)  # Back to push notifications
            # p.moveTo(1305, 150, duration=1)  # Create new notification
            # # p.click()

            p.keyDown('command')
            p.press('1')
            p.keyUp('command')
            p.press('right', presses=3, interval=0.1)
            p.press('down')
            p.keyDown('command')
            p.press('c')
            p.keyUp('command')
            p.keyDown('command')
            p.press('2')
            p.keyUp('command')
        starting_chapter = 1

# setup(book_name + " " + str(starting_chapter))

t(2)
'''
Reminder these are the prerequisties
1. Daily verse spreadsheet is the first tab
2. Verse is copied
3. Subsplash should be on Apps > Push Notifications
'''
create_notification(starting_book, starting_chapter)







