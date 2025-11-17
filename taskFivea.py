import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

#for index, item in enumerate(data)

titleInput = input("What is the movie name: ")



for index, item in enumerate(data):    
    if item["title"] == titleInput:
        print(item["title"])







