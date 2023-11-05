import random

# for numbers in range(9, 102):
#     if numbers % 2 != 0:
#         print(numbers)

# print("For loop")
# def print_odd_numbers(start, end):
#     for num in range(9, 102, 2):
#         print(num)
#
#
# print_odd_numbers(9, 101)
# def print_odd_numbers(start, end):
#     for number in range(start, end + 1):
#         if number % 2 != 0:
#             print(number)

# Call the function with the desired range
# print_odd_numbers(9, 101)


# print("-----------------------")
# print("While loop")
# numbers = 9
# while numbers < 102:
#         print(numbers)
#         numbers += 2

def odds(start: int, end: int) -> "Iterator":
    yield from range(start + start % 2 - 1, end, 2)


for i in odds(9, 102):
    print(i)
#
# print()
#
# for i in odds(8, 13):
#     print(i)