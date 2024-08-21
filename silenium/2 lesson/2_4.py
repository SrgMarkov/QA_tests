import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

elems = ['Сергей', 'Марков', 'markov@test.by']

name = browser.find_element(By.NAME, 'firstname')
second_name = browser.find_element(By.NAME, 'lastname')
email = browser.find_element(By.NAME, 'email')

name.send_keys(elems[0])
second_name.send_keys(elems[1])
email.send_keys(elems[2])

upload = browser.find_element(By.ID, 'file')
upload.send_keys(file_path)

button = browser.find_element(By.CLASS_NAME, 'btn')
button.click()

time.sleep(10)
