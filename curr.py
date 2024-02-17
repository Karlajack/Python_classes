# This variable defination
name.upper()=input("Enter currency type: ")
amount=int(input("Enter amount to convert to Ksh= "))
if (name=="usd"):            # us dollar
      print(f"Ksh {amount*150}")
elif (name=="eur"):           # euro
      print(f"Ksh {amount*160}")
elif (name=="jpy"):           #japanese yen
      print(f"Ksh {amount*130}")
elif (name=="gbp"):        # british pound
      print(f"Ksh {amount*180}")
else:
        print("Exchange rate is not found")

