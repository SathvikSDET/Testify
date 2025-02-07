from enum import Enum, auto

class ElementLocator:
    
    class LookUpType(Enum):
        XPATH = "xpath"
        CSS_SELECTOR = "css_selector"
        ID = "id"
        
    def __init__(self, locator_type, locator):
        if locator_type not in self.LookUpType.__members__:
            raise ValueError(f"Invalid locator type: {locator_type}")
        self.locator_type = self.LookUpType[locator_type]  
        self.locator_data = locator  
