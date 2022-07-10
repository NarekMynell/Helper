## Instalation in windows
1. Download python
*install անելուց custum setting տանք, որ միանգամից **pip**-ն էլ ինթոլ անենք ու նաև պաթև տանք*
2. Set path
> Windows-ի որոնման դաշտում գտնում ենք փայթնի էքսեշնիկը ու իրանով կոդ ենք գրում, կամ էլ ստանդարտ քմանդ լայնում գրում ենք python ու էլի կոդ գրում
 ## Packages
 * **OpenCV** (Image Processing)
    ```pip install opencv-python```
 * **pyautogui** (control the mouse and keyboard to automate interactions)
    ```pip install pyautogui```
* **[turtle](https://realpython.com/beginners-guide-python-turtle/)** (փեքիջ, որտող բացվումա պատուհան ու գրաֆիկական ներկայացնումա կոդը)
* **PIL** (նկարների հետ աշխատանքի գրադարան)

## [Pyautogui](https://pyautogui.readthedocs.io/en/latest/)
~~~python
>>> import pyautogui

>>> screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
>>> screenWidth, screenHeight
(2560, 1440)

>>> currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
>>> currentMouseX, currentMouseY
(1314, 345)

>>> pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

>>> pyautogui.click()          # Click the mouse.
>>> pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
>>> pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

>>> pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
>>> pyautogui.doubleClick()     # Double click the mouse.
>>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

>>> pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
>>> pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

>>> with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
        pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
>>> # Shift key is released automatically.

>>> pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

>>> pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.
~~~
**Կտպի մկնիկի կոորդինատը անվերջ ցիկլում**
~~~python
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
~~~

## PIL
**Սքրինշոթ կանի բոլոր էկրանները**
~~~
screenshot = ImageGrab.grab(None, False, True)
screenshot.show() 
~~~
**Կտա էկրանի համապատասխան պիքսելի գույնը**
~~~
import PIL.ImageGrab
rgb = PIL.ImageGrab.grab().load()[10, 20]
~~~