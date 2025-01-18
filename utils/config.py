import configparser
import os

class Configparser:
    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = os.path.join(os.getcwd(),"config", "config.ini")
        self.config.read(config_path) 
        
    def get(self, sub, key):
        try:
            return self.config[sub][key]
        except KeyError:
            print(f"Key {key} not found in section {sub}")
            return None

if __name__ == "__main__":
    c = config()
    print(c.get("URL", "baseURL"))  
