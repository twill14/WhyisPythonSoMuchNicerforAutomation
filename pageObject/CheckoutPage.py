from selenium.webdriver.common.by import By
from pageObject.ConfirmPage import ConfirmPage

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    purchaseButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH , "//button[@class='btn btn-success']")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    country = (By.ID, "country")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    success = (By.CSS_SELECTOR, "[class*='alert-success']")


    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

    def click_checkBox(self):
        self.driver.find_element(*CheckOutPage.checkBox).click()

    def getPurchaseButton(self):
        return self.driver.find_element(*CheckOutPage.purchaseButton)

    def  getCountry(self):
        return  self.driver.find_element(*CheckOutPage.country)

    def click_Submit(self):
        self.driver.find_element(*CheckOutPage.submit).click()

    def getSuccessMessage(self):
        return self.driver.find_element(*CheckOutPage.success).text