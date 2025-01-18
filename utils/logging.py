import logging


class Logging:

    level_dict = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }

    def __init__(self,classname):
        self.configparser = configparser()
        self.logger = logging.getLogger(classname)
        log_level = level_dict[self.config.get('Logging', 'level', fallback='DEBUG').upper()]
        self.logger.setLevel(log_level)

        self.filehandler = logging.FileHandler("./reports/app.log")
        self.filehandler.setLevel(logging.DEBUG)

        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.filehandler.setFormatter(self.formatter)

        self.filehandler.setFormatter(self.formatter)
        self.logger.addHandler(self.filehandler)

    
  
     



        



