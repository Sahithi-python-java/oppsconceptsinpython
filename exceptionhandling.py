# Function to check if a number is positive
def check_positive(number):
    # If the number is less than or equal to 0, raise a ValueError
    if number <= 0:
        raise ValueError("The number must be positive.")
    # If the number is positive, return it (optional, but signifies valid input)
    return number

# Using a try-except block to handle any exceptions that might occur
try:
    # Prompt the user to enter a number, and convert the input to an integer
    user_input = int(input("Enter a number: "))
    
    # Call the check_positive function to check if the input is positive
    check_positive(user_input)
    
    # If no exception is raised, print a confirmation that the number is positive
    print(f"Great! {user_input} is a positive number.")

# Handle the ValueError that might be raised if the number is not positive
except ValueError as e:
    # Print the error message that was raised in the check_positive function
    print(e)


'''Explanation of the Comments:
Function Definition (check_positive):
Comment: The function check_positive checks if a given number is positive. If the number is less than or equal
 to 0, it raises a ValueError.

Line: if number <= 0: checks the condition, and if it's true, the exception is raised using raise ValueError().
Try Block:
Comment: The try block is where the code tries to take user input and process it. If the user enters invalid 
input (like a negative number), the corresponding exception is handled.

Line: int(input("Enter a number: ")) converts the user input (which is a string) to an integer so that it can
 be checked if it’s positive.
Check Function Call:
Comment: The function check_positive(user_input) is called to check if the input is positive.
If the input passes the check (i.e., it's positive), the else part of the function executes 
(which is implicitly just a return statement).

Except Block:
Comment: The except block catches the ValueError raised by the check_positive function when an invalid input
 (non-positive number) is detected.
Line: The error message stored in ValueError is printed for the user’s understanding, telling them what went 
wrong.
'''