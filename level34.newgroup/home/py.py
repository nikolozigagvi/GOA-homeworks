#1
def sum_numbers(num1 , num2):
 print(num1 * num2)

sum_numbers(1 , 23)
sum_numbers(4 , 2)
sum_numbers(6 , 3)
sum_numbers(7 , 2)
sum_numbers(6 , 26)


#2
def welcome_user(name):
    print("Welcome {name}!")


welcome_user("nikoloz")

#3
def find_maximum(numbers):
    if not numbers:  
        print(None)
     
    maximum = numbers[0]  
    for num in numbers:  
        if num > maximum:  
            maximum = num  
    print(maximum) 


numbers_list = [5, 7, 5, 9, 9, 10]
print(find_maximum(numbers_list))  


#4
#ფუნქცია არის კოდის ორგანიზებული ნაწილი რომელიც ასრულებს კონკრეტულ ამოცანას.
#არგუმენტი არის კონკრეტული მნიშვნელობა რომელსაც პარამეტრისთვის ფუნქციის გამოძახებისას გადავცემთ.
#def არის საკვანძო სიტყვა პითონ-ში რომელიც გამოიყენება ფუნქციის განსაზღვრის დასაწყებად.