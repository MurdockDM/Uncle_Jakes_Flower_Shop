from flowers import Daisy, Alstroemeria, Babys_Breath, Lilly, Poppy, Rose
from arrangements import MothersDay, ValentinesDay

if __name__ == "__main__":
    
    daisy = Daisy()
    babys_breath = Babys_Breath()
    alstroemeria = Alstroemeria()
    poppy = Poppy()
    lilly = Lilly()
    red_rose = Rose("red")
    pink_rose = Rose("pink")
    blue_rose = Rose("blue")
    
    valentines_day = ValentinesDay()
    mothers_day = MothersDay()

    valentines_day.enhance(pink_rose)  
    valentines_day.enhance(red_rose)  
    valentines_day.enhance(blue_rose)  
    valentines_day.enhance(lilly)  
    valentines_day.enhance(alstroemeria)  
    
    mothers_day.enhance(daisy)
    mothers_day.enhance(babys_breath)
    mothers_day.enhance(poppy)



print(valentines_day)
print(mothers_day)
    
