from arrangements.arrangement import Arrangement



class ValentinesDay(Arrangement):
    def __init__(self):
        Arrangement.__init__(self)
 
    # Override the `enhance` method from Arrangement to ensure only
    # roses, lillies, and alstroemeria can be added

    def enhance(self, flower):

        try:
            if flower.is_refrigerated == True:
                self._Arrangement__flowers.append(flower)
                print(f"You added a {flower} to the Valentines Day arrangement")
            else:
                print("The flower must be either a Rose, Lilly, or Alstroemeria to be added to the Valentines Day arrangement")
        except AttributeError:
            return 0                

    def __str__(self):
        listOfFlowers = []
        for flower in self._Arrangement__flowers:
            listOfFlowers.append(str(flower))
        return(f"This Valentine's Day arrangement has {listOfFlowers}")                