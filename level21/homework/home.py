# 7 davaleba 
bill = int(input("enter your bill :"))
tip = int(input(bill * 20 // 100))

# davaleba 6 
hours=int(input(7425 // 550))

#davaleba 5

floor = int(input("enter your floor :"))
if floor == 5:
 print("it is resturant")
else:
 print("it is not a resturant")

#davaleba 4

supported = ["light off ", "look the door" , "open the door" , "make coffee" , "shut down"]
supported = int(input("enter you command :"))
if supported == True:
 print("ok")

 #davaleba 2
day = int(input("enter the day :"))
hours = int(input("enter the hours : "))
if day == 7:
  print("today we arnt working")
elif day < 7:
  print("we are working")
  if hours == 22:
   print(" we arnt working any more")
elif hours < 22:
  print("we are open")