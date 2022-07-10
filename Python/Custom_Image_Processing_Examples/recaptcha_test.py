import time
from typing import Tuple, Type
from PIL import Image
import pyautogui
import random

chrome_icon_pos = (34, 321, 57, 335)
captcha_pos = (38, 290, 70, 322)



def find_fragment_in_screenshot(target_path : str, pos : tuple):
    image = pyautogui.screenshot()
    # print("screenshot is done")
    # image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    target = Image.open(target_path)
    # image.show()
    image_px = image.load()
    target_px = target.load()
    image_rows = image.width
    image_columns = image.height
    target_rows = pos[2] - pos[0]
    target_columns = pos[3] - pos[1]

    a = b = 0

    # print("compere start")
    for x in range(image_rows - target_rows):
        for y in range(image_columns - target_columns):
            find = False
            pix = image_px[x, y]
            pix1 = target_px[pos[0], pos[1]]
            if (pix[0], pix[1], pix[2]) == (pix1[0], pix1[1], pix1[2]): 
                find = True
                a = x
                b = y
                u = x
                for i in range(pos[0], target_rows + pos[0]):
                    v = y
                    for j in range(pos[1], target_columns + pos[1]):
                        pix = image_px[u, v]
                        pix1 = target_px[i, j]
                        # print((x + u, y + v), (i, j), (pix[0], pix[1], pix[2]), (pix1[0], pix1[1], pix1[2]))
                        # if o == True:
                        #     print ('ggggggggggggggg')
                        #     pyautogui.moveTo(u, v, 0)    
                        if (pix[0], pix[1], pix[2]) != (pix1[0], pix1[1], pix1[2]):
                            find = False
                            break
                        v += 1
                    if find == False:
                        break
                    u += 1

            if find == True:
                return (a + target_rows / 2, b + target_columns / 2)
    print('compere end')      
    return (0, 0)
    

pos = find_fragment_in_screenshot('chrome_icon.png', chrome_icon_pos)
if pos != (0,0):
    pyautogui.moveTo(pos[0], pos[1], 2, pyautogui.easeInElastic)
    pyautogui.doubleClick()
else:
    print("doesn't find chrome_icon.png")
    exit()
time.sleep(1)
pyautogui.typewrite('https://patrickhlauke.github.io/recaptcha/', 0.2)
time.sleep(random.uniform(0.1, 0.5))
pyautogui.keyDown('enter')
time.sleep(random.uniform(2.6, 3.99))

t = 0
pos = find_fragment_in_screenshot('captcha.png', captcha_pos)
while True:
    if pos != (0,0):
        pyautogui.moveTo(pos[0] -1, pos[1] + 6, random.uniform(0.6, 1.2), pyautogui.easeInElastic)
        time.sleep(0.2)
        pyautogui.click()
        break
    else:
        if t > 10:
            print("doesn't find like_icon.png")
            exit()
        time.sleep(0.6)
        t += 0.6