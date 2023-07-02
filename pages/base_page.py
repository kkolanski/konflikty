from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    """
    Klasa bazowa, z której będą korzystały wszystkie strony (pages)
    """
    def __init__(self, driver):
        self.driver = webdriver
        self._verify_page()
        self.alert = Alert(self.driver)

    def _verify_page(self):
        """Autotest strony - utuchamiany automatycznie po wejściu na nią"""
        return
