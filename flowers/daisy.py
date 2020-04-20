from .flower import Flower
from growth_class.not_refrigerated import Inotrefrigerated

class Daisy(Flower, Inotrefrigerated):

    def __init__(self):
        Flower.__init__(self)
        Inotrefrigerated.__init__(self)
        self.flower_type = "Daisy"

    def __str__(self):
        return "Daisy"    