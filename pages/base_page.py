from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, CartPageLocators
import math

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # неявное ожидание

    # метод для проверки наличия элемента
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)