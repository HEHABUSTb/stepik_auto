from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/registration1.html'
    link ='http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #Fill required field
    first_name = browser.find_element_by_css_selector('input.form-control.first')
    first_name.send_keys('Ivan')
    time.sleep(1)
    last_name = browser.find_element_by_css_selector('input.form-control.second')
    last_name.send_keys('Last name')
    time.sleep(1)
    email = browser.find_element_by_css_selector('input.form-control.third')
    email.send_keys('Email')
    time.sleep(1)
    
    #Send filled field 
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    #Check, we passed registration
    #Wait page loading
    time.sleep(1)

    #Find element, contains text
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    # Write in variable welcome_text text from element welcome_text_elt
    welcome_text = welcome_text_elt.text

    #With help assert check, what we succes
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Wait for visiable check succes of the script
    time.sleep(5)
    # Terminate browser
    browser.quit()

