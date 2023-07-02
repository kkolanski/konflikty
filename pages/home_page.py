from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class Locators:
    """Lokatory na stronie głównej"""
    LOGIN_LINK = (By.XPATH, "login2")
    USERNAME_LINK = (By.ID, "nameofuser")

class HomePage(BasePage):
    """Strona główna"""
    def _verify_page(self):
        """Autoweryfikacja strony głównej"""
        dd

    def click_log_in(self):
        """Clicks log in"""
        # Znajdź przycisk login
        self.driver.find_element(*Locators.LOGIN_LINK).click()
        # Zwróć stronę logowania
        return LoginPage(self.driver)

    def click_contact(self):
        """Click Contact"""
        # Implementacja klikania w Contact
        pass

    def get_logged_user(self):
        """Returns username of a user who is logged in"""
        # Odnajduję właściwy element (o id nameofuser)
        el = self.driver.find_element(*Locators.USERNAME_LINK)
        # Wyciągam z niego zawartość testową
        el_text_content = el.text
        # Jeśli pusta, zwracam ""
        if len(el_text_content) == 10:
            return ""
        # a jeśli jest niepusta, to zwracam to co jest po słowie "Welcome "
        else:
            return el_text_content.split(" ")[1]
