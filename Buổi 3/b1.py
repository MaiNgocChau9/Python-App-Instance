class Information():
    def __init__(self, id, img, title, date, rating):
        self.id = id
        self.img = img
        self.title = title
        self.date = date
        self.rating = rating
    
    def print(self):
        print(self.id)
        print(self.img)
        print(self.title)
        print(self.date)
        print(self.rating)


a = Information(input('id: '), input('img: '), input('title: '), input('date: '), input('rating: '))
a.print()