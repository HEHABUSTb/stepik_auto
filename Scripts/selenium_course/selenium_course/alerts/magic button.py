from selenium import webdriver 
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #push magic button
    button = browser.find_element_by_css_selector('button').click()

    #switch to second page
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #calculate answer x
    x = browser.find_element_by_id('input_value').text
    x = calc(x)
    print(x)

    #put and send answer
    answer = browser.find_element_by_id('answer').send_keys(x)
    submit = browser.find_element_by_css_selector('button').click()


finally:
    time.sleep(5)
    browser.quit()
