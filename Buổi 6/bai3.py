import json

class AnimeItem:
    def __init__(self, anime_id, title, date, image=None, rating=None):
        self.id = anime_id
        self.title = title
        self.date = date
        self.image = image
        self.rating = rating

# Read and print
with open ('Buổi 6\data.json', "r") as f:
    data = json.load(f)
print(data)

# Use data from json
anime_1 = AnimeItem(data[0]['id'], data[0]['title'], data[0]['date'], data[0]['image'], data[0]['rating'])

# For loop to create list
anime_list = []
for item in data:
    anime_list.append(AnimeItem(item['id'], item['title'], item['date'], item['image'], item['rating']))
print(anime_list)