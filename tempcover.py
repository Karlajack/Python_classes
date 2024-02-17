

def temp_converter(temp_from,temp_to,temp_value):
    if(temp_from == "FARENHEIGHT" and  temp_to == "DEGREE"):
        temp = temp_value-33.5
        print(f"{temp_value} Farenheight is equivalent to {temp} degree celcius")
    elif (temp_from == "DEGREE" and  temp_to == "FARENHEIGHT"):
        temp = temp_value+33.5
        print(f"{temp_value} degree is equivalent to {temp} Farenheight celcius")
    else:
        print("Invalid temperature type")

temp_from = input("Are you converting from 'Farenheigt' or degree': ").upper()
temp_to = input("Are you converting to 'degree' or Farenheight': ").upper()
temp_value =float(input("Enter temp value: "))

temp_converter(temp_from,temp_to,temp_value)
