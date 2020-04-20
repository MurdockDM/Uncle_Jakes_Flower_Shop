from arrangements.arrangement import Arrangement

class MothersDay(Arrangement):

    def __init__(self):
        Arrangement.__init__(self)

    def enhance(self, flower):

        try:
            if flower.is_refrigerated == False:
                self._Arrangement__flowers.append(flower)
                print(f"You added a {flower} to the Mothers Day arrangement")
            else:
                print("The flower must be either a Daisy, Baby's Breath, or Poppy to be added to the Mothers Day arrangement")
        except AttributeError:
            return 0     

    def __str__(self):
        listOfFlowers = []
        for flower in self._Arrangement__flowers:
            flowerToString = str(flower)
            listOfFlowers.append(flowerToString)
        return(f"This Mothers Day arrangement has  {listOfFlowers}")        