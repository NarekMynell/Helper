import selenium
from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


saving_path = "C:\\Users\\narek\\Bot\\Mails\\Armenian\\boys.txt"
names_path = "C:\\Users\\narek\\Desktop\\armenian_boys_names.txt"
surnames_path = "C:\\Users\\narek\\Desktop\\armenian_surnames.txt"
keywords_path = "C:\\Users\\narek\\Desktop\\names_of_musicians.txt"
names = []
surnames = []
keywords = []
sign = ['_', '.']
name = ""
surname = ""
login = ""
password = ""
answer = ""
#driver = webdriver.Firefox()
#driver1 = webdriver.Firefox()

with open(names_path, "r") as f:
   for line in f:
       names.append(line)

with open(surnames_path, "r") as f:
   for line in f:
       surnames.append(line)

with open(keywords_path, "r") as f:
    for line in f:
        keywords.append(line)

names_count = len(names)-1
surnames_count = len(surnames)-1 
musicians_count = len(keywords)-1  


def registration():
    global name
    global surname
    global login
    global password
    global answer
    driver = webdriver.Firefox()
   # driver2 = driver
    driver.get("https://passport.yandex.com/registration/mail?from=mail&require_hint=1&origin=hostroot_homer_reg_com&retpath=https%3A%2F%2Fmail.yandex.com%2F%3Fnoretpath%3D1&backpath=https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1")

    name = names[random.randrange(names_count)]
    surname = surnames[random.randrange(surnames_count)]
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[1]/span/input").send_keys(name)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[2]/span[1]/input").send_keys(surname)

    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[3]").click()
    time.sleep(3)

    login = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/ul/li[1]/label").text
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[1]/div[3]/span/input").send_keys(login)
    password = login
    password += sign[random.randrange(2)]
    password += str(1000 + random.randrange(99000))
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[2]/div[1]/span/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[2]/div[2]/span/input").send_keys(password)

    # to click "I don't have a phone number" text
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[1]").click()

    # to answer the question
    answer = keywords[random.randrange(musicians_count)]
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[1]/div[2]/span/input").send_keys(answer)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div[2]/div/div[2]/div").click()
    return driver

def saving_data():
    with open(saving_path, "a") as f:
        f.write(name + surname + login + '\n' + password + '\n' + answer + '\n')



driver1 = registration()
saving_data()
driver2 = registration()
saving_data()
driver3 = registration()
saving_data()

while True:
    try:
        while True:
            determinant = 1
            driver1.current_url
            determinant = 2
            driver2.current_url
            determinant = 3
            driver3.current_url
            time.sleep(0.2)
    except WebDriverException:
        if(determinant == 1):
            driver1 = registration()
            saving_data()
        else:
            if (determinant == 2):
                driver2 = registration()
                saving_data()
            else:
                driver3 = registration()
                saving_data()
           


