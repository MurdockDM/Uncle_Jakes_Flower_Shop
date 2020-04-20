from .flower import Flower
from growth_class.is_refrigerated import Irefrigerated

class Rose(Flower, Irefrigerated):
    
    def __init__(self, color):
        Flower.__init__(self)
        Irefrigerated.__init__(self)
        self.color = color.capitalize()
        self.flower_type = "Rose"
        self.stem_length = "7 inches"


    def __str__(self):
        return f"{self.color} Rose"    