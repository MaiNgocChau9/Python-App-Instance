import json

# doc file
def read_to_anime():
    anime_dict_list = list()
    with open("Buổi 6\data.json", "r") as f:
        data = json.load(f)

    anime_dict_list.extend(data)
    return anime_dict_list

# luu file  
def write_to_anime(data_anime):
    with open("Buổi 6\data.json", "w") as f:
        json.dump(data_anime, f)

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
        self.anime_dict_list = read_to_anime()

    def get_item_by_title(self, anime_title) -> AnimeItem:
        for anime_item in self.anime_item_list:
            if anime_item.title == anime_title:
                return anime_item
    
    def add_item(self, anime_dict):
        anime_dict["id"] = len(self.anime_item_list)
        new_item = AnimeItem(anime_dict["id"],
                             title=anime_dict["title"],
                             date=anime_dict["date"],
                             image=anime_dict["image"],
                             rating=anime_dict["rating"])
        self.anime_item_list.append(new_item)
        self.anime_dict_list.append(anime_dict)
        write_to_anime(self.anime_dict_list)

    def item_to_obj(self):
        a = list()
        for i in self.anime_item_list:
            a.append(i.__dict__)
        return a

    def edit_item_from_dict(self, edit_title, anime_dict: AnimeItem):
        anime_edit = self.get_item_by_title(edit_title)
        anime_edit.update(anime_dict)
        self.anime_dict_list = self.item_to_obj()
        write_to_anime(self.anime_dict_list)

    def delete_item(self, delete_title):
        anime_delete = self.get_item_by_title(delete_title)
        self.anime_item_list.remove(anime_delete)
        self.anime_dict_list = self.item_to_obj()
        write_to_anime(self.anime_dict_list)

danhsach = AnimeList()

danhsach.add_item({
    "anime_id": 0,
    "title": "One Piece",
    "date" : "2024",
    "image": None,
    "rating": None
})

danhsach.add_item({
    "anime_id": 1,
    "title": "One Piece 1",
    "date" : "2025",
    "image": None,
    "rating": None
})

danhsach.edit_item_from_dict("One Piece",{
    "date": "2000"
})

danhsach.delete_item("One Piece 1")

print(danhsach.anime_item_list[0].__dict__)