def main():
    # Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Srinjoy Chatterjee", 
        "student_id": 10323958, 
        "pizza_toppings": ["Pepperoni", "Chicken", "Onions"],
        "movies": [
            {"title": "Titanic", "genre": "Romantic"},
            {"title": "Dangal", "genre": "Sports Drama"}
        ]
    }

    # Step 3 - Add another movie to the data structure
    new_movie = {"title": "KGF chapter 1", "genre": "action-drama"}
    about_me["movies"].append(new_movie)
    # Display the student's full name and ID
    print_student_name_and_id(about_me)
    # Show the initial list of favorite pizza toppings
    print_pizza_toppings(about_me)
    # Add additional pizza toppings to the list
    add_pizza_toppings(about_me, ["Mushrooms", "Spinach"])
    # Show the updated list of favorite pizza toppings
    print_pizza_toppings(about_me)
    # Display the genres of the student's favorite movies
    print_movie_genres(about_me)
    # Display the titles of the student's favorite movies
    print_movie_titles(about_me['movies'])

# Step 4 - Function that prints student name and ID
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split(" ")[0]
    student_id = about_me['student_id']
    print(f"My name is {full_name}, but you can call me Mr. {first_name}.")
    print(f"My student ID is {student_id}.\n")


# Step 5 - Function that adds pizza toppings to the data structure
def add_pizza_toppings(about_me, toppings):
    # Add the new toppings to the existing list
    about_me['pizza_toppings'].extend(toppings)
    # Eliminate duplicates, convert to lowercase, and sort alphabetically
    about_me['pizza_toppings'] = sorted({topping.lower() for topping in about_me['pizza_toppings']})



# Step 6 - Function that prints a bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favorite pizza toppings are:")
    print("\n".join(f"- {topping.capitalize()}" for topping in about_me['pizza_toppings']))
    print()



# Step 7 - Function that prints a comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie['genre'] for movie in about_me['movies']]
    print(f"I like to watch {', '.join(genres)} movies.\n")


# Step 8 - Function that prints a comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie['title'] for movie in movie_list]
    print(f"Some of my favorite movies are {', '.join(titles)}!\n")


if __name__ == '__main__':
    main()
