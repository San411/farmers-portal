  #Initially the mulitplicarion factor is 1 and depending upon soil and weather it can go slightly up or down
#The list of Soil types Possible
#Clayey, Sandy, Silty
soil=[0,"sandy","loamy","lateritic","red sandy","latersistic gravelly", "lateristic","deep black","medium black","shallow black"]
A=[]
A.append(25)
constant_temp=A[0]

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
    if(temperature>=25 and temperature<50):
        print("At warmer temperature the breeding cycle of insects is increased\n")
        multiplication_factor-=(temperature-constant_temp)/500
    elif(temperature<25 and temperature>10):
        print("In winter there are lesser number of breeding cycle of insects\n")
        multiplication_factor+=(constant_temp-temperature)/500
    else:
        print("The temperature value is not present in Karnataka at all\n")
        multiplication_factor=-1
    return multiplication_factor

def Soil_Type(soil2):
    multiplication_factor=1.0
    soil = [0, "sandy", "loamy", "lateritic", "red sandy", "latersistic gravelly", "lateristic", "deep black",
            "medium black", "shallow black"]
    if(soil2.lower()==soil[1]):
        multiplication_factor=0.85
    elif(soil2.lower()==soil[2]):
        multiplication_factor = 0.92
    elif (soil2.lower() == soil[3]):
        multiplication_factor = 0.90
    elif (soil2.lower() == soil[4]):
        multiplication_factor = 0.87
    elif (soil2.lower() == soil[5]):
        multiplication_factor = 0.94
    elif (soil2.lower() == soil[6]):
        multiplication_factor = 0.90
    elif (soil2.lower() == soil[7]):
        multiplication_factor = 0.96
    elif (soil2.lower() == soil[8]):
        multiplication_factor = 1.03
    elif (soil2.lower() == soil[9]):
        multiplication_factor = 1.08
    else:
        multiplication_factor=-1
    return multiplication_factor


millet_crop=Plant("Rabi","Clayey",50.0)

result=Weather_Input()
while result==-1:
    print("The temperature in Karnataka is usually between 10 and 50 degree Celsius\nPlease retry")
    result=Weather_Input()
else:
    base=millet_crop.base_price
    millet_crop.base_price=result*(millet_crop.base_price)
    print(f"The base price is {base} and the updated price is {millet_crop.base_price} ")
    print(millet_crop)


print(f"\nChoose a soil type among\n{soil[1]} \n{soil[2]} \n{soil[3]} \n{soil[4]} \n{soil[5]} \n{soil[6]} \n{soil[7]} \n{soil[8]} \n{soil[9]}")
soil2=input("Enter a soil type now\n")
result1=Soil_Type(soil2)
while result1 == -1:
    print("The soil type is of the types \n{soil[1]} \n{soil[2]} \n{soil[3]} \n{soil[4]} \n{soil[5]} \n{soil[6]} \n{soil[7]} \n{soil[8]} \n{soil[9]\nPlease retry")
    result1 = Weather_Input()
else:
    base = millet_crop.base_price
    millet_crop.base_price = result1 * (millet_crop.base_price)
    print(f"The base price is {base} and the updated price is {millet_crop.base_price} ")
    print(millet_crop)
