import json

class AnimeItem:
    def __init__(self, anime_id, title, date, image=None, rating=None):
        self.id = anime_id
        self.title = title
        self.date = date
        self.image = image
        self.rating = rating

anime_1 = AnimeItem(1, "abc", "abc", "abc", 0)
anime_2 = AnimeItem(2, "abc_2", "abc_2", "abc_2", 0)

# Đọc với ghi file
with open("Buổi 6\data.json", "w") as f:
    json.dump(anime_1.__dict__, f, indent=4)

# Đọc và in (để xem kết quả mới nhất)
with open ('Buổi 6\data.json', "r") as f:
    data = json.load(f)
print("\nNew data:",data)