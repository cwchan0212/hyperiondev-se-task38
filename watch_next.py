# Task 38 - Semantic Similarity (NLP)
# Compulsory Task 2
# semantic.py

# Import os, spaCy liabrary
import os, spacy
# Set an object "nlp" to store the load the model "en_core_web_md" 
nlp = spacy.load("en_core_web_md")

# Set the variable "current_directory" to store the current directory path
# Replace the backslash of the variable "current_directory" to dash
current_directory = os.getcwd().replace("\\", "/")
# Set a variable "movies" to the text file of the movies
movies_file = "movies.txt"

# Create a function "read_movies_file" to read the the text file movies.txt 
def read_movies_file():
    # Set a list "movies_list" to empty
    movies_list = []
    # Use try and except block to read the the text file movies.txt
    try:
        with open(f"{current_directory}/{movies_file}", "r") as file:
            # Set the list "movies_list" to store all elements "split_line" in the "file" object
            # i.e. 2D List
            movies_list = [[split_line.strip() for split_line in  read_line.split(":")] for read_line in file]
        # Return the list movie_list
        return movies_list
    # If it fails to read the text file "movies.txt", print the message to notify the user for checking the current directory,
    # the file location of the text file and exit the program
    except:
        print(f"Fail to read the text file {movies_file}. Please check the current directory and the file location of the text file.\n")
        exit()
# Set a variable "movie_description" to store the description of the movie
movie_description = f"Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, \
the Illuminati trick Hulk into a shuttle and launch him into space to a \
planet where the Hulk can live in peace. Unfortunately, Hulk land on the\
planet Sakaar where he is sold into slavery and trained as a gladiator." 

# Create a function "get_movie_with_the_highest_score" with the parameter "movie_description" 
# to return the title of the movie with the highest simiarity score
def get_movie_with_the_highest_score(movie_description):
    # Set a list "movies_list" to store the list returned from the function "read_movies_file"
    movies_list = read_movies_file()
    # If the variable "movies_list" and the parameter "movie_description" are not empty, 
    # calculate the similarity scores of each movies
    if movies_list and movie_description:
        # Set a nlp object "nlp_movie_description" to store the nlp object with the variable "movie_description" 
        nlp_movie_description = nlp(movie_description)
        # Use for-loop to calculate the similarity scores of all the elements of the list "movies_list"
        for index, movie in enumerate(movies_list):
            # Set a variable "similarity_score" to store the simiarity score between two movies
            similarity_score = nlp(movie[1]).similarity(nlp_movie_description)
            # Append the variable "similarity_score" to the last element of the list "movies_list"
            movies_list[index].append(similarity_score)        
        # Sort the list "movies_list" by similarity score in a descending order
        # with the use of lambda function
        movies_list.sort(key=lambda x:x[2], reverse=True)
    # Return the first element of the list "movies_list"
    return movies_list[0][0]

# Set a variable "movie_title" to store the title of the movie 
# returned from the function "get_movie_with_the_highest_score" with the parameter "movie_description"
movie_title = get_movie_with_the_highest_score(movie_description)
# Print the title of the movie withe the highest simiarity score
print(f"The movie \"{movie_title}\" gets the highest simiarity score.")
    