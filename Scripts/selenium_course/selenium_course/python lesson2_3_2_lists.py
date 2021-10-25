from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()
browser.get(link)

#Find x and y 
x = browser.find_element_by_id('num1').text
y = browser.find_element_by_id('num2').text
answer = int(x) + int(y)

#Find and choose answer in droplist
select = Select(browser.find_element_by_id('dropdown'))
select.select_by_value(str(answer)) 

#Send the answer
submit = browser.find_element_by_css_selector('button').click()







time.sleep(3)
browser.quit()
