import os
from selenium import webdriver
import time 



try:
    
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #Fill a fields
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Alex')

    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Ivanov')

    email = browser.find_element_by_name('email')
    email.send_keys('abs@example')

    #download txt file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(current_dir, 'text.txt')

    download = browser.find_element_by_id('file')
    print(file)
    download.send_keys(file)

    #Click on the submit button
    button = browser.find_element_by_css_selector('button').click()
    

    



finally:
    time.sleep(5)
    browser.quit()
    


