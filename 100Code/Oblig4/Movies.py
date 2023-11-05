
class Movies:
    def __init__(self, name, release_year, ratings):
        self.name = name
        self.release_year = release_year
        self.ratings = ratings

    def movie_info(self):
        print(f"The movie {movie_1.name} was released in {movie_1.release_year} and it has a ratings of {movie_1.ratings} stars")


movie_1 = Movies("Inception", 2010, 8.8)
movie_2 = Movies("The Martian", 2015, 8.0)
movie_3 = Movies("Joker", 2019, 8.4)

print(movie_3.movie_info())
# print(f"The movie { movie_1.name} was released in {movie_1.release_year} and it has a ratings of {movie_1.ratings} stars")
# print(f"The movie { movie_2.name} was released in {movie_2.release_year} and it has a ratings of {movie_2.ratings} stars")
# print(f"The movie { movie_3.name} was released in {movie_3.release_year} and it has a ratings of {movie_3.ratings} stars")
