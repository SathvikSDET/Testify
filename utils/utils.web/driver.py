import idriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver


class driver(idriver):

    __chrome_webdriver = lambda (): webdriver.chrome






    def get_driver(self, browser):
        pass
  