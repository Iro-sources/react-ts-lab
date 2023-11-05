import random

options = ("\n#### Welcome here are your options###\n"
           "Type '1' to add to the list\n"
            "type '2' to see the full list\n"
            "type '3' to delete an item from the list\n"
            "type 'quit' to exit the system")
my_shopping_list = []

msg = " "
while msg != 'quit':
    print(options)
    msg = input(": ")

    if msg == '1':
        item = input("add an item to the list: ")
        my_shopping_list.append(item)

    elif msg == '2':
        for items in my_shopping_list:
            print(items)
        else:
            print("The cart is empty")

    elif msg == '3':
        item = input("Type an item to remove from the list: ")
        if item in my_shopping_list:
            my_shopping_list.remove(item)
            print(f"{item} removed from the list")
        else:
            print("OOps! item not in the list")

else:
    print(options)