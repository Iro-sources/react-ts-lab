my_list = [200, "cola", "coffee", 45]
print(my_list[0])

my_list[2] = "tea"
print(my_list)

#List slicing
my_list = [200, "cola", "coffee", 45]
print(my_list[2:])
print(my_list[:3])
print(my_list[1:3])

#List in a list
mix_list = [["fruits", "clothes", "medicine", "cosmetic"]]
print(mix_list[0][2])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[1])
print(spam[0][1])
print(spam[1][3])

#List Concatenation and List Replication
fruits = ["apple", "banana", "orange", "grape", "mango"]
clothes = ["shirt", "jeans", "jacket", "skirt", "hat"]
medicine = ["aspirin", "ibuprofen", "antibiotic", "vitamin C", "bandage"]
cosmetic = ["lipstick", "foundation", "eyeliner", "mascara", "blush"]

new_list = fruits + cosmetic
print(new_list)

new_list = new_list + [1, 5, 7, 9]
print(new_list)

#Removing Values from Lists with del Statements
del new_list[10:]
print(new_list)

del cosmetic[0]
print(cosmetic)


