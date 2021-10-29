import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support import expected_conditions as EC


class TestTimer:

    @pytest.fixture()  # scope='class' “function”, “class”, “module”, “session”.
    def browser(self):
        print('browser start for test')
        browser = webdriver.Chrome()
        yield browser
        print('\nquit browser')
        browser.quit()

    result = []
    link = 'https://stepik.org/lesson/236895/step/1'


    def test_parametr(self, browser):
        link = 'https://stepik.org/lesson/236895/step/1'

        browser.get(link)
        browser.implicitly_wait(10)
        text_area = browser.find_element_by_css_selector('textarea')
        text_area.send_keys(str(math.log(int(time.time()))))