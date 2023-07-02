from faker import Faker
import csv

class ValidLoginCredentials:
    username = "tester_wsb"
    password = "tester"

class TestData:
    def __init__(self):
        fake = Faker()
        self.password = fake.password()
        self.user_name = fake.user_name()

    def get_login_data_from_csv(self, filename):
        """ get login data from csv file"""
        rows = []
        data_file = open(filename, "rb")
        reader = csv.reader(data_file)
        for row in reader:
            rows.append(row)
        return rows
