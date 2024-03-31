class Homework:
    def __init__(self, name, priority, completed):
        self.name = name
        self.priority = priority
        self.completed = completed
    
class HomeworkList:
    def __init__(self):
        self.items = []
        self.un_finished = []
    
    def add(self, item):
        self.items.append(item)
    
    def all_finished(self):
        self.un_finished = []
        for i in range(len(self.items)):
            if self.items[i].completed == False:
                self.un_finished.append(self.items[i])
        return True

# Tạo danh sách các bài tập
homeworklist = HomeworkList()

"""
 ==== TEST ====
# Thêm các bài tập vào danh sách
homeworklist.add(Homework("Lập trình App Producer", 3, True))
homeworklist.add(Homework("Làm văn", 2, False))
homeworklist.add(Homework("Lập trình Gamemaker", 1, False))

# Kiểm tra
homeworklist.all_finished()

for item in homeworklist.un_finished:
    print("Tên:", item.name)

    print("Mức độ quan trọng: ", end="")
    if item.priority == 3: print("Cao")
    elif item.priority == 2: print("Trung bình")
    elif item.priority == 1: print("Thấp")
    else: print("Không xác định")

    if item.completed == True: print("Đã hoàn thành")
    else: print("Chưa hoàn thành")
    print()
"""

# Main program
while True:
    print("PHẦN MỀM QUẢN LÍ BÀI TẬP")
    print("1. Thêm bài tập")
    print("2. Xem bài tập chưa hoàn thành")
    print("3. Thoát")
    choice = int(input("\nChọn chức năng: "))

    if choice == 1:
        while True:
            name = input("\nTên: ")
            if name == "": break
            priority = int(input("Mức độ quan trọng ( 1: Thấp | 2: Trung bình | 3: Cao ): "))
            completed = input("Đã hoàn thành (y/n): ")
            if completed == "y": completed = True
            else: completed = False
            homeworklist.add(Homework(name, priority, completed))
    elif choice == 2:
        print("\nNHỮNG BÀI TẬP CHƯA HOÀN THÀNH")
        homeworklist.all_finished()

        for item in homeworklist.un_finished:
            print("Tên:", item.name)

            print("Mức độ quan trọng: ", end="")
            if item.priority == 3: print("Cao")
            elif item.priority == 2: print("Trung bình")
            elif item.priority == 1: print("Thấp")
            else: print("Không xác định")
            print()
    
    else: break