from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return math.log(abs(12*math.sin(int(x))))
try:
    link =  'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Find value and calculate math function
    x = browser.find_element_by_css_selector('span#input_value').text
    y = calc(x)
    y = str(y)

    # Execute script to scroll page
    button = browser.find_element_by_css_selector('button')
    browser.execute_script("window.scrollBy(0, 100);")

    #Type the answer
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    #Select the first checkbox
    checkbox = browser.find_element_by_id('robotCheckbox').click()
    #Click on radio button
    radio  = browser.find_element_by_id('robotsRule').click()

    #Send the answer
    submit = browser.find_element_by_css_selector('button').click()


finally:
    time.sleep(5)
    browser.quit()
