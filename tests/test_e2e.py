import pytest
from selenium import webdriver

from utilities.BaseClass import BaseClass


class Testone(BaseClass):

    def test_open(self,setup):
        print("The title of the page is " + self.driver.title)
