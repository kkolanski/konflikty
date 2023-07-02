from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class Locators:
    """Lokatory strony logowania"""
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[@onclick='logIn()']")
    # Jeszcze Close - Będzie zabawa :)

class LoginPage(BasePage):
    """Strona logowania"""
    def _verify_page(self):
        # Poczekaj, aż inputy (username oraz password) będą dostępne
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located(Locators.USERNAME_INPUT))
        wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))

    def enter_username(self, username):
        """Enters username"""
        # Znaleźć element (będę potrzebował do tego lokatora)
        # self.driver.find_element(..
        el = self.driver.find_element(*Locators.USERNAME_INPUT)
        # Wpisać username
        el.send_keys(username)

    def enter_password(self, password):
        """Enters password"""
        # Znaleźć element (będę potrzebował do tego lokatora)
        # self.driver.find_element(..
        el = self.driver.find_element(*Locators.PASSWORD_INPUT)
        # Wpisać
        el.send_keys(password)

    def click_log_in(self):
        """Clicks Log in"""
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

    def get_alert_message(self):
        """ Gets alert message"""
        # Zamiast spać, poczekamy na alerta
        # Zastosujmy mechanizm explicit wait
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.alert_is_present())
        return self.alert.text

    def click_cancel(self):
        pass