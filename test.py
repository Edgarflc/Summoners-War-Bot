import pyautogui
import time

def click_on_bluestacks(x, y):
    # Attendez 5 secondes pour vous donner le temps de changer de fenêtre
    time.sleep(5)

    # Trouvez la fenêtre Bluestacks
    bluestacks_windows = pyautogui.getWindowsWithTitle('Bluestacks')

    # Vérifiez si la fenêtre Bluestacks a été trouvée
    if len(bluestacks_windows) == 0:
        print("La fenêtre Bluestacks n'a pas été trouvée.")
        return

    # Si la fenêtre Bluestacks a été trouvée, effectuez un clic à des coordonnées spécifiques
    bluestacks_window = bluestacks_windows[0]

    # Déplacez le curseur de souris à ces coordonnées dans la fenêtre Bluestacks
    pyautogui.moveTo(bluestacks_window.left + x, bluestacks_window.top + y)

    # Cliquez à ces coordonnées
    pyautogui.click()

# Appelez la fonction click_on_bluestacks avec les coordonnées (100, 100)
if __name__ == "__main__":
    click_on_bluestacks(100, 100)
