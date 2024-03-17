class AnimeItem_1:
    def __init__(self, id, img, title, date, rating):
        self.id = id
        self.img = img
        self.title = title
        self.date = date
        self.rating = rating

class AnimeItem_2:
    def __init__(self, id, img, title, date, rating):
        self.id = id
        self.img = img
        self.title = title
        self.date = date
        self.rating = rating

class AnimeItem_3:
    def __init__(self, id, img, title, date, rating):
        self.id = id
        self.img = img
        self.title = title
        self.date = date
        self.rating = rating

all_anime = [AnimeItem_1, AnimeItem_2, AnimeItem_3]
for i in range(len(all_anime)):
    print(all_anime[i].__name__)
    all_anime[i].__init__(input('id: '), input('img: '), input('title: '), input('date: '), input('rating: '))

for i in range(len(all_anime)):
    print(all_anime[i].__name__)
    print(all_anime[i].id)
    print(all_anime[i].img)
    print(all_anime[i].title)
    print(all_anime[i].date)
    print(all_anime[i].rating)