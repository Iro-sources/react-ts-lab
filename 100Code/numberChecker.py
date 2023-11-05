
def number_checker(number):

    if number % 2 == 0:
        return "odd"
    else:
        return "even"


number = int(input("Which number do you want to check? "))
result = number_checker(number)
print(f"The number {number} is {result}")



