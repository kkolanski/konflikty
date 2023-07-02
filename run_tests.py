import unittest
from tests.login_test import LoginTest
# Pobierz testy, które chcesz uruchomić
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# Lista testów do uruchomienia
tests_for_run = [
    login_test,
    # kolejny test
    # ...
]

# Stwórz Test Suitę łącząc testy
test_suite = unittest.TestSuite(tests_for_run)

# Odpal testy
unittest.TextTestRunner().run(test_suite)