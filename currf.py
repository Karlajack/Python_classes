# declaring a function
def currency_converter(curr_from,curr_to,amount):
    if (curr_from =="USD" and curr_to =="KSH"):     # USD to KSH
      cov_amt=amount*150
      print(f"{amount} {curr_from} is equivalent to {curr_to} {cov_amt}")
    elif (curr_from =="KSH" and curr_to =="USD"):     
      cov_amt=amount/150
      print(f"{amount} {curr_from} is equivalent to {curr_to} {cov_amt}")

    elif (curr_from=="EUR" and curr_to=="KSH"):     # EUR to KSH
      cov_amt=amount*170
      print(f"{amount} {curr_from} is equivalent to {curr_to} {cov_amt}")
    elif (curr_from =="KSH" and curr_to =="EUR"):  
      cov_amt=amount/170
      print(f"{amount} {curr_from} is equivalent to {curr_to} {cov_amt}")

    elif (curr_from=="JPY" and curr_to=="KSH"):     # JPY to KSH
      cov_amt=amount*175
      print(f"{amount} {curr_from} is equivalent to {curr_to} {cov_amt}")
    elif (curr_from =="KSH" and curr_to =="JPY"):  
      cov_amt=amount/175
      print(f"{amount} {curr_from} is equivalent to {curr_to} {cov_amt}")

    elif  (curr_from=="GBP" and curr_to=="KSH"):     # GBP to KSH
      cov_amt=amount*180
      print(f"{amount} {curr_from} is equivalent to {curr_to} {cov_amt}")
    elif (curr_from =="KSH" and curr_to =="GBP"):  
      cov_amt=amount/180
      print(f"{amount} {curr_from} is equivalent to {curr_to} {cov_amt}")

    else:
        print("Exchange rate is not found")
        
curr_from=input("Enter currency to convert from ").upper()
curr_to=input("Enter currency to convert to ").upper()
amount=int(input("Enter amount to convert= "))

# calling a function
currency_converter(curr_from,curr_to,amount)
