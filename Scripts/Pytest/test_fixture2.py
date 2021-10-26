from selenium import webdriver
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture() #scope='class' “function”, “class”, “module”, “session”.
def browser():
    print('browser start for test')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser')
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")

class TestMainPage1():
    #Call fixture like parametr in test
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")