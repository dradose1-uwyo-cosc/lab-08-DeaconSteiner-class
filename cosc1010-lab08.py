# Deacon Steiner
# UWYO COSC 1010
# 11/05/24
# Lab 08
# Lab Section: 11
# Sources, people worked with, help given to:
# Used w3schools to find a method to check if the entered string is a float


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def num_check(user_string):
    
    if user_string.isdigit():
        return int(user_string)
        
    elif user_string.count('.') == 1 and user_string.replace('.', '').isdigit():
        return float(user_string)
        
    elif user_string[0] == '-' and user_string[1:].isdigit():
        return int(user_string)
    
    elif user_string[0] == '-' and user_string[1:].count('.') == 1 and user_string[1:].replace('.', '').isdigit():
        return float(user_string)
    
    else:
        return False
        

while True:

    
    user_string = input("Number Checking: Please enter something (exit to leave): ")
    
    if user_string == "exit".lower():
        print("END")
        break

    else:
        num_check(user_string)
        print(type(num_check(user_string)))



print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, x_lower, x_upper):
    """ Given m, b, and a lower and upper x bound, return all y-values on the interval

    Args:
        m (int, float): slope of the line
        b (int, float): y-intercept of the line
        x_lower (int): lower bound for x-value
        x_upper (int): upper bound for x-value
    """
    y_vals = []
    
    for i in range(x_lower, x_upper+1):
        y = (m*i) + b
        y_vals.append(y)
        
        
    print(y_vals)
   
#slope_intercept(-1, 0, 0, 5)
   
while True:
    user_value = input("Slope-Intercept: Please enter exit to leave or continue to begin: ")
    
    quit_command = 'exit'.lower()
    continue_command = 'continue'.lower()
    if user_value == quit_command:
        print("END")
        break
    
    if user_value == continue_command:
        
        m = input("Input a slope value: ")
        b = input("Input a y-intercept value: ")
        x_lower = input("Enter a lower x bound: ")
        x_upper = input("Enter an upper x bound: ")
        
        if (not isinstance(num_check(x_lower), int) or not isinstance(num_check(x_upper), int)):
            print("Error: Bounds must be whole numbers")
            continue
            
        if (isinstance(num_check(m), int) or isinstance(num_check(m), float) or (isinstance(num_check(b), int) or isinstance(num_check(b), float))):
            slope_intercept(num_check(m), num_check(b), num_check(x_lower), num_check(x_upper))
            
        else:
            print("m and b must both be numbers")
            continue
        
    
        
            
       
                
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def quadratic_solver(a, b, c):
    """given values for a, b, and c: return the x-values
    ax^2+bx+c=0 -> quadratic equation

    Args:
        a (int, float): coefficient on the x^2 value
        b (int, float): coefficient on the x value
        c (int, float): constant
    """
    x_1 = ((-num_check(b) + ((num_check(b)**2 - (4 * num_check(a) * num_check(c)))**(1/2))) / 2 * num_check(a))
    x_2 = ((-num_check(b) - ((num_check(b)**2 - (4 * num_check(a) * num_check(c)))**(1/2))) / 2 * num_check(a))
    
    print(x_1)
    print(x_2)
    
while True:
    user_value = input("Quadratic Solver: Please enter exit to leave or continue to begin: ")
    
    quit_command = 'exit'.lower()
    continue_command = 'continue'.lower()
    if user_value == quit_command:
        print("END")
        break
    
    if user_value == continue_command:
        
        a = input("Please enter the coefficient of the x^2 term: ")
        b = input("Please enter the coefficient of the x term: ")
        c = input("Please enter the constant term: ")
        
        if (isinstance(num_check(a), int) or isinstance(num_check(a), float) or isinstance(num_check(b), int) or isinstance(num_check(b), float) or isinstance(num_check(c), int) or isinstance(num_check(c), float)):
            quadratic_solver(a, b, c)
        
        else:
            print("Error: All values must be numbers")
            continue
        
        
print("*" * 75)  

      
def square_root(s):
    """Take the square root of a number

    Args:
        s (int, float): The number that is being square rooted
    """
    if num_check(s) < 0:
        print("Cannot calculate the square root of a negative number")
        return "null"
    
    else:
        return num_check(s)**(1/2)
    

    
while True:
    user_value = input("Square Root: Please enter exit to leave or continue to begin: ")
    
    quit_command = 'exit'.lower()
    continue_command = 'continue'.lower()
    if user_value == quit_command:
        print("END")
        break
        
    if user_value == continue_command:
        
        s = input("Please enter a number to calculate the square root: ")
        
        if isinstance(num_check(s), int) or isinstance(num_check(s), float):
            root_number = square_root(s)
            print(f"The square root of {s} is {root_number}")
            
        else:
            print("Error: s must be a positive number")
            
print("*" * 75)
        
        
    