
movies = [{"name": "Inception", "year": 2010, "rating": 8.7},
               {"name": "Inside Out", "year": 2015, "rating": 6.9},
               {"name": "Con Air", "year": 1997, "rating": 6.9}]


options = input("\n#### Welcome here are your options###\n"
           "Type 'a' to add to the list\n"
            "type 's' to see movies in the list\n"
            "type 'r' to delete a movie from the list\n")


def add_movie(movies, name, year, rating, options):
    if options == 'a':
        new_movie_name = input("Enter movie name: ")
        new_movie_year = input("Enter movie year: ")
        new_movie_rating = input("Enter movie rating: ")
        new_movie = {"name": new_movie_name, "year": int(new_movie_year), "rating": new_movie_rating}
        movies.append(new_movie)
    elif options == 's':
        print(movies)

    elif options == 'r':
        movie_to_remove = input("Enter a name to remove a movie: ")
        # new_movies = movies[:]
        # for movie in new_movies:
        #     if movie["name"] != movie_to_remove:
                #movie.remove(new_movies)
                # print(f"{movie} was deleted")
                # return new_movies
        movies[:] = [movie for movie in movies if movie["name"] != movie_to_remove]

        return movies


updated_movies = add_movie(movies, name="name", year="year", rating="rating", options=options)
print(updated_movies)


