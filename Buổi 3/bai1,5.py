anime_1 = [input('the_id: '), input('img: '), input('title: '), input('date: '), input('rating: ')]
anime_2 = [input('the_id: '), input('img: '), input('title: '), input('date: '), input('rating: ')]
anime_3 = [input('the_id: '), input('img: '), input('title: '), input('date: '), input('rating: ')]


class AnimeItem_1:
    def __init__(self, id, img, title, date, rating):
        self.id = id
        self.img = img
        self.title = title
        self.date = date
        self.rating = rating
    
    def output(self):
        print(self.id)
        print(self.img)
        print(self.title)
        print(self.date)
        print(self.rating)
    
    def update(self):
        self.__delattr__('title')

class AnimeItem_2:
    def __init__(self, id, img, title, date, rating):
        self.id = id
        self.img = img
        self.title = title
        self.date = date
        self.rating = rating
    
    def output(self):
        print(self.id)
        print(self.img)
        print(self.title)
        print(self.date)
        print(self.rating)

class AnimeItem_3:
    def __init__(self, id, img, title, date, rating):
        self.id = id
        self.img = img
        self.title = title
        self.date = date
        self.rating = rating
    
    def output(self):
        print(self.id)
        print(self.img)
        print(self.title)
        print(self.date)
        print(self.rating)

all_anime = [AnimeItem_1, AnimeItem_2, AnimeItem_3]
all_anime.remove(AnimeItem_1)
all_anime[1].update(
    {'title':'Monono hime'}
)