#homework 2: Basic List Operations

fruits =["apple", "banana", "cherry", "date",  "elderberry"]
print(fruits)
print(fruits[0])
print(fruits[4])
fruits.append("fig")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits[2] = "blueberry"
print(fruits)
print(len(fruits))


#homework 3: List Functions and Methods


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers)
numbers.append(100)
numbers.remove(30)
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
print(numbers.index(50))
print(numbers.count(20))

#homework 4: Slicing and List Comprehensions


number = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
number_twin = [1 , 2 , 3 , 4 , 5 ]
number_not_twin = [6 , 7 , 8 , 9 ,10]
print(number + number_twin + number_not_twin)




#homework 5: List Manipulation and Aggregation


temperatures = [72, 68, 75, 70, 78, 74, 71]
max(temperatures) == [72, 68, 75, 70, 78, 74, 71]
print(max(temperatures))
print(min(temperatures))
print(sum(temperatures))

above_70 = [72 , 75 , 70 , 78 , 74 , 71]
print(above_70)