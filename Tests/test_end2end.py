import pytest
from selenium import webdriver
import time
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from pageObject.CheckoutPage import CheckOutPage


class TestEnd2End(BaseClass):

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
        checkOutPage.checkOutItems()
        checkOutPage.getCountry().send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        self.driver.find_element_by_link_text("India").click()
        checkOutPage.click_checkBox()
        checkOutPage.click_Submit()
        textMatch = checkOutPage.getSuccessMessage()

        assert ("Success! Thank you!" in textMatch)
