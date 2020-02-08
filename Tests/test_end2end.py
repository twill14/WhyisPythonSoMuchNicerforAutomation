import pytest
from selenium import webdriver
import time
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from pageObject.CheckoutPage import CheckOutPage





class TestOne(BaseClass):
    def test_end2end(self):
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        checkOutPage.getPurchaseButton().click()
        confirmPage = checkOutPage.checkOutItems()
        checkOutPage.getCountry().send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text

        assert ("Success! Thank you!" in textMatch)
