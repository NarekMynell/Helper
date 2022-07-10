# import cv2
# import sys

# imagePath = sys.argv[1]

# image = cv2.imread(imagePath)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# faces = faceCascade.detectMultiScale(
#     gray,
#     scaleFactor=1.3,
#     minNeighbors=3,
#     minSize=(30, 30)
# )

# print("[INFO] Found {0} Faces!".format(len(faces)))

# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# status = cv2.imwrite('faces_detected.jpg', image)
# print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
# if status == True:
#     cv2.imshow('Contrast Image', image)
#     cv2.waitKey(0)


import time
from typing import Tuple, Type
from PIL import Image
import pyautogui
import random
import cv2
import numpy as np
from enum import Enum

o = False

chrome_icon_pos = (34, 321, 57, 335)
like_tab_icon_pos = (678, 330, 699, 340)
do_it_icon_pos = (971, 563, 1016, 587)
like_icon_pos = (1073, 776, 1125, 791)
more_tasks_icon_pos = (571, 618, 589, 628)
# def find_fragment_in_screenshot(targetImagePath : str):
#     # try:
#     targetImage = cv2.imread(targetImagePath)
#     image = pyautogui.screenshot()
#     image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#     # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     result = cv2.matchTemplate(image, targetImage, cv2.TM_CCOEFF)
#     min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)

#     height, width = targetImage.shape[:2]

#     top_left = max_loc
#     return (top_left[0] + width / 2, top_left[1] + height / 2)
#     # except:
#     #     return (0, 0)




# pos = find_fragment_in_screenshot('do_it_icon.png')
# if pos != (0,0):
#     pyautogui.moveTo(pos[0], pos[1], 2, pyautogui.easeInElastic)
#     pyautogui.doubleClick()
# else:
#     print("doesn't find chrome_icon.png")

# # time.sleep(0.5)
# # pyautogui.typewrite('wiq.ru/tasks.php', 0.4)
# # time.sleep(random.uniform(0.1, 0.5))
# # pyautogui.keyDown('enter')
# # time.sleep(random.uniform(5.6, 8.99))


# # pos = find_fragment_in_screenshot('like_tab_icon.png')
# # if pos != (0,0):
# #     pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.9), pyautogui.easeInElastic)
# #     pyautogui.click()
# # else:
# #     print("doesn't find like_tab_icon.png")

# # time.sleep(random.uniform(2.7, 4.3))

# # i = 0
# # while True:
# #     like_pos = pos = find_fragment_in_screenshot('do_it_icon.png')
# #     while True:
# #         if pos != (0,0):
# #             pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
# #             pyautogui.click()
# #             break
# #         else:
# #             time.sleep(0.3)



# #     pos = find_fragment_in_screenshot('like_icon.png')
# #     while True:
# #         if pos != (0,0):
# #             pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
# #             pyautogui.click()
# #             break
# #         else:
# #             time.sleep(0.3)
    


# #     pyautogui.moveTo(1532, 52, random.uniform(0.6, 1.2), pyautogui.easeInElastic)
# #     pyautogui.click()

# #     pyautogui.moveTo(like_pos[0], like_pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
# #     pyautogui.click()

# #     time.sleep(3)
    
# #     i += 1

# #     if(i > 3):
# #         pyautogui.scroll(-100)
# #         pos = find_fragment_in_screenshot('more_tasks.png')
# #         pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
# #         pyautogui.click()
# #         i = 0
# #         time.sleep(3)













def find_fragment_in_screenshot(target_path : str, pos : tuple):
    global o
    image = pyautogui.screenshot()
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

    for y in range(image_columns - target_columns):
        for x in range(image_rows - target_rows):
            find = False
            pix = image_px[x, y]
            pix1 = target_px[pos[0], pos[1]]
            if (pix[0], pix[1], pix[2]) == (pix1[0], pix1[1], pix1[2]): 
                find = True
                a =  x
                b =  y

                v = y
                for j in range(pos[1], target_columns + pos[1]):
                    u = x
                    for i in range(pos[0], target_rows + pos[0]):
                        pix = image_px[u, v]
                        pix1 = target_px[i, j]
                        # print((x + u, y + v), (i, j), (pix[0], pix[1], pix[2]), (pix1[0], pix1[1], pix1[2]))
                        # if o == True:
                        #     print ('ggggggggggggggg')
                        #     pyautogui.moveTo(u, v, 0)    
                        if (pix[0], pix[1], pix[2]) != (pix1[0], pix1[1], pix1[2]):
                            find = False
                            break
                        u += 1
                    if find == False:
                        break
                    v += 1

            if find == True:
                return (a + target_rows / 2, b + target_columns / 2)
            
    return (0, 0)
    

def wiq_like():
    global o
    # find chrome_icon
    pos = find_fragment_in_screenshot('chrome_icon.png', chrome_icon_pos)
    if pos != (0,0):
        pyautogui.moveTo(pos[0], pos[1], 2, pyautogui.easeInElastic)
        pyautogui.doubleClick()
    else:
        print("doesn't find chrome_icon.png")
        exit()

    time.sleep(0.5)
    pyautogui.typewrite('wiq.ru/tasks.php', 0.2)
    time.sleep(random.uniform(0.1, 0.5))
    pyautogui.keyDown('enter')
    time.sleep(random.uniform(2.6, 3.99))

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
        like_pos = pos = find_fragment_in_screenshot('do_it_icon.png', do_it_icon_pos)
        t = 0
        while True:
            if pos != (0,0):
                pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
                pyautogui.click()
                break
            else:
                if t > 10:
                    print("doesn't find do_it_icon.png")
                    exit()
                time.sleep(0.6)
                t += 0.6
        time.sleep(4)
        # find like icon
        o = True    

        t = 0
        pos = find_fragment_in_screenshot('like_icon.png', like_icon_pos)
        while True:
            if pos != (0,0):
                pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
                pyautogui.click()
                break
            else:
                if t > 10:
                    print("doesn't find like_icon.png")
                    exit()
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
            time.sleep(3)

# print("hello")
# myScreenshot = pyautogui.screenshot()
# myScreenshot.save(r'file name.png')


wiq_like()



# # image = pyautogui.screenshot()
# # image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
# target = Image.open('like_icon.png')
# # print(type(image), type(target))
# # image_px = image.load()
# target_px = target.load()
# # image_rows = image.width
# # image_columns = image.height
# pos = like_icon_pos
# target_rows = pos[2] - pos[0]
# target_columns = pos[3] - pos[1]


# for j in range(pos[1], target_columns + pos[1]):
#     for i in range(pos[0], target_rows + pos[0]):

#         # print((pix[0], pix[1], pix[2]), (pix1[0], pix1[1], pix1[2]))
#         pyautogui.moveTo(i, j, 0)    


# t = 0
# pos = find_fragment_in_screenshot('like_icon.png', like_icon_pos)
# while True:
#     if pos != (0,0):
#         pyautogui.moveTo(pos[0], pos[1], random.uniform(0.6, 1.2), pyautogui.easeInElastic)
#         pyautogui.click()
#         break
#     else:
#         if t > 10:
#             print("doesn't find like_icon.png")
#             exit()
#         time.sleep(0.6)
#         t += 0.6