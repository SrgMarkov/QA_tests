import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x1 = browser.find_element(By.ID, 'num1')
        x2 = browser.find_element(By.ID, 'num2')
        answer = int(x1.text) + int(x2.text)

        select = Select(browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value(str(answer))

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)


    finally:
        time.sleep(10)
        browser.quit()