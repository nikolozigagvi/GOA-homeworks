def first_and_last(lst):
    if not lst:
        return None 
    return [lst[0], lst[-1]]

def max_of_three(a, b, c):
    return max(a, b, c)

def reverse_string(s):
    return s[::-1]


print(first_and_last([1, 2, 3, 4]))  
print(max_of_three(10, 25, 15))      
print(reverse_string("გამარჯობა"))   