import time
from typing import Tuple, Type
from PIL import Image
import pyautogui
import random

chrome_icon_pos = (41, 331, 57, 332)
like_tab_icon_pos = (677, 331, 689, 334)
do_it_icon_pos = (970, 565, 1080, 566)
like_icon_pos = (1073, 776, 1097, 787)
more_tasks_icon_pos = (571, 618, 589, 628)
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
    return (0, 0)
    

def wiq_like():
    # find chrome_icon
    pos = find_fragment_in_screenshot('chrome_icon.png', chrome_icon_pos)
    if pos != (0,0):
        pyautogui.moveTo(pos[0], pos[1], 2, pyautogui.easeInElastic)
        pyautogui.doubleClick()
    else:
        print("doesn't find chrome_icon.png")
        exit()
    time.sleep(1)
    pyautogui.typewrite('wiq.ru/tasks.php', 0.2)
    time.sleep(random.uniform(0.1, 0.5))
    pyautogui.keyDown('enter')
    time.sleep(random.uniform(3.6, 4.99))

    # find like_tab_icon
    pos = find_fragment_in_screenshot('like_tab_icon.png', like_tab_icon_pos)
    if pos != (0,0):
        pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.9), pyautogui.easeInElastic)
        pyautogui.click()
    else:
        print("doesn't find like_tab_icon.png")
        exit()

    time.sleep(random.uniform(2.7, 4.3))

    # find task icon
    i = 0
    while True:
        if i == 0:
            pyautogui.scroll(2000)
        like_pos = (0, 0)
        t = 0
        while True:
            pos = find_fragment_in_screenshot('do_it_icon.png', do_it_icon_pos)
            if pos != (0,0):
                pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
                pyautogui.click()
                like_pos = pos
                break
            else:
                if t > 10:
                    print("doesn't find do_it_icon.png")
                    exit()
                time.sleep(0.6)
                t += 0.6

        # find like icon 
        o = True    

        t = 0
        while True:
            pos = find_fragment_in_screenshot('like_icon.png', like_icon_pos)
            if pos != (0,0):
                print(pos)
                pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
                pyautogui.click()
                break
            else:
                if t > 10:
                    print("doesn't find like_icon.png")
                    t += 1
                    break
                time.sleep(0.6)
                t += 0.6

        # to close second window
        pyautogui.moveTo(1532, 52, random.uniform(0.6, 1.2), pyautogui.easeInElastic)
        pyautogui.click()
        # to check task
        pyautogui.moveTo(like_pos[0], like_pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
        pyautogui.click()

        time.sleep(3)
        
        i += 1

        if(i > 3):
            pyautogui.scroll(-2000)
            pos = find_fragment_in_screenshot('more_tasks_icon.png', more_tasks_icon_pos)
            pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
            pyautogui.click()
            i = 0
            time.sleep(1)

# print("hello")
# myScreenshot = pyautogui.screenshot()
# myScreenshot.save(r'file name.png')


wiq_like()



# image = pyautogui.screenshot()
# # image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
# target = Image.open('do_it_icon.png')
# # print(type(image), type(target))
# image_px = image.load()
# target_px = target.load()
# image_rows = image.width
# image_columns = image.height
# pos = do_it_icon_pos
# target_rows = pos[2] - pos[0]
# target_columns = pos[3] - pos[1]


    # find task icon
# i = 0
# while True:
#     like_pos = (0, 0)
#     t = 0
#     while True:
#         pos = find_fragment_in_screenshot('do_it_icon.png', do_it_icon_pos)
#         if pos != (0,0):
#             pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
#             # pyautogui.click()
#             like_pos = pos
#             break
#         else:
#             if t > 10:
#                 print("doesn't find do_it_icon.png")
#                 exit()
#             time.sleep(0.6)
#             t += 0.6

