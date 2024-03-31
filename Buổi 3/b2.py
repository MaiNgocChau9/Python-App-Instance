all_items_information = [
    [input('the_id: '), input('img: '), input('title: '), input('date: '), input('rating: ')],
    [input('the_id: '), input('img: '), input('title: '), input('date: '), input('rating: ')],
    [input('the_id: '), input('img: '), input('title: '), input('date: '), input('rating: ')],
]
print(all_items_information[1])

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

for i in range(len(all_anime)):
    print(all_anime[i].__name__)
    all_anime[i].__init__(all_items_information[i])

for i in range(len(all_anime)):
    all_anime[i].output()