from .flower import Flower
from growth_class.is_refrigerated import  Irefrigerated

class Alstroemeria(Flower, Irefrigerated):

    def __init__(self):
        Flower.__init__(self)
        Irefrigerated.__init__(self)
        self.flower_type = "Alstroemeria"

    def __str__(self):
        return "Alstroemeria"    