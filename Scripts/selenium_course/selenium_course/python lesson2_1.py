from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #Calculate y for answer
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    #Fill the answer fields
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    #Click on checkbox 
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    
    #Click on radio 
    radio  = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    #Send the answer
    button = browser.find_element_by_css_selector('button')
    button.click()
    
finally:
    time.sleep(5)
    browser.quit()
