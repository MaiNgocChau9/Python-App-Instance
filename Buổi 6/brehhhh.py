import json

class AnimeItem:
    def __init__(self, anime_id, title, date, image=None, rating=None):
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
        self.list = []
    
    def add(self, anime: AnimeItem):
        self.list.append(anime)
    
    def remove(self, id: int):
        for i in self.list:
            if i.id == id:
                self.list.remove(i)
                break
    def update(self, id: int, new_data: dict):
        for i in self.list:
            if i.id == id:
                i.update(new_data)
                break
    
    def find(self, id: int):
        for i in self.list:
            if i.id == id:
                return i
    def output(self):
        for i in self.list:
            print(i)
