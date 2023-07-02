from tests.base_test import BaseTest
from tests.test_data import ValidLoginCredentials
from time import sleep
from ddt import ddt, data, unpack
import csv
import unittest

from tests.test_data import TestData


def get_login_data_from_csv(filename):
    """ get login data from csv file"""
    rows = []
    data_file = open(filename, "r")
    reader = csv.reader(data_file)
    for row in reader:
        rows.append(row)
    return rows


@ddt
class LoginTest(BaseTest):
    """Testy logowania się"""
    def setUp(self):
        # Chciałbym użyć metody setUp z BaseTest,
        # ale dodatkowo jeszcze kliknąć login
        # super() - zwraca instancję nadklasy
        # umożliwia wywołanie metody z klasy bazowej
        super().setUp()
        self.login_page = self.home_page.click_log_in()
        self.test_data = TestData()

    @data(*get_login_data_from_csv("valid_login_credentials.csv"))
    @unpack
    def test_log_in_with_valid_credentials(self, username, password):
        """Logowanie przy użyciu poprawnych danych. Zastosowanie DDT"""
        # Warunki wstępne:
        # Otwórz przeglądarkę na stronie głównej
        # ( Już zaimplementowane w BaseTest )

        # Kroki:
        # # 1. Kliknij Login
        # login_page = self.home_page.click_log_in()
        # 2. Wpisz poprawny username
        self.login_page.enter_username(username)
        # 3. Wpisz poprawny password
        self.login_page.enter_password(password)
        # 4. Kliknij LogIn
        self.login_page.click_log_in()
        # Sprawdź, czy się udało zalogować
        # (czy nazwa użytkownika na stronie jest taka sama jak wcześniej wpiswana )
        # Tutaj trzeba będzie chwilę poczekać (do przemyślenia jak) - Webdriver Wait
        sleep(12)
        self.assertEqual(username, self.home_page.get_logged_user())

    def test_invalid_username(self):
        """ BEZ DDT"""
        # Kroki:
        # # 1. Kliknij Login
        # login_page = self.home_page.click_log_in()
        # 2. Wpisz niepoprawny username
        self.login_page.enter_username(self.test_data.user_name)
        # 3. Wpisz poprawny password
        self.login_page.enter_password(ValidLoginCredentials.password)
        # 4. Kliknij LogIn
        self.login_page.click_log_in()
        # 5. Sprawdź, czy użytkownik dostaje informację
        # "user does not exist"
        self.assertEqual("User does not exist.", self.login_page.get_alert_message())

    def test_invalid_password(self):
        """BEZ DDT"""
        # Kroki:
        # 1. Wpisz poprawny username
        self.login_page.enter_username(ValidLoginCredentials.username)
        # 2. Wpisz niepoprawny password
        self.login_page.enter_password(self.test_data.password)
        # 3. Kliknij LogIn
        self.login_page.click_log_in()
        # 4. Sprawdź, czy użytkownik dostaje informację
        # "Wrong password."
        self.assertEqual("Wrong password.", self.login_page.get_alert_message())

    def test_invalid_username_and_password(self):
        self.login_page.enter_username("sdd")
        self.login_page.enter_password("sadjghfd")
        self.login_page.click_log_in()
        self.assertEqual("Wrong password.", self.login_page.get_alert_message())
