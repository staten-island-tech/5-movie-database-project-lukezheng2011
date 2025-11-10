import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

#for index, item in enumerate(data)

yr = input("Which year would you like to see the movies released after: ")


for i in range(2026):
    if i >= yr:
        print(data[i]["title"])







#After accepting user input, print all movies that released AFTER a given year.