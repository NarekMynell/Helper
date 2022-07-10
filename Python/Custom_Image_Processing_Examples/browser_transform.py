import time
from typing import Tuple, Type
from PIL import Image, ImageGrab
import PIL
import pyautogui
import os
import copy
import threading

screenshoot_dir = 'C:/Users/Admin/Pictures/Screenshots'

def open_chrome():
    pyautogui.rightClick(726, 1058)
    time.sleep(0.5)
    pyautogui.click(690, 926)


def get_match_poss(image, frame_color):
    image_px = image.load()
    if len(image_px[0, 0]) == 4:
        frame_color = (frame_color[0], frame_color[1], frame_color[2], image_px[0, 0][3])
    leftX = None
    rightX = None
    topY = None
    bottomY = None
    for y in range(image.height):
        for x in range(image.width):
            if image_px[x, y] == frame_color and image_px[x + 400, y] == frame_color and image_px[x, y + 400] == frame_color:
                leftX = x
                topY = y
                x += 401
                y += 401
                
                while(image_px[x, topY] == frame_color):
                    x +=1
                rightX = x - 1

                while(image_px[leftX, y] == frame_color):
                    y +=1 
                bottomY = y - 1
                return(leftX, rightX, topY, bottomY)
    return(None)

def sclae_browser(leftX, rightX, topY, bottomY, frame_color = (24, 187, 197)):
    image = ImageGrab.grab(None, False, True)
    x1, x2, y1, y2 = get_match_poss(image, frame_color)

    pyautogui.moveTo(x2 + 2, y1 + 150)
    time.sleep(0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(rightX, y1 + 150, 0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(x1 - 2, y1 + 150)
    time.sleep(0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(leftX, y1 + 150, 0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(leftX + 150, y1 + 2)
    time.sleep(0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(leftX + 150, topY, 0.1)    
    pyautogui.mouseUp()


    pyautogui.moveTo(leftX + 150, y2 + 2)
    time.sleep(0.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(leftX + 150, bottomY, 0.1)    
    pyautogui.mouseUp()

def make_screenshot(folder_path : str = screenshoot_dir):
    pyautogui.keyDown('win')
    time.sleep(0.1)
    pyautogui.keyDown('prtscr')
    pyautogui.keyUp('win')
    pyautogui.keyUp('prtscr')
    time.sleep(1)
    path = ''
    number = -1
    for filename in os.listdir(screenshoot_dir):
        f = os.path.join(screenshoot_dir, filename)
        name = ''
        find = False
        for l in f:
            if find == False and l == '(':
                find = True
            else:
                if l == ')':
                    i =  int(name)
                    if i > number:
                        number = i
                        path = f
                    break
                else:
                    if find == True:
                        name += l

    im = Image.open(path)
    im_px = im.load()
    im.close()
    os.remove(path)
    return im_px

    

# t = time.time()
# for i in range(0, 4):
#     width = 950
#     open_chrome()
#     time.sleep(0.5)
#     x1 = i * width + 1
#     x2 = (i + 1) * width + 1 
#     sclae_browser(x1, x2, 1, 500, frame_color = (24, 187, 197))
#     time.sleep(0.1)

# for i in range(0, 1):
#     width = 950
#     open_chrome()
#     time.sleep(0.5)
#     x1 = i * width + 1
#     x2 = (i + 1) * width + 1 
#     # sclae_browser(x1, x2, 501, 1000, frame_color = (24, 187, 197))
#     # time.sleep(0.1)



# print(time.time() - t)


# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')


# pyautogui.keyDown('win')
# time.sleep(0.1)
# pyautogui.keyDown('prtscr')
# pyautogui.keyUp('win')
# pyautogui.keyUp('prtscr')

# a = make_screenshot()


from selenium import webdriver
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_argument("start-minimized")

# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Admin\Downloads\chromedriver_win32\chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


url = "https://patrickhlauke.github.io/recaptcha/"
driver.get(url)
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/span/div[2]').click()

