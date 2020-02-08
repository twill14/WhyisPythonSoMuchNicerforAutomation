from selenium.webdriver.common.by import By
from pageObject.CheckoutPage import CheckOutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    example = (By.ID, "exampleCheck1")
    selection = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    alert = (By.CSS_SELECTOR, "[class*='alert-success']")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return  checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.example)

    def getGender(self):
        return self.driver.find_element(*HomePage.selection)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.alert)
