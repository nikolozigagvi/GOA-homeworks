for num in range(1, 101):
   
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    
    else:
         
  
            age = int(input("Please enter your age: "))
            driving_experience = int(input("Please enter your driving experience in years: "))

          
            if age <= 0 or driving_experience < 0:
                print("Both age and driving experience must be positive integers. Please try again.")
                
            # Determine if the user meets the criteria for obtaining a driver's license
            if age >= 18 and driving_experience >= 1:
                print("Congratulations! You are eligible to obtain a driver's license.")
            elif age >= 18:
                print("You are old enough to obtain a driver's license, but you need at least 1 year of driving experience.")
            else:
                print("You must be at least 18 years old to obtain a driver's license.")
