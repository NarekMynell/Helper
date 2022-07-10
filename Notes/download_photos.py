import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import re
import os
import random
import urllib.request

login = "+37493303327"
password = "asdewq-123456"
count = 1
saving_folder = 'C:\\Users\\narek\\Bot\\Accounts_photos\\Armenian\\Boys\\'
URLs_path = 'C:\\Users\\narek\\Bot\\Accounts_photos\\Armenian\\boys_links.txt'
page_link = 'https://vk.com/search?c%5Bcountry%5D=6&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Bsex%5D=2'

def saving_photos(photos, name):
    global count
    if count > 2000:
        driver.quit()
    size = 20 + random.randrange(20)
    saving_path = saving_folder + str(count) + '  ' + name
    os.mkdir(saving_path)
    i = 1
    for photo in photos:
        if i > size:
            break
        uncorrect_url = photo.value_of_css_property("background-image")
        url = uncorrect_url[5 : len(uncorrect_url) - 2]
        new_name = saving_path + '\\' + str(i) + '.jpg'
        urllib.request.urlretrieve(url, new_name)
        i += 1
        time.sleep(0.5)
    count +=1

def availability_check(url):
    with open(URLs_path, 'r') as the_file:
        for line in the_file:
            # For each line, check if line contains the string
            if url in line:
                return True
    return False

def saving_url(url):
    with open(URLs_path, 'a') as the_file:
        the_file.write(url + '\n')


driver = webdriver.Firefox()
driver.get("https://vk.com")
driver.find_element_by_id("index_email").send_keys(login)
driver.find_element_by_id("index_pass").send_keys(password)
driver.find_element_by_id("index_login_button").click()
time.sleep(8)
driver.get(page_link)
time.sleep(2)
items = None
accounts_count = 0
while accounts_count < 950:    
    items = driver.find_elements_by_class_name('search_item_img')
    accounts_count = len(items)
    driver.execute_script("window.scrollBy(0,5000)","")
    print("accaunts count = " + str(accounts_count))
    time.sleep(1)
print(len(items))

URLs = []
accounts_count = 1
for item in items:
    URLs.append(item.find_element_by_xpath('..').get_attribute("href"))

for url in URLs: 
    print(accounts_count)
    print(url)
    accounts_count +=1    
    if availability_check(url) == True:
        continue
    driver.get(url)
    time.sleep(1.5)
    tabs = driver.find_elements_by_class_name('page_counter')
    photos_count = -1

    photos_page = None
    for tab in tabs:
        if tab.text.find("фотографи") != -1:
            photos_count = int(re.search(r'\d+', tab.text).group())
            photos_page = tab
    name = None
    if photos_count > 9:
        name = driver.find_element_by_class_name('page_name').text
        try:
            photos_page.click()
        except:
            print("errorik") 
            continue   
        waiting_time = 10 - 1 / (photos_count * 0.013)
        time.sleep(waiting_time)
        photos = driver.find_elements_by_class_name('photos_row')         
        try:  
            saving_photos(photos, name)
            saving_url(url)
        except:
            print("error")                 
    #driver.execute_script("window.history.go(-1)")
    
