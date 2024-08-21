import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/get_attribute.html"


def calculate(x):
    return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element(By.ID, 'treasure')
        x = x_element.get_attribute('valuex')

        result = calculate(x)

        input_value = browser.find_element(By.ID, "answer")
        input_value.send_keys(result)

        option1 = browser.find_element(By.ID, "robotCheckbox")
        option1.click()

        option2 = browser.find_element(By.ID, "robotsRule")
        option2.click()


        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)


    finally:
        time.sleep(10)
        browser.quit()