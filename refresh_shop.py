import pyautogui
import time

mysticalScrollFound = False
nbMysticalScroll = 0

ladScrollFound = False
nbLadScroll = 0

bluestacks_windows = pyautogui.getWindowsWithTitle('Bluestacks')

####################### GENERIC FUNCTIONS #######################

def check_window():
    time.sleep(5)

    if len(bluestacks_windows) == 0:
        print("La fenêtre Bluestacks n'a pas été trouvée.")
        return

def find_image(image_path):
    global mysticalScrollFound
    global ladScrollFound

    bluestacks_window = bluestacks_windows[0]
    position = pyautogui.locateOnScreen(image_path, region=(bluestacks_window.left, bluestacks_window.top, bluestacks_window.width, bluestacks_window.height))
    if position is not None:
        mysticalScrollFound = True
        ladScrollFound = True
        return position

def click_window(x, y):
    bluestacks_window = bluestacks_windows[0]
    pyautogui.moveTo(bluestacks_window.left + x, bluestacks_window.top + y)
    pyautogui.click()

####################### FIND ITEMS FUNCTIONS #######################

def find_mystical_scroll():
    global mysticalScrollFound
    global nbMysticalScroll

    position = find_image("images/mysticalScroll.PNG")
    if (mysticalScrollFound == True and position is not None):
        nbMysticalScroll += 1
        print("Nombre de Vélins mystiques obtenus :", nbMysticalScroll)
        click_window(position.left, position.top)
        time.sleep(1)
        click_window(610, 1000)
        time.sleep(1)
        click_window(1112, 867)
        time.sleep(1)

def find_lad_scroll():
    global ladScrollFound
    global nbLadScroll

    position = find_image("images/ladScroll.PNG")
    if (ladScrollFound == True and position is not None):
        nbLadScroll += 5
        print("Nombre de morceaux de Vélins L&D obtenus :", nbLadScroll)
        click_window(position.left, position.top)
        time.sleep(1)
        click_window(610, 1000)
        time.sleep(1)
        click_window(1112, 867)
        time.sleep(1)

####################### ENGINE FUNCTIONS #######################

def refresh_shop():
    global mysticalScrollFound
    global ladScrollFound

    while True:
        find_mystical_scroll()
        find_lad_scroll()

        click_window(2202, 272)
        time.sleep(1)

        mysticalScrollFound = False
        ladScrollFound = False

def events():
    check_window()
    refresh_shop()

############################ MAIN ############################

if __name__ == "__main__":
    events()
