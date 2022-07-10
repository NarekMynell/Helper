import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import re
import os
import random
import urllib.request

url = 'https://scontent.fevn6-1.fna.fbcdn.net/v/t1.0-9/118772983_10218390708619878_3280720641925595352_o.jpg?_nc_cat=106&_nc_sid=730e14&_nc_ohc=wH0GO-SrEKgAX8KK7gW&_nc_ht=scontent.fevn6-1.fna&oh=f7cb65bf64bd0a7a5c71a2716140066e&oe=5FB2E9D9'
new_name ='C:\\Users\\narek\\Desktop\\tutak.jpg'
urllib.request.urlretrieve(url, new_name)