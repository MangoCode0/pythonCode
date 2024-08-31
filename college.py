# #[1] Prompt the user to enter a string
# user_input = input("Please enter a string: ")

# # Display the string entered by the user
# print("You entered:", user_input)


# [2]Function to calculate the electricity bill
# def calculate_bill(units_consumed, rate_per_unit, fixed_charge=0):
#     # Calculate the total bill
#     total_bill = (units_consumed * rate_per_unit) + fixed_charge
#     return total_bill

# # Main program
# def main():
#     print("Electricity Bill Calculator")
    
#     # Get user input
#     units = float(input("Enter the number of units consumed: "))
#     rate = float(input("Enter the rate per unit: "))
#     fixed_charge = float(input("Enter the fixed charge (if any): "))

#     # Calculate the bill
#     bill = calculate_bill(units, rate, fixed_charge)
    
#     # Display the result
#     print(f"The total electricity bill is: ${bill:.2f}")

# # Run the program
# if __name__ == "__main__":
#     main()

# # [3] Main program to calculate the electricity bill

# # Prompt the user to enter the number of units consumed
# units_consumed = float(input("Enter the number of units consumed: "))

# # Prompt the user to enter the rate per unit
# rate_per_unit = float(input("Enter the rate per unit: "))

# # Prompt the user to enter any fixed charge (if applicable)
# fixed_charge = float(input("Enter the fixed charge (if any): "))

# # Calculate the total bill
# total_bill = (units_consumed * rate_per_unit) + fixed_charge

# # Display the result
# print(f"The total electricity bill is: ${total_bill:.2f}")


# #[4] Main program to calculate tax

# # Prompt the user to enter their income
# income = float(input("Enter your income: "))

# # Prompt the user to enter the tax rate (as a percentage)
# tax_rate = float(input("Enter the tax rate (as a percentage): "))

# # Calculate the tax amount
# tax_amount = (income * tax_rate) / 100

# # Display the result
# print(f"The total tax amount is: ${tax_amount:.2f}")



# #[5] Main program to check if the input number is positive or negative

# # Prompt the user to enter a number
# number = float(input("Enter a number: "))

# # Check if the number is positive, negative, or zero
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")


# # [6] Function to multiply a string N times
# def multiply_string(s, N):
#     # Ensure N is a non-negative integer
#     if N < 0:
#         return "Error: The number of times must be a non-negative integer."
#     return s * N

# # Main program
# def main():
#     # Prompt the user for input
#     string_input = input("Enter the string to be multiplied: ")
#     try:
#         times = int(input("Enter the number of times to multiply the string: "))
#     except ValueError:
#         print("Error: Please enter a valid integer.")
#         return

#     # Get the result by calling the function
#     result = multiply_string(string_input, times)
    
#     # Display the result
#     print("Result:", result)

# # Run the main program
# if __name__ == "__main__":
#     main()

# #[7] Function to check if the entered string matches a specific target string
# def check_string(user_input, target_string):
#     if user_input == target_string:
#         return True
#     else:
#         return False

# # Main program
# def main():
#     # Define the specific string to check against
#     target_string = "hello"

#     # Prompt the user to enter a string
#     user_input = input("Enter a string: ")

#     # Check if the entered string matches the target string
#     if check_string(user_input, target_string):
#         print("The entered string matches the target string.")
#     else:
#         print("The entered string does not match the target string.")

# # Run the main program
# if __name__ == "__main__":
    # main()

# # [7] Define the specific string to check against
# target_string = "hello"

# # Prompt the user to enter a string
# user_input = input("Enter a string: ")

# # Check if the entered string matches the target string
# if user_input == target_string:
#     print("The entered string matches the target string.")
# else:
#     print("The entered string does not match the target string.")

