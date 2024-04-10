import json
class Animal:
    def __init__(self, name, species, sound, weight):
        self.name = name
        self.species = species
        self.sound = sound
        self.weight = weight


animals = [
    Animal("Hổ mang", "Bò sát", "rít", 10),
    Animal("Sư tử", "Có vú", "gầm gừ", 150),
    Animal("Vẹt", "Chim", "hót", 0.5),
]
    
sorted_animals = sorted(animals, key=lambda animal: animal.weight)
"""
Giải thích: Sắp xếp danh sách động vật theo trọng lượng

Hàm sorted() thường yêu cầu hai giá trị:
- Danh sách hoặc chuỗi cần sắp xếp: Trong trường hợp này là danh sách animals.
- Hàm khóa (key function): Hàm này xác định cách sắp xếp các phần tử. Trong trường hợp này, hàm lambda được sử dụng để truy xuất trọng lượng của mỗi động vật và sắp xếp chúng theo thứ tự tăng dần.

Cú pháp: sorted(string/list], key=key_function)
"""

animal_data = []
for animal in animals:
    animal_data.append({"name": animal.name, "weight": animal.weight})

with open("Buổi 6\\BTVN\\animals.json", "w", encoding="utf-8") as f:
    json.dump(animal_data, f, indent=4, ensure_ascii=False)

""" 
Giải thích: THAM SỐ ENSURE_ASCII

Tham số ensure_ascii xác định liệu các ký tự Unicode trong dữ liệu JSON có được mã hóa thành các ký tự ASCII hay không.

Nếu ensure_ascii được đặt thành True (mặc định), thì tất cả các ký tự Unicode trong dữ liệu JSON sẽ được mã hóa thành các ký tự ASCII.
Ví dụ: "Vẹt" -> "V\u1eb9t"

Nếu ensure_ascii được đặt thành False, thì các ký tự Unicode trong dữ liệu JSON sẽ không được mã hóa thành các ký tự ASCII. Điều này sẽ đảm bảo rằng tất cả dữ liệu được bảo toàn khi được lưu vào tệp JSON.
Ví dụ: "Vẹt" -> "Vẹt"
"""