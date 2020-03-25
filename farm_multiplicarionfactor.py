#Code by Rahul Noronha 00:56 24/03/2020

muliplication_factor=1 #Initially the mulitplicarion factor is 1 and depending upon soil and weather it can go slightly up or down

class Plant():
    def __init__(self,type,soil,base_price):
        self.type=type
        self.soil=soil
        self.base_price=base_price
    def __str__(self):
        return(f"The crop is of the type {self.type}, which grows in {self.soil} soil and in ideal conditions it costs Rs. {self.base_price}\n")
    def Weather_Input():
        temperature=int(input("Enter the current temperature\n"))
        print(temperature)
        if (temperature>=22):
                seaoson= "Summer"
        else:
                season= "Winter"
        print("Enter True if it is rainy season and False if not\n")
        rain=input()

    pass
result=Weather_Input()
print("It is "+result)
millet_crop=Plant("Rabi","Clayey","50")
print(millet_crop)
