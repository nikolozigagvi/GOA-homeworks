def big_sentence(name, surname, age, color):
  print(f"my {name} {surname} my {age} and my fav {color}")

big_sentence("nika" , "gagvishvili","12" , "green")

print(big_sentence)



def  check_lowercase(user_str):
  if user_str.lower():
    print("user_str is lower")
  else:
    if user_str.upper():
     print("user_str isnt lower")

check_lowercase("nika")
check_lowercase("gergIa")
check_lowercase("5iorgi") 



def elemet_remover(user_list, index_remove):
  list1 = ["a" , "b" , "c"]
  print(list1.pop(index_remove))