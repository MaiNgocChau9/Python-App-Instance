import json

# Đọc file
def read_to_anime():
    with open ('Buổi 6\data.json', "r") as f:
        data = json.load(f)
    return data

# Lưu file
def write_to_anime(data_anime):
    with open("Buổi 6\\anime.json", "w") as f:
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
        self.anime_item_dict = list()
    
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
        self.anime_item_dict.append(anime_dict)
        write_to_anime(self.anime_item_dict)
    
    def edit_item_from_dict(self, edit_title, anime_dict: AnimeItem):
        anime_edit = self.get_item_by_title(edit_title)
        anime_edit.update(anime_dict)
        # Cập nhật file JSON
        write_to_anime(self.anime_item_dict)
    
    def delete_item(self, delete_title):
        anime_delete = self.get_item_by_title(delete_title)
        self.anime_item_list.remove(anime_delete)

danhsach = AnimeList()
for item in read_to_anime():
    danhsach.add_item(item)

# main program to run anime app
while True:
    print("PHẦN MỀM QUẢN LÍ ANIME")
    print("1. Thêm anime")
    print("2. Xem anime")
    print("3. Chỉnh sửa")
    print("4. Thoát")
    choice = int(input("\nChọn chức năng: "))
    if choice == 1:
        new_anime = {
            "id": len(danhsach.anime_item_list),
            "title": input("\nTên anime: "),
            "date": input("Ngày phát hành: "),
            "image": input("Hình ảnh: "),
            "rating": float(input("Đánh giá: ")),
        }
        danhsach.add_item(new_anime)
    elif choice == 2:
        print("\nDanh sách anime:")
        for anime in danhsach.anime_item_list:
            print(f"{str(anime.id)}. {anime.title}")
    elif choice == 3:
        print("\nSửa: ")
        edit_title = input("Nhập tên anime để sửa: ")
        edit_anime = {
            "title": input("Tên anime: "),
            "date": input("Ngày phát hành: "),
            "image": input("Hình ảnh: "),
            "rating": float(input("Đánh giá: ")),
        }
        danhsach.edit_item_from_dict(edit_title, edit_anime)
    elif choice == 4:
        break