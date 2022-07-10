import time
import pyautogui
import keyboard


s = 7375

# while True:
#     pyautogui.rightClick(240, 999)
#     time.sleep(0.1)
#     pyautogui.leftClick(313, 853)
#     time.sleep(0.1)
#     pyautogui.write(str(s))
#     pyautogui.press('enter')
#     time.sleep(0.1)
#     pyautogui.press('enter')
#     time.sleep(0.1)
#     print(s)
#     s = s+1
pyautogui.PAUSE = 0.07

try:
    while not keyboard.is_pressed('q'):
        pyautogui.rightClick(240, 999)
        time.sleep(0.01)
        pyautogui.leftClick(313, 853)
        time.sleep(0.01)
        pyautogui.write(str(s))
        pyautogui.press('enter')
        time.sleep(0.01)
        pyautogui.press('enter')
        time.sleep(0.01)
        print(s)
        s = s+1
except KeyboardInterrupt:
    pass