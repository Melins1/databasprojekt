import mysql.connector
import program_db_config

def search_movie_by_title():
    connection = mysql.connector.connect(**program_db_config.db_config)
    try:
        title_search = input("Enter a title search: ")
        query = """
        SELECT Movie.Movie_ID, Movie.Title, Movie.Release_Year,
               GROUP_CONCAT(DISTINCT Genre.Name) AS Genres,
               GROUP_CONCAT(DISTINCT Director.Name) AS Directors,
               GROUP_CONCAT(DISTINCT Actor.Name) AS Actors
        FROM Movie
        LEFT JOIN Movie_Genre ON Movie.Movie_ID = Movie_Genre.Movie_ID
        LEFT JOIN Genre ON Movie_Genre.Genre_ID = Genre.Genre_ID
        LEFT JOIN Movie_Director ON Movie.Movie_ID = Movie_Director.Movie_ID
        LEFT JOIN Director ON Movie_Director.Director_ID = Director.Director_ID
        LEFT JOIN Movie_Actor ON Movie.Movie_ID = Movie_Actor.Movie_ID
        LEFT JOIN Actor ON Movie_Actor.Actor_ID = Actor.Actor_ID
        WHERE Movie.Title LIKE %s
        GROUP BY Movie.Movie_ID;
        """

        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (f"%{title_search}%",))
        result = cursor.fetchall()
        cursor.close()

        if result:
            print(f"Movies matching '{title_search}':")
            for movie in result:
                print("Title:", movie["Title"])
                print("Release Year:", movie["Release_Year"])
                print("Genres:", movie["Genres"])
                print("Directors:", movie["Directors"])
                print("Actors:", movie["Actors"])
                print("-" * 30)
        else:
            print(f"No movies found matching '{title_search}'")
    finally:
        if connection.is_connected():
            connection.close()

def avg_release_year_by_genre_function():
    genre_search = input("Enter a genre search: ")
    connection = mysql.connector.connect(**program_db_config.db_config)
    try:
        cursor = connection.cursor()
        query = f"SELECT AvgReleaseYearByGenre('{genre_search}')"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()

        if result is not None:
            avg_year = result[0]
            print(f"Average release year for {genre_search} genre: {avg_year:.2f}")
        else:
            print(f"No movies found for {genre_search} genre")

    finally:
        if connection.is_connected():
            connection.close()
