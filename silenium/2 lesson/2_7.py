import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calculate(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button = browser.find_element(By.ID, "book")
button.click()

x_element = browser.find_element(By.ID, 'input_value')
result = calculate(x_element.text)

input_value = browser.find_element(By.ID, "answer")
input_value.send_keys(result)

button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(10)
