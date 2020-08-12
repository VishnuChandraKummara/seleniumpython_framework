import pytest
from selenium import webdriver

from utilities.BaseClass import BaseClass


class Testone(BaseClass):

    def test_open(self,setup):
        print("The title of the page is " + self.driver.title)
        print ("Hello this is the program running from GIT")
        print("Hello this is the program running from GIT second trigger")

