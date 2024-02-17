# declaring a function
def currency(name):
    if ((name)=="USD"):            # us dollar
      print(f"Ksh {amount*150}")
    elif (name=="EUR"):           # euro
      print(f"Ksh {amount*160}")
    elif (name=="JPY"):           #japanese yen
      print(f"Ksh {amount*130}")
    elif (name=="GBP"):        # british pound
      print(f"Ksh {amount*180}")

    else:
        print("Exchange rate is not found")
        
name=input("Enter currency type: ")

amount=int(input("Enter amount to convert to Ksh= "))
# calling a function
currency(name.upper())
