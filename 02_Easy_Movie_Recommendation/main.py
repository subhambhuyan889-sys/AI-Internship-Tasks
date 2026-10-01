MOVIES = {
    "action": ["The Dark Knight", "Avengers: Endgame", "Gladiator"],
    "comedy": ["3 Idiots", "The Hangover", "Home Alone"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Pursuit of Happyness"],
    "sci-fi": ["Interstellar", "Inception", "The Martian", "Arrival"],
    "animation": ["Toy Story", "Coco", "The Lion King"],
}


def recommend_movies(genre):
    genre = genre.strip().lower()
    return MOVIES.get(genre)


def run_recommender():
    print("Movie Recommendation System")
    print("Available genres:", ", ".join(MOVIES))

    genre = input("Enter your preferred genre: ")
    movies = recommend_movies(genre)

    if movies is None:
        print("Sorry, that genre is not available.")
        return

    print(f"Recommended {genre.title()} movies:")
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie}")


if __name__ == "__main__":
    run_recommender()
