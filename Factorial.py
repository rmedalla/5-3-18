user_input = int(input("Enter a number to see it's factorial: "))

def factorial(user_input):
    if user_input == 0:
        return 1
    else:
        return user_input * factorial(user_input-1)

print(factorial(user_input))
