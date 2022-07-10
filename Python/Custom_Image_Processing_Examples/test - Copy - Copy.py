import ctypes
import math
import time
from typing import Optional
import pyautogui
import random
from enum import Enum


def random_sign():
    a = random.randrange(0, 2)
    return -1 if a == 0 else 1

# (x - h)^2 + (y - k)^2 = r^2
# return h, k, r 
def find_circle(x1, y1, x2, y2, x3, y3):
    x12 = x1 - x2
    x13 = x1 - x3
 
    y12 = y1 - y2
    y13 = y1 - y3
 
    y31 = y3 - y1
    y21 = y2 - y1
 
    x31 = x3 - x1
    x21 = x2 - x1
 
    # x1^2 - x3^2
    sx13 = pow(x1, 2) - pow(x3, 2)
 
    # y1^2 - y3^2
    sy13 = pow(y1, 2) - pow(y3, 2)
 
    sx21 = pow(x2, 2) - pow(x1, 2)
    sy21 = pow(y2, 2) - pow(y1, 2)
 
    f = ((sx13) * (x12) + (sy13) * (x12) + (sx21) * (x13) + (sy21) * (x13)) / (2 * ((y31) * (x12) - (y21) * (x13)))
    g = ((sx13) * (y12) + (sy13) * (y12) + (sx21) * (y13) + (sy21) * (y13)) / (2 * ((x31) * (y12) - (x21) * (y13)))
 
    c = -pow(x1, 2) - pow(y1, 2) - 2 * g * x1 - 2 * f * y1;
 
    # eqn of circle be x^2 + y^2 + 2*g*x + 2*f*y + c = 0
    # where centre is (h = -g, k = -f) and radius r
    # as r^2 = h^2 + k^2 - c
    h = -g
    k = -f
    sqr_of_r = h * h + k * k - c
 
    # r is the radius
    r = math.sqrt(sqr_of_r)
    return h, k, r

# y = a*x + b
# return a, b
def find_linear(x1, y1, x2, y2):
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        return a, b

def linear(x, a, b):
    return a * x + b

def quadratic_equation_solution(a, b, c) -> tuple:
    d = b * b - 4 * a * c

    if d > 0:
        return ((-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a))
    else:
        if d == 0:
            return ((-b / (2 * a)), None)
        else:
            return (None, None)

def circle(x, h, k, r) -> tuple:
    a = 1
    b = -2 * k
    c = - r * r + (x - h) * (x - h) + k * k
    return quadratic_equation_solution(a, b, c)

# pyautogui.moveTo(pos[0] -1, pos[1] + 6, random.uniform(0.6, 1.2), pyautogui.easeInElastic)

def mov_func(argument):
    match argument:
        case 0: return pyautogui.easeInCirc,
        case 1: return pyautogui.easeInCubic,
        case 2: return pyautogui.easeInOutQuad,
        case 3: return pyautogui.easeInExpo,
        case 4: return pyautogui.easeInOutBack,
        case 5: return pyautogui.easeInOutBounce,
        case 6: return pyautogui.easeInOutCirc,
        case 7: return pyautogui.easeInOutCubic,
        case 8: return pyautogui.easeInOutElastic,
        case 9: return pyautogui.easeInOutExpo,
        # case 10: return pyautogui.easeInElastic,

# X or Y parameter to bring to the screen
def bring_to_screen(pos: int, screen_res : int):
    if pos < 0:
        pos = 1
    if pos > screen_res:
        pos = screen_res - 1
    return(pos)


def get_inside_epsilion_env(x, y, height, width, eps : int = 100):
    x = x + random.randrange(-eps, eps)
    y = y + random.randrange(-eps, eps)
    x = bring_to_screen(x, width)
    y = bring_to_screen(y, height)
    return x, y

def mouse_move_to(x1, y1):
    width = pyautogui.size()[0]
    height = pyautogui.size()[1]

    current_pos = pyautogui.position()
    x0 = current_pos[0]
    y0 = current_pos[1]

    # offsetX, offsetY = get_inside_epsilion_env(x1, y1, height, width)

    # dir = -1 if x0 > offsetX else 1

    # distance = math.sqrt((x0 - offsetX) ** 2 + (y0 - offsetY) ** 2)

    # a, b = find_linear(x0, y0, offsetX, offsetY)


    # sign = random_sign()

    # offsetB : int = b + sign * distance / random.randrange(6, 17)

    # x2 = (x0 + offsetX) / 2
    # y2 = (x0 + offsetY) / 2 + offsetB

    # h, k, r = find_circle(x0, y0, offsetX, offsetY, x2, y2)

    # pixCountX = abs(x0 - offsetX)
    # x = x0
    # for i in range(pixCountX):
    #     values = circle(x, h, k, r)
    #     if values[0] == None:
    #         break
    #     if (sign == 1 and values[0] > linear(x, a, b)) or (sign == -1 and values[0] < linear(x, a, b)):
    #         y = values[0]
    #     else:
    #         y = values[1]
    #     x = x + dir
    #     # print(x, int(y))
    #     ctypes.windll.user32.SetCursorPos(x, int(y))
    #     time.sleep(0.00001)
    # pyautogui.moveTo(x1, y1, 0.3, pyautogui.easeInOutBounce)
    

    if x0 > x1:
        dir = -1
        offsetX = x1 - random.randrange(0, x1) / 10
    else:
        dir = 1
        offsetX = width - random.randrange(x1, width) / 10

    a = (y1 - y0) / (x1 - x0)
    b = y0 - a * x0

    wrongPosCount = random.randrange(1, 6)
    step = abs(x0 - x1) / (wrongPosCount)
    timeStep = random.uniform(0.3, 0.7) / (wrongPosCount + 1)

    for i in range(wrongPosCount - 1):
        u = int(x0 + (i + 1) * step * dir)
        v = int(bring_to_screen(a * u + b + random.randrange(-40, 40), height))
        argument = random.randrange(0, 11)
        print(argument)
        func = mov_func(argument)[0]
        print(type(func))
        pyautogui.moveTo(u, v, timeStep, func, False, True)
    argument = random.randrange(0, 11)
    func = mov_func(argument)[0]
    u, v = get_inside_epsilion_env(x1, y1, width, height)
    pyautogui.moveTo(u, v, timeStep, pyautogui.easeInElastic)
    pyautogui.moveTo(x1, y1, timeStep, pyautogui.easeInElastic)

    


# cars = []

# cars.append("he")
# cars.append("be")

# for x in cars:
#     print(x)

# mouse_move_to((100, 560))


# pyautogui.moveTo(30, 100, 1, pyautogui.easeInCirc)


# print('Press Ctrl-C to quit.')

# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)

# except KeyboardInterrupt:
#     print('\nDone.')



# # time.sleep(1)
# # mouse_move_to(100, 100)

# from pywinauto import Application

# chrome_dir = r'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
# # tab_log_in = u'Meet Google Drive - One place for all your files (Incognito)'
# # tab_drive = 'My Drive - Google Drive (Incognito)'

# # # start google chrome
# # chrome = Application(backend='uia')
# # chrome.start(chrome_dir + ' --force-renderer-accessibility --start-maximized '
# #              'https://www.instagram.com/azat_tonoyan/')


# app = Application()
# app.start(chrome_dir + ' --force-renderer-accessibility --start-restore ' 'https://www.instagram.com/azat_tonoyan/')
# dlg_spec = app.window()
# dlg_spec.move_window(x=100, y=100, width=600, height=400, repaint=True)





t = time.time()

a = pyautogui.screenshot()
x = a.load()
v = 0
for i in range(0, a.height, 0.1):
    for j in range(0, a.width, 0.1):
        
        v += 1
print(1/(time.time() - t))
print(v)