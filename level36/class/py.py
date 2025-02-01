def manual_capitalize(user_str):
    if len(user_str) == 0:
        print("") 
    
    first_letter = user_str[0].upper()
    left_letters= user_str[1].lower()
    print(first_letter + left_letters)


print(manual_capitalize("ByE"))       
print(manual_capitalize("fRIEND"))      
print(manual_capitalize("pYTHON"))      
print(manual_capitalize("fUnCtIoN"))    
print(manual_capitalize("123123Ad"))   





def lower_or_upper(user_str, choise):
    if choise == "upper":
        print(user_str.upper())
    elif choise == "lower":
        print(user_str.lower())
    else:
        print("wrong choise")
   
       

lower_or_upper("nika" ,  "anna")
lower_or_upper("gio" ,  "ana")
lower_or_upper("print" ,  "return")



name = "nikoloz"
surname = "gagvishvili"
age = 12
academy = "goa"
role = "student"

print("my name is {}, my surname is {}. I am {} years old. I study at {}, my role is {}.").format((name , surname , age , academy , role))