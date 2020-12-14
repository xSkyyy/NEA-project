def airportdetails():
  correctairport = False
  distance = False
  ukairportcode = input("please input the UK airport code")
  if ukairportcode == "LPL":
    osairportcode = input("please enter the overseas airport code ")
    if osairportcode == "JFK":
      print("John F Kennedy International")
      correctairport = True 
      distance = 5326
    elif osairportcode == "ORY":
      print("Paris - Orly")
      correctairport = True
      distance = 629
    elif osairportcode == "MAD":
      print("Adolfo Suarez Madrid-Barajas")
      correctairport = True
      distance = 1428
    elif osairportcode == "AMS":
      print("Amsterdam Schiphol")
      correctairport = True
      distance = 526
    elif osairportcode == "CAI":
      print("Cairo International")
      corectairport = True
      distance = 3779
    else:
      print("airport code entered not valid.")
  elif ukairportcode == "BOH" :
    osairportcode = input("please enter the overseas airport code")
    if osairportcode == "JFK":
      print("John F Kennedy International")
      correctairport = True 
      distance = 5486
    elif osairportcode == "ORY":
      print("Paris - Orly")
      correctairport = True
      distance = 379
    elif osairportcode == "MAD":
      print("Adolfo Suarez Madrid-Barajas")
      correctairport = True
      distance = 1151
    elif osairportcode == "AMS":
      print("Amsterdam Schiphol")
      correctairport = True
      distance = 489
    elif osairportcode == "CAI":
      print("Cairo International")
      correctairport = True
      distance = 3584
    else:
      print("airport code entered not valid.")
  else:
    print("Airport not valid")
  return(correctairport,distance)
 
def flightdetails():
  correctaircraft = False
  fcs = False
  maxflightrange = False
  runningcost = False
  standardclassseats = False
  aircraft= input("please enter your choice of aicraft : \n medium narrow body \n large narrow body \n medium wide body \n ").lower()
  if aircraft == "medium narrow body": 
    print("Medium Narrow Body")
    print("running cost pers seat 100km - £8")
    print("Maxium Flight Range - 2650")
    print("capacity if all seats are standard class - 180 ")
    print("minium number of first class seats - 8 ")
    minfirstclass = 8
    cap = 180
    correctaircraft = True
    maxflightrange = 2650
    runningcost = 8
  elif aircraft == "large narrow body":
    print("running cost pers seat 100km - £7")
    print("Maxium Flight Range - 5600")
    print("capacity if all seats are standard class - 220 ")
    print("minium number of firts class seats - 10 ")
    minfirstclass = 10
    cap = 220
    correctaircraft = True
    maxflightrange = 5600
    runningcost = 7
  elif aircraft== "medium wide body" :
    print("Medium Wide Body")
    print("running cost pers seat 100km - £5")
    print("Maxium Flight Range - 4050")
    print("capacity if all seats are standard class - 406 ")
    print("minium number of firts class seats - 14 ")
    minfirstclass = 14
    cap = 406  
    correctaircraft = True
    maxflightrange = 4050
    runningcost = 5
  else:
    print("Invalid aircraft")
    return(correctaircraft,fcs,maxflightrange,runningcost,standardclassseats)
    
  numfirstclass = int(input("Enter the number of first class seats"))
  if numfirstclass != 0:
    if numfirstclass >= minfirstclass:
        if numfirstclass <= (cap/2):
            standardclassseats = cap - (numfirstclass * 2)
            print(standardclassseats, " standard class seats available")
            fcs = numfirstclass
        else:
            print("Error")
    else:
      print("Error")
  else:
    print("Error")
  return(correctaircraft,fcs,maxflightrange,runningcost,standardclassseats)

def priceplan(correctairport,correctaircraft,fcs,maxflightrange,distance,runningcost,standardclassseats):
    if correctairport == True:
        if correctaircraft == True:
            if fcs != False:
                if maxflightrange >= distance:
                    standardprice = int(input("How much is a standard class seat?"))
                    firstprice = int(input("How much is a first class seat?"))
                    fcps = (runningcost * distance)/100
                    flightcost = fcps * (fcs + standardclassseats)
                    flightincome = (fcs * firstprice) + (standardclassseats * standardprice) 
                    flightprofit = flightincome - flightcost
                else:
                    print("Error")
            else:
                print("Error")
        else:
            print("Error")
    else:
        print("error")
    
def clear():
  pass

y = False
x = True 
while x == True:
 
  print("1.enter airport details")
  print("2.enter flight details")
  print("3.enter price plan and enter and calculate profit")
  print("4.clear")
  print("5.quit")

  choice = input("please select one of the options") 

  if choice == "1":
    correctairport,distance = airportdetails()
  elif choice =="2":
    correctaircraft,fcs,maxflightrange,runningcost,standardclassseats = flightdetails()
  elif choice == "3":
    priceplan(correctairport,correctaircraft,fcs,maxflightrange,distance,runningcost,standardclassseats)
  elif choice == "4":
    clear()
  elif choice == "5":
    x = False
