 #Initially the mulitplicarion factor is 1 and depending upon soil and weather it can go slightly up or down
A=[]
A.append(25)
constant_temp=A[0]
soil_udupi=("sandy","loamy","lateritic")
soil_bangalore=("loamy","red sandy","latersistic gravelly", "lateristic")
soil_bijapur=("deep black","medium black","shallow black")
class Plant():
    def __init__(self,type,soil,base_price):
        self.type=type
        self.soil=soil
        self.base_price=base_price
    def __str__(self):
        return(f"The crop is of the type {self.type}, which grows in {self.soil} soil and in ideal conditions it costs Rs. {self.base_price}\n")
def Weather_Input():
    multiplication_factor=1.0
    temperature=int(input("Enter the current temperature\n"))
    if(temperature>=25):
        print("At warmer temperature the breeding cycle of insects is increased\n")
        multiplication_factor-=(temperature-constant_temp)/500
    else:
        print("In winter there are lesser number of breeding cycle of insects\n")
        multiplication_factor+=(constant_temp-temperature)/500
    return multiplication_factor
millet_crop=Plant("Rabi","Clayey",50.0)
result=Weather_Input()
base=millet_crop.base_price
millet_crop.base_price=result*(millet_crop.base_price)
print(f"The base price is {base} and the updated price is {millet_crop.base_price} ")
print(millet_crop)
