
movies = [{"name": "Inception", "year": 2010, "rating": 8.7},
               {"name": "Inside Out", "year": 2015, "rating": 6.9},
               {"name": "Con Air", "year": 1997, "rating": 6.9}]

#Writing to a file using function
def write_to_file(movies, filename):
    with open(filename, "w") as file:

        for movie in movies:
            file.write(f"name: {movie['name']} - {movie['year']} has a rating of {movie['rating']}\n")



filename = "movies.txt"
write_to_file(movies, filename)

#Reading from file using function
def read_from_file(filename):
    with open(filename, "r") as file:
        contents = file.read()
        print(contents)


filename = "movies.txt"
read_from_file(filename)
