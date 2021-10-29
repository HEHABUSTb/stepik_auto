import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTimer:

    @pytest.fixture()  # scope='class' “function”, “class”, “module”, “session”.
    def browser(self):
        print('browser start for test')
        browser = webdriver.Chrome()
        yield browser
        print('\nquit browser')
        #browser.quit()

    result = []
    links = ['https://stepik.org/lesson/236895/step/1','https://stepik.org/lesson/236896/step/1',
             'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
             'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
             'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']

    @pytest.mark.parametrize('links', links)
    def test_parametr(self, browser, links):
        link = f"{links}"
        browser.implicitly_wait(10)
        browser.get(link)
        text_area = browser.find_element_by_css_selector("textarea")
        text_area.send_keys(str(math.log(int(time.time()))))
        time.sleep(1)

        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        button.click()
        message = browser.find_element_by_class_name('smart-hints__hint').text
        print('\n', message)
        if message != 'Correct!':
            self.result.append(message)
            print('\n', self.result)
        time.sleep(1)
