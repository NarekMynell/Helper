import cv2
import numpy as np

# Կարդումա մեծ նկարը
image= cv2.imread('Rainforest.png')
# Ցուցադրումա
cv2.imshow('Rainforest', image)
# Սպասումա փակոլուն
cv2.waitKey(0)
# Տալիսա մոխրագույն երանգ, որ հեշտ լինի փնտրելը
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Կարդումա որոնվող նկարը
template= cv2.imread('Yellowing-leaf.png',0)

# Կատարումա որոնում
result= cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
# max_loc-ը գտած մասի վերևի ձախ անկյունի կոորդինատնա
min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)

height, width= template.shape[:2]

top_left= max_loc
bottom_right= (top_left[0] + width, top_left[1] + height)
# Գծումա կվադրատ գտած մասի շուրջը
cv2.rectangle(image, top_left, bottom_right, (0,0,255),5)

cv2.imshow('Rainforest', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
