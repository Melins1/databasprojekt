import mysql.connector
import program_db_config

def count_movies_by_genre():
    connection = mysql.connector.connect(**program_db_config.db_config)
    try:
        cursor = connection.cursor()

        query = """
        SELECT Genre.Name, COUNT(*) AS Movie_Count
        FROM Genre
        LEFT JOIN Movie_Genre ON Genre.Genre_ID = Movie_Genre.Genre_ID
        GROUP BY Genre.Name
        """

        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            print("Genre          Movie Count")
            print("--------------------------")
            for genre, count in results:
                print(f"{genre:<15} {count:>10}")
        else:
            print("No movies found.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if connection.is_connected():
            connection.close()

def list_directors_and_movie_count():
    connection = mysql.connector.connect(**program_db_config.db_config)
    try:
        cursor = connection.cursor()

        query = """
        SELECT Director.Name, COUNT(*) AS Movie_Count
        FROM Director
        LEFT JOIN Movie_Director ON Director.Director_ID = Movie_Director.Director_ID
        GROUP BY Director.Name
        """

        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            print("Director       Movie Count")
            print("--------------------------")
            for director, count in results:
                print(f"{director:<15} {count:>10}")
        else:
            print("No directors found.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if connection.is_connected():
            connection.close()

def count_movies_by_release_year():
    connection = mysql.connector.connect(**program_db_config.db_config)
    try:
        cursor = connection.cursor()

        query = """
        SELECT Release_Year, COUNT(*) AS Movie_Count
        FROM Movie
        GROUP BY Release_Year
        """

        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            print("Release Year   Movie Count")
            print("--------------------------")
            for release_year, count in results:
                print(f"{release_year:<15} {count:>10}")
        else:
            print("No movies found.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    count_movies_by_genre()
    list_directors_and_movie_count()
    count_movies_by_release_year()