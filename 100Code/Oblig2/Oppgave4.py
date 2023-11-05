books = ["The Hobbit", "Farmer", "Giles of Ham", "Lord of the Rings: The Fellowship of the Ring",
         "Lord of the Rings: The Two Towers", "Lord of the Rings: The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]

my_list = []

for book in books:
    if "Lord of the Rings:" in book:
        my_list.append(book)

print(my_list)


