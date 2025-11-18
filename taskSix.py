import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

#for index, item in enumerate(data)

genreInput = input("What is the genre: ")

for movie in data:
    for item in movie["genres"]:
        if item == genreInput:
            print(movie["title"])







