# Example movie data
movies = [
    {'title': 'gita govindam', 'genre': 'romance'},
    {'title': 'Srinivasa kalyanam', 'genre': 'family'},
    {'title': 'shathamanambavathi', 'genre': 'family'},
    {'title': 'anabelle', 'genre': 'horror'}
]

def recommend_movies(movies, preferred_genre):
    """
    Returns a list of movie titles matching the preferred genre (case-insensitive).
    """
    return [movie['title'] for movie in movies if movie['genre'].lower() == preferred_genre.lower()]

# Few-shot prompting examples:
# recommend_movies(movies, 'horror') -> ['anabelle']
# recommend_movies(movies, 'Romance') -> ['gita govindam']
# recommend_movies(movies, 'family') -> ['Srinivasa kalyanam','shathamanambavathi']

if __name__ == "__main__":
    user_genre = input("Enter your preferred genre: ")
    suggestions = recommend_movies(movies, user_genre)
    if suggestions:
        print("Recommended movies:", ", ".join(suggestions))
    else:
        print("No movies found for the selected genre.")
