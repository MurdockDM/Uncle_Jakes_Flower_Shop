from .flower import Flower
from growth_class.not_refrigerated import Inotrefrigerated

class Poppy(Flower, Inotrefrigerated):

    def __init__(self):
        Flower.__init__(self)
        Inotrefrigerated.__init__(self)
        self.flower_type = "Poppy"

    def __str__(self):
        return "Poppy"    