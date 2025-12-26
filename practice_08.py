
""""


Movie Streaming Platform Management System
We have track user search history, watched movies, and ratings given by users to movies.
provide recommendations based on search history ,ratings and watched movies.


"""


class MovieStreamingPlatform:

    def __init__(self, platform_name):
        self.platform_name = platform_name
        self.user_list = []
        self.movies_list = {}

        # FIX: must be dict, not set
        self.user_watch_history = {}
        self.user_ratings_history = {}
        self.user_search_history = {}

    # ----------------- CHECKS -----------------

    def is_user_exist(self, user_id):
        return user_id in self.user_list

    def is_movies_exist(self, movie_id):
        return movie_id in self.movies_list

    def is_movie_watched_by_user(self, user_id, movie_id):
        if not self.is_user_exist(user_id):
            print(f"please ensure that this user id : {user_id} exist!!")
            return False

        if not self.is_movies_exist(movie_id):
            print(f"please ensure that this movie id : {movie_id} exist!!")
            return False

        return movie_id in self.user_watch_history[user_id]

    # ----------------- SEARCH -----------------

    def return_search_movie_from_platform(self, search_term):
        search_term = search_term.strip().lower()
        search_unique_movie_id = set()

        for movie_id, movie in self.movies_list.items():
            title = movie['title'].lower()
            for ch in search_term:
                if ch in title:
                    search_unique_movie_id.add(movie_id)
                    break

        return search_unique_movie_id

    def add_user_search_history(self, user_id, search_term):

        if not self.is_user_exist(user_id):
            print(f"please ensure that this user id : {user_id} exist!!")
            return

        user_search_movie = self.return_search_movie_from_platform(search_term)
        self.user_search_history[user_id].update(user_search_movie)

    # ----------------- RECOMMENDATION -----------------

    def user_movie_recommendation(self, user_id):

        if not self.is_user_exist(user_id):
            print(f"please ensure that this user id : {user_id} exist!!")
            return []

        search_history = self.user_search_history.get(user_id, set())
        rating_history = self.user_ratings_history.get(user_id, {})
        watch_history = self.user_watch_history.get(user_id, set())

        recommended_movies = set()
        recommended_movies_title = set()


        for movie_id in search_history:

            if movie_id not in recommended_movies:
                recommended_movies.add(movie_id)

        for movie_id in rating_history:
                
            if movie_id not in recommended_movies:
           
                recommended_movies.add(movie_id)

        for movie_id in watch_history:
                
            if movie_id not in recommended_movies:
           
                recommended_movies.add(movie_id)

        for movie_id in recommended_movies:
            recommended_movies_title.add(self.movies_list[movie_id]['title'])

        return recommended_movies_title

    # ----------------- Adding   MOVIE -----------------

    def add_movie(self, movie_id, title, genre, duration):

        if self.is_movies_exist(movie_id):
            print(f" this id : {movie_id} movie already exist!!")
            return

        self.movies_list[movie_id] = {
            'title': title,
            'genre': genre,
            'duration': duration
        }

    # ----------------- Adding   User -----------------


    def add_user(self, user_id):

        if self.is_user_exist(user_id):
            print(f" this id : {user_id} user already exist!!")
            return

        self.user_list.append(user_id)
        self.user_watch_history[user_id] = set()
        self.user_ratings_history[user_id] = {}
        self.user_search_history[user_id] = set()

    # ----------------- WATCH & RATE -----------------

    def add_record_watch(self, user_id, movie_id):

        if not self.is_user_exist(user_id):
            print(f"please ensure that this user id : {user_id} exist!!")
            return

        if not self.is_movies_exist(movie_id):
            print(f"please ensure that this movie id : {movie_id} exist!!")
            return

        self.user_watch_history[user_id].add(movie_id)

    def add_user_rating(self, user_id, movie_id, rating, comments):

        if not self.is_movie_watched_by_user(user_id, movie_id):
            print(f" please ensure that user id : {user_id} has watched movie id : {movie_id} !!")
            return

        self.user_ratings_history[user_id][movie_id] = {
            'rating': rating,
            'comments': comments
        }



if __name__ == "__main__":
    platform = MovieStreamingPlatform("Netflix")

    platform.add_user("user1")
    platform.add_user("user2")

    platform.add_movie("movie1", "The Great Adventure", "Action", 120)
    platform.add_movie("movie2", "Romantic Escape", "Romance", 90)
    platform.add_movie("movie3", "Mystery Manor", "Mystery", 110)

    platform.add_record_watch("user1", "movie1")
    platform.add_user_rating("user1", "movie1", 5, "Amazing movie!")

    platform.add_user_search_history("user1", "Romantic")



    
    
    platform.add_user_search_history("user2", "M")   
    recommendations = platform.user_movie_recommendation("user2")
    
    print(f"Recommended movies for user2: {recommendations}")



    recommendations = platform.user_movie_recommendation("user1")
    print(f"Recommended movies for user1: {recommendations}")




    







       