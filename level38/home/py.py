def  check_lowercase(user_str):
  if user_str.islower():
    print("user_str is lower")
  else:
    if user_str.isupper():
     print("user_str isnt lower")

check_lowercase("nika")
check_lowercase("gergIa")
check_lowercase("5iorgi")

def check(str1):
  print(str1.islower)

check("hello")
check("Giroegi")
check("gEorgia")
check("hello12")
check("goa is The best1234")
check("why so h1ard")



str1 = input("enetr you str :")

if str1.islower():
  print("your str is lower")
else:
  print("your str is not in lowercase ")



def check_upper(str2):
  print(str2.isupper())



def chaeck_if_upper(s: str):
    return s.isupper()


print(chaeck_if_upper("good"))  
print(chaeck_if_upper("GOOD"))  
print(chaeck_if_upper("1GOO3"))    
print(chaeck_if_upper("GO3")) 



is_upper = input("enter you str for a check up :")

if is_upper.isupper():
  print("your str has passed the check up")
else:
  print("your str didnt passed the check up soo choose new one")

def swap(str1):
    print( str1.swapcase())

str2 = "best" , "academy" , "is" , "GOA"
print(str2.swapcase())