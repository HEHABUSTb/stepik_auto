from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
