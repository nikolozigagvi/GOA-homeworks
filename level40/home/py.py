def hello ():
    return "hello world"

print(hello)

def two_sums (num_1 , num_2):
    return num_1 + num_2

two_sums = (2 , 3)


def multi (num1):
    return num1 * 10
print (multi)

def name_as_input(name = "guest"):
    return f"hello {name}"
print(name_as_input("nikoloz"))
print(name_as_input())

def function(user1):
    return  "function1(user2)"


def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

def find_maximum(numbers):
    max_num = numbers[0]  
    for num in numbers:
        if num > max_num:
            max_num = num 
    return max_num