import json

class AnimeItem:
    def __init__(self, anime_id, title, date, image=None, rating=None):
        self.id = anime_id
        self.title = title
        self.date = date
        self.image = image
        self.rating = rating

# Đọc và in
with open ('Buổi 6\data.json', "r") as f:
    data = json.load(f)
print(data)

# Đọc với ghi file
new_data = {"name": "abc", "title": "abc", "date": "abc", "image": "abc", "rating": "abc"}
with open("Buổi 6\data.json", "w") as f:
    json.dump(new_data, f)

# Đọc và in (để xem kết quả mới nhất)
with open ('Buổi 6\data.json', "r") as f:
    data = json.load(f)
print(data)