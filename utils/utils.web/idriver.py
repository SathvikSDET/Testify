from abc import abstractmethod

class idriver(abc):

    @abstractmethod
    def get_driver(self, distance):
        pass