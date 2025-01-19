from abc import ABC, abstractmethod
import Configparserparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver

class WebDriverFactory(ABC):
  
    __chrome_driver_local = lambda: webdriver.Chrome()
    __firefox_driver_local = lambda: webdriver.Firefox()
    __safari_driver_local = lambda: webdriver.Safari()

    __chrome_driver_remote = lambda: webdriver.Remote(
        command_executor=self.remote_url,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    __firefox_driver_remote = lambda: webdriver.Remote(
        command_executor=self.remote_url,
        desired_capabilities=DesiredCapabilities.FIREFOX
    )
    __safari_driver_remote = lambda: webdriver.Remote(
        command_executor=self.remote_url,
        desired_capabilities=DesiredCapabilities.SAFARI
    )

    local_map = {
        "chrome": __chrome_driver_local,
        "firefox": __firefox_driver_local,
        "safari": __safari_driver_local
    }

    remote_map = {
        "chrome": __chrome_driver_remote,
        "firefox": __firefox_driver_remote,
        "safari": __safari_driver_remote
    }

    def __init__(self):
        # Load Configparseruration settings
        self.Configparser = Configparser()
        self.browser_name = self.Configparser['Grid']['browser']
        self.grid_enabled = self.Configparser.getboolean('Grid', 'Grid')
        self.headless = self.Configparserparser.getboolean('Grid', 'headless')
        self.remote_url = self.Configparserparser.getboolean('Grid', 'remote_url')

    @classmethod
    def get_driver(self, name):
        if name not in local_map and name not in remote_map:
            if self.grid_enabled:
                return remote_map[name]
            else:
                return local_map[name]
        else:
            raise ValueError(f"Unsupported browser: {name}")
