import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calculate(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

first_button = browser.find_element(By.CLASS_NAME, 'btn')
first_button.click()

alert = browser.switch_to.alert
alert.accept()


x_element = browser.find_element(By.ID, 'input_value')
result = calculate(x_element.text)

input_value = browser.find_element(By.ID, "answer")
input_value.send_keys(result)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
