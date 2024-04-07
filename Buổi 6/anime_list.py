import json

# Đọc file
def read_to_anime():
    with open ('Buổi 6\data.json', "r") as f:
        data = json.load(f)
    return data

# Lưu file
def write_to_anime(data_anime):
    with open("Buoi 6\data.json", "w") as f:
        json.dump(data_anime, f, indent=4)

class AnimeItem:
    def __init__(self, anime_id, title, date, image, rating):
        self.id = anime_id
        self.title = title
        self.date = date  
        self.image = image
        self.rating = rating
        
    def update(self, new_data: dict):
        for k, v in new_data.items():
            if v:
                setattr(self, k, v)

class AnimeList:
    def __init__(self):
        self.anime_item_list = list()
    
    def get_item_by_title(self, anime_title) -> AnimeItem:
        for anime_item in self.anime_item_list:
            if anime_item.title == anime_title:
                return anime_item
    
    def add_item(self, anime_dict):
        anime_dict["id"] = len(self.anime_item_list)
        new_item = AnimeItem(anime_id=anime_dict["id"],
                             title=anime_dict["title"],
                             date=anime_dict["date"],
                             image=anime_dict["image"],
                             rating=anime_dict["rating"])
        self.anime_item_list.append(new_item)
    
    def edit_item_from_dict(self, edit_title, anime_dict: AnimeItem):
        anime_edit = self.get_item_by_title(edit_title)
        anime_edit.update(anime_dict)
    
    def delete_item(self, delete_title):
        anime_delete = self.get_item_by_title(delete_title)
        self.anime_item_list.remove(anime_delete)

danhsach_anime = read_to_anime()
print(danhsach_anime)
danhsach = []
for item in danhsach_anime:
    print(item)
    # anime = AnimeItem(item["id"], item["title"], item["date"], item["image"], item["rating"])
    danhsach.append(AnimeList.add_item(item))
print(danhsach)