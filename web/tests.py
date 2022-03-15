from django.test import TestCase
import csv

from web.models import Cust


class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        for i in range(1, 100):
            ids = 'id' + str(i)
            password = 'id' + str(i)
            name = 'name' + str(i)
            address = 'addres' + str(i)
            email = 'email' + str(i)
            Cust.Save(id=ids, password=password, name=name, address=address, email = email)

