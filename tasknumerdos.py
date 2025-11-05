import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for index, item in enumerate(data):
    print(index, ":", item["title"])



yr = int(input)






#After accepting user input, print all movies that released AFTER a given year.