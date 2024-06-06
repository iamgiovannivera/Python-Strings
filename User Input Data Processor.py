# 2. User Input Data Processor

# def validate_name_length(first_name, last_name):
#     if len(first_name) < 2:
#         print("First name must be at least 2 characters long.")
#     if len(last_name) < 2:
#         print("Last name must be at least 2 characters long.")

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# validate_name_length(first_name, last_name)

# Task 2:
    
    
# import re

# def check_password_complexity(password):
#     if len(password) < 8:
#         print("Password must be at least 8 characters long.")
#     elif not re.search(r'[A-Z]', password):
#         print("Password must contain at least one uppercase letter.")
#     elif not re.search(r'[a-z]', password):
#         print("Password must contain at least one lowercase letter.")
#     elif not re.search(r'[0-9]', password):
#         print("Password must contain at least one number.")
#     else:
#         print("Password is valid.")

# password = input("Enter your password: ")
# check_password_complexity(password)

# Task 3: 
    
# def format_email(email):
#     return email.lower().strip()

# email = input("Enter your email address: ")
# formatted_email = format_email(email)
# print(f"Formatted Email: {formatted_email}")