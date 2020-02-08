import pytest
from selenium import webdriver
import time
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from pageObject.CheckoutPage import CheckOutPage


class TestEnd2End(BaseClass):

    def test_end2end(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            print(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        checkOutPage.getPurchaseButton().click()
        checkOutPage.checkOutItems()
        log.info("Entering country name as ind")
        checkOutPage.getCountry().send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        self.driver.find_element_by_link_text("India").click()
        checkOutPage.click_checkBox()
        checkOutPage.click_Submit()
        textMatch = checkOutPage.getSuccessMessage()
        log.info("Text Recieved from application is " + textMatch)
        assert ("Success! Thank you!" in textMatch)
