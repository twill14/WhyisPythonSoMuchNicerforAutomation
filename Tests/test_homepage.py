from selenium import webdriver
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from TestData.HomePageData import HomePageData
import pytest


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.submitForm().click()

        alertText = homePage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params = HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param