from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)


    #wait until price drop down
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    print('Price drop down to $100')
    book = browser.find_element_by_id('book').click()

    #Calculate and send answer
    x = browser.find_element_by_id('input_value').text
    x = calc(x)
    answer = browser.find_element_by_id('answer').send_keys(x)
    submit = browser.find_element_by_id('solve').click() 
    
  
finally:
    time.sleep(5)
    browser.quit()

