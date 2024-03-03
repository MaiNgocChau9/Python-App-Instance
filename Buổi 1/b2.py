class hinh_chu_nhat:
    def __init__ (self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    def chu_vi(self):
        return (self.dai + self.rong) * 2
    
    def dien_tich(self):
        return self.dai * self.rong

hinh_chu_nhat = hinh_chu_nhat(float(input("Nhập chiều dài: ")), float(input("Nhập chiều rộng: ")))
print("Chu vi:",hinh_chu_nhat.chu_vi())
print("Diện tích:",hinh_chu_nhat.dien_tich())