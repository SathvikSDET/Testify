from basepages import BasePom
from selenium.webdriver.common.by import By

class LoginPage(BasePom):
    def __init__(self, driver):
        super().__init__(driver)

    ##locators
    emailid = (By.ID , "email")
    password = (By.ID, "password")

    def isElementDisplayed(self, element):
        element = self.find_element(element)
        return element.is_displayed()
    
    def enterUrl(self, url):
        base_url = self.config.get("URL", "baseURL")
        if base_url:
            full_url = base_url + url
            return self.driver.get(full_url)
        else:
                print("Base URL not found")


if __name__ == '__main__':

    from selenium import webdriver
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.enterUrl("/login")
    print(login_page.isElementDisplayed(LoginPage.emailid))
    print(login_page.isElementDisplayed(LoginPage.password))
    driver.quit()


    
    