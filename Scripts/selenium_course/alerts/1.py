from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #Push button
    button = browser.find_element_by_css_selector('button').click()

    #Accept alert
    alert = browser.switch_to.alert
    alert.accept()

    #calculate x
    x = browser.find_element_by_id('input_value').text
    x = calc(x)

    #Send answer
    answer = browser.find_element_by_id('answer')
    answer.send_keys(x)

    #Submit answer
    submit = browser.find_element_by_css_selector('button').click()


finally:
    time.sleep(5)
    browser.quit()
