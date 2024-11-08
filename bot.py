# pip3 install keyboard
# pip3 install pyautogui
# pip3 install opencv-python
import pyautogui
import time
import keyboard

def cautare_google():
    if pyautogui.locateOnScreen(r"path_to_file.jpg") != None:
        bara_cautare = pyautogui.locateOnScreen(r"path_to_file.jpg")
        pyautogui.click(bara_cautare)
        time.sleep(1)
        pyautogui.write("link_to_site")
        pyautogui.press('enter')

def click_videoclips():
    time.sleep(3)
    pyautogui.click(1793,544)

def afisare_coordonates():
    while not keyboard.is_pressed('x'):
        print(pyautogui.position())
        time.sleep(0.2)

raspuns = pyautogui.confirm("Veri sa incepi rularea programului?","Confirmare")
if(raspuns=="OK"):
    cautare_google()
    click_videoclips()
else:
    afisare_coordonates()
