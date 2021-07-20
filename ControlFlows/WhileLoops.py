
user_input = True

while user_input:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 118:
        user_input = False
    else:
        print("Please provide your answer in digits and ensure it is less than 118")

print(f"Your age is {age}")