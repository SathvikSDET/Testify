
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from abc import ABC,abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Testify.utils.config import config


class  BasePom(ABC) :

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.config = config()
        PageFactory.init_element(self.driver,self)


    def find_element(self, webelement): 
        return self.wait.until(EC.presence_of_element_located(webelement))
   

    def find_elements(self, webelement):
        return self.wait.until(EC.presence_of_all_elements_located(webelement))

    @abstractmethod
    def isElementDisplayed(self, webelement):
        pass
    @abstractmethod
    def enterUrl(self, url):
        pass
