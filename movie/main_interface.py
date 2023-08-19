import program_queries
import program_procedures_functions
import program_db_config

def main():
    print("Welcome to Movie Database Explorer!")

    while True:
        print("\nMenu:")
        print("1. Count movies by genre")
        print("2. Count movies by release year")
        print("3. List directors and movie count")
        print("4. Search movie by title")
        print("5. Avg release year by genre (function)")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            program_queries.count_movies_by_genre()
        elif choice == "2":
            program_queries.count_movies_by_release_year()
        elif choice == "3":
            program_queries.list_directors_and_movie_count()
        elif choice == "4":
            program_procedures_functions.search_movie_by_title()
        elif choice == "5":
            program_procedures_functions.avg_release_year_by_genre_function()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()