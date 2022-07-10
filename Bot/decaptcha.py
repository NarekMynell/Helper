import os
import random
import urllib.request
from selenium import webdriver
from operator import itemgetter
from subprocess import check_output
import time
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller

from PIL import Image
import pytesseract as tess
from PIL._imaging import display
from selenium.webdriver.common.action_chains import ActionChains
import copy
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
keyboard = Controller()


def get_captchas_numbers():
    number_0_0 = [4, 5, 6, 7, 8, 9, 10]
    number_0_1 = [2, 3, 9, 10, 11, 12]
    number_0_2 = [0, 1, 12, 13, 14]
    number_0_3 = [0, 1, 14, 15]
    number_0_4 = [0, 16]
    number_0_5 = [0, 1, 17]
    number_0_6 = [1, 2, 17]
    number_0_7 = [2, 3, 4, 16]
    number_0_8 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    number_1_0 = [17]
    number_1_1 = [0, 1, 17]
    number_1_2 = [0, 1, 14, 15, 16, 17]
    number_1_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    number_1_4 = [16]
    number_1_5 = [16]
    number_1_6 = [17]

    number_2_0 = [5]
    number_2_1 = [2, 3, 19, 20]
    number_2_2 = [1, 18, 19]
    number_2_3 = [0, 17, 18, 19]
    number_2_4 = [0, 1, 16, 17, 18, 19]
    number_2_5 = [1, 2, 15, 16, 19]
    number_2_6 = [2, 3, 4, 13, 14, 19]
    number_2_7 = [5, 6, 7, 8, 9, 10, 11, 12, 19]
    number_2_8 = [19]
    number_2_9 = [18]
    number_2_10 = [18]
    number_2_11 = [18]

    number_3_0 = [0, 1]
    number_3_1 = [0, 1]
    number_3_2 = [0, 1, 2]
    number_3_3 = [0, 1, 2, 9, 16]
    number_3_4 = [0, 1, 2, 8, 9, 10, 15, 16]
    number_3_5 = [1, 2, 7, 8, 9, 10, 14, 15, 16]
    number_3_6 = [2, 3, 7, 8, 9, 10, 14, 15]
    number_3_7 = [4, 5, 6, 10, 11, 12, 14]
    number_3_8 = [11]

    number_4_0 = [7, 8]
    number_4_1 = [5, 8]
    number_4_2 = [8]
    number_4_3 = [2, 8]
    number_4_4 = [1, 8]
    number_4_5 = [0, 8]
    number_4_6 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    number_4_7 = [7, 17]

    number_5_0 = [3]
    number_5_1 = [2, 3, 4]
    number_5_2 = [2, 3, 4, 5, 6]
    number_5_3 = [1, 2, 7, 8, 16]
    number_5_4 = [1, 8, 15, 16]
    number_5_5 = [1, 8, 9, 16]
    number_5_6 = [1, 8, 9, 16]
    number_5_7 = [0, 1, 8, 9, 16]
    number_5_8 = [0, 1, 8, 9, 16]
    number_5_9 = [0, 1, 9, 15, 16]
    number_5_10 = [0, 1, 9, 10, 11, 12, 13, 14]
    number_5_11 = [0, 1, 10, 11, 12, 13]

    number_6_0 = [12, 13, 14, 15, 16, 17]
    number_6_1 = [7, 8, 9, 10, 15, 16, 17]
    number_6_2 = [5, 6, 17]
    number_6_3 = [3, 4, 17]
    number_6_4 = [1, 2, 3, 17]
    number_6_5 = [0, 1, 2, 13, 17]
    number_6_6 = [0, 1, 12, 17, 18]
    number_6_7 = [12, 17, 18]
    number_6_8 = [12, 13, 16, 17]
    number_6_9 = [13, 14, 15, 16]
    number_6_10 = [14, 15]

    number_7_0 = [0, 1]
    number_7_1 = [0, 1]
    number_7_2 = [0]
    number_7_3 = [0]
    number_7_4 = [0, 16, 17]
    number_7_5 = [0, 13, 14, 15, 16, 17]
    number_7_6 = [0, 10, 11, 12, 13, 14]
    number_7_7 = [0, 6, 7, 8, 9]
    number_7_8 = [0, 3, 4, 5]
    number_7_9 = [0, 1, 2]
    number_7_10 = [0]

    number_8_0 = [3, 4, 5, 6, 14, 15]
    number_8_1 = [1, 2, 11, 12]
    number_8_2 = [1, 9, 10, 11]
    number_8_3 = [0, 9, 10, 18]
    number_8_4 = [0, 9, 10, 19]
    number_8_5 = [0, 9, 20]
    number_8_6 = [0, 9, 20]
    number_8_7 = [1, 9, 19]
    number_8_8 = [2, 3, 8, 9]
    number_8_9 = [4, 5, 6, 9, 10, 18]
    number_8_10 = [6, 11, 12, 13, 14, 16]
    number_8_11 = [14, 15]

    number_9_0 = [4, 5, 6, 7]
    number_9_1 = [3, 4, 8]
    number_9_2 = [2, 9]
    number_9_3 = [1, 2]
    number_9_4 = [0, 1, 10]
    number_9_5 = [0, 10]
    number_9_6 = [0, 10, 15, 16, 17]
    number_9_7 = [0, 9, 10, 12, 13, 14, 15]
    number_9_8 = [0, 1, 4, 5, 6, 7, 8, 9, 10, 11]
    number_9_9 = [0, 1, 2, 3, 4, 5, 6]

    number_0 = [number_0_0, number_0_1, number_0_2, number_0_3, number_0_4, number_0_5, number_0_6, number_0_7, number_0_8]
    number_1 = [number_1_0, number_1_1, number_1_2, number_1_3, number_1_4, number_1_5, number_1_6]
    number_2 = [number_2_0, number_2_1, number_2_2, number_2_3, number_2_4, number_2_5, number_2_6, number_2_7, number_2_8, number_2_9, number_2_10, number_2_11]
    number_3 = [number_3_0, number_3_1, number_3_2, number_3_3, number_3_4, number_3_5, number_3_6, number_3_7, number_3_8]
    number_4 = [number_4_0, number_4_1, number_4_2, number_4_3, number_4_4, number_4_5, number_4_6, number_4_7]
    number_5 = [number_5_0, number_5_1, number_5_2, number_5_3, number_5_4, number_5_5, number_5_6, number_5_7, number_5_8, number_5_9, number_5_10, number_5_11]
    number_6 = [number_6_0, number_6_1, number_6_2, number_6_3, number_6_4, number_6_5, number_6_6, number_6_7, number_6_8, number_6_9, number_6_10]
    number_7 = [number_7_0, number_7_1, number_7_2, number_7_3, number_7_4, number_7_5, number_7_6, number_7_7, number_7_8, number_7_9, number_7_10]
    number_8 = [number_8_0, number_8_1, number_8_2, number_8_3, number_8_4, number_8_5, number_8_6, number_8_7, number_8_8, number_8_9, number_8_10, number_8_11]
    number_9 = [number_9_0, number_9_1, number_9_2, number_9_3, number_9_4, number_9_5, number_9_6, number_9_7, number_9_8, number_9_9]

    numbers = [(18, number_0), (18, number_1), (21, number_2), (17, number_3), (18, number_4), (17, number_5), (19, number_6), (18, number_7), (21, number_8), (18, number_9)]
    return numbers

def image_cleaning(image):
    row = image.size[1]
    column = image.size[0]
    colorsTable = {}
    for i in range(column):
        for j in range(row):
            pixel = im.getpixel((i,j))
            if colorsTable.get(pixel) == None:
                colorsTable[pixel] = 1
            else:
                colorsTable[pixel] += 1

    backCount = 0
    textCount = 0
    backColor = None
    textColor = None
    for x in colorsTable:
        item = colorsTable[x]
        if item > backCount:
            backCount = item
            backColor = x
    for x in colorsTable:
        item = colorsTable[x]
        if item > textCount and x != backColor:
            textCount = item
            textColor = x

    pixels = image.load()
    for i in range(column):
        for j in range(row):
            if pixels[i,j] == textColor:
                pixels[i,j] = (0,0,0)
            else:
                pixels[i,j] = (255,255,255)
    return image

def get_first_painted_column(image):
    pixels = image.load()
    row = image.size[1]
    column = image.size[0]
    first_painted_column = -1
    for i in range(column):
        has_paint = False
        for j in range(row):
            if pixels[i, j] != (255,255,255):
                has_paint = True
        if has_paint == True:
            first_painted_column = i
            break
    return first_painted_column

def is_empty(image, lenght):
    paints_count = 0
    row = image.size[1]
    pixels = image.load()
    for i in range(lenght):
        for j in range(row):
            if pixels[i,j] != (255,255,255):
                paints_count += 1
    if paints_count < 2:
        return True
    else:
        return False

im = Image.open('C:\\Users\\narek\\Downloads\\2.png')
im = image_cleaning(im)

numbers = get_captchas_numbers()
image = im
pixels = image.load()
pixels1 = image.load()
first_painted_column = get_first_painted_column(im)

for o in range(5):
    first_painted_column = get_first_painted_column(image)   
    # print(first_painted_column)
    
    break_condision = False
    while break_condision == False:
        u = 0
        for x in numbers:
            height = x[0]
            lenght = len(x[1])
            h = 0
            while h + height < 35:
                imo = copy.copy(image)
                pixels = imo.load()
                for i in range(len(x[1])):
                    for j in range(len(x[1][i])):
                        pixels[i+first_painted_column,x[1][i][j]+h] = (255,255,255)
                h += 1
                if is_empty(imo, first_painted_column + lenght):
                    print(u)
                    break_condision = True
                    image = copy.copy(imo)
                    break
            if break_condision:
                break
            u += 1
        first_painted_column -= 1
    # image.show()






# # #pix_vall = list(im.getdata()) # get all pixels

# # im = im.convert("P")
# # his = im.histogram()
# # values = {}

# # for i in range(256):
# #     values[i] = his[i]

# # colors = []

# # for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:2]:
# #     colors.append(j)
	
# # pixels = im.load() # creates the pixel map

# # for i in range(im.size[0]):    
# #     for j in range(im.size[1]): 
# #         pixel = pixels[i, j]
# #         if pixel != (colors[0]) and pixel != (colors[1]):
# #             pixels[i, j] = (colors[0])

# # im.show()
# # #im.save('C:\\Users\\narek\\Desktop\\captcha.png')

# # text = tess.image_to_string(im)
# # print(text)










# driver = webdriver.Chrome()
# driver.get('https://instagram777.ru/login.php')
# time.sleep(1)
# btn = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div[1]/div/div/form/div[1]/div[3]/span')
# captcha = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div[1]/div/div/form/div[1]/div[3]/img')
# # btn.click()
# # time.sleep(0.5)
# # i = 1
# # # while True:
# # #     print(i)
# # #     print(captcha.get_attribute('src'))
# # #     btn.click()
# # #     i += 1

# #urllib.request.urlretrieve(captcha.get_attribute('src'), 'C:\\Users\\narek\\Desktop\\captcha.png')

# # action chain object creation
# action = ActionChains(driver)
# # right click operation and then perform
# action.context_click(captcha).perform()
# time.sleep(0.5)
# for i in range(5):
#     keyboard.press (Key.down)
#     time.sleep(0.5)
# keyboard.press(Key.enter)