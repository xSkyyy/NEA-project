def airportdetails():
  airportcode = input("Input the 3 letter code for the airport")
  if airportcode == "LPL" or airportcode == "BOH":
    pass 
  else:
    print("Airport code not valid.")
    pass
def flightdetails():
  pass
def priceplan():
  pass
def clear():
  pass


print("1. enter airport details pls")
print("2. enter flight details")
print("3. enter price plan and calculate profit")
print("4. clear")
print("5. quit")
choice = input ("please select one of the options")
x = True
while x == True:
  if choice == "1":
    airportdetails()
  elif choice == "2":
    flightdetails()
  elif choice == "3":
    priceplan()
  elif choice == "4":
    clear()
  elif choice == "5":
    x = False
