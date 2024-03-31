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