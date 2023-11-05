
movies = [{"name": "Inception", "year": 2010, "rating": 8.7},
               {"name": "Inside Out", "year": 2015, "rating": 6.9},
               {"name": "Con Air", "year": 1997, "rating": 6.9}]

#adedd the list variable 'movies' to reference by which list to update
#made the rating as default incase a movie has no ratings it will automatically give this rating '5.0'
def add_movie(movies, name, year, rating=5.0):
    new_movies = {"name": name, "year": year, "rating":rating}

    movies.append(new_movies)
    return movies

def print_movies(new_movies):
    for film in new_movies:
        print(f"{film['name']} - {film['year']} has a rating of {film['rating']}")

print()

#Lag en funksjon som tar en liste med filmer og regner ut gjennomsnittsratingen
#for alle filmene i lista og returnerer dette. Test funksjonen og skriv ut gjennomsnittet.
def calculate_rating(movies_rating):
    total_ratings = 0
    for movie in movies:
        total_ratings += movie["rating"]
    average_rating = total_ratings / len(movies)
    return average_rating


result = calculate_rating(movies_rating=movies)
print(f"The total average rating of the movies are: {result}")

print()

def movies_in_year_2010(movies, release_year):
    movies_until_2010 = []
    for movie in movies:
        if movie["year"] >= release_year:
            movies_until_2010.append(movie)
    return movies_until_2010


release_year = 2010
result = movies_in_year_2010(movies, release_year)
for movie in result:
    print(f"name:{movie['name']} year: {movie['year']}")



print("*******With the new movies********")
updated_movies = add_movie(movies, "Allied", 2009, 5.7)
updated_movies = add_movie(movies, "Fight Club", 2012, 6.1)
updated_movies = add_movie(movies, "Shaw Kank Redemption", 1994, 10.0)
updated_movies = add_movie(movies, "Race", 1879, )


print_movies(movies)
print()

#printing the average ratings
result = calculate_rating(movies_rating=movies)
print(f"The total average rating of the movies are: {round(result,2)}")
# for movie in updated_movies:
#     print(movie)
# print("############################")

#print(updated_movies)
#
# Dictionaries
# def add_new_country(country, visits, list_of_cities):
#     new_countries = {"country": country, "visits": visits, "cities": list_of_cities}
#     travel_log.append(new_countries)
#             OR
# def add_new_country(country, visits, list_of_cities):
#     new_countries = {}
#     new_countries["country"] = country
#     new_countries["visits"] = visits
#     new_countries["cities"] = list_of_cities
#     travel_log.append(new_countries)