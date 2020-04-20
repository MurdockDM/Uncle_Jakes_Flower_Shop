from .flower import Flower
from growth_class.is_refrigerated import Irefrigerated

class Lilly(Flower, Irefrigerated):

    def __init__(self):
        Flower.__init__(self)
        Irefrigerated.__init__(self)
        self.flower_type = "Lilly"


    def __str__(self):
        return "Lilly"    