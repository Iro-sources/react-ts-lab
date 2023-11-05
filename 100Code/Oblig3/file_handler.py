import Benyttmodul
from Benyttmodul import books
from Benyttmodul import my_books

def write_to_file(books, filename):

    with open(filename, "w") as file:
        for book in books:
            file.write(f"{book}, ")


filename = "books.txt"
write_to_file(books, filename)

def read_from_file(my_books, filename):
    with open(filename) as file:
        for line in file:
            contents = line.strip().split(',')
        for item in contents:
            print(contents)
    # with open(filename) as file:
    #     for line in file:
    #         contents = line[:-1]
    #         my_books.append(contents)
    #         print(contents)


filename = "books.txt"
read_from_file(my_books, filename)


# def write_to_json():







# def read_from_json():
#

