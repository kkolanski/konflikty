from selenium import webdriver
import unittest
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """Klasa bazowa każdego testu"""
    def setUp(self):
        """Warunki wstępne każdego testu"""
        # Otwarcie przeglądarki
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        # Jesteśmy na stronie głównej - tworzę instancję klasy HomePage
        # Muszę zaimportować niezbędną klasę
        # Tworzę obiekt tej klasy
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
