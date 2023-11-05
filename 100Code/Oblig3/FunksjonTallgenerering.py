import random

def generate_random_number():
    number = random.randrange(0, 100)
    print("*********")
    print(number)
    print("*********")


for num in range(5):
    generate_random_number()

#'02d:' is a format you can use when you want to control how a random_num variable is displayed

