class ghe:
    def __init__(self, chan_ghe, cho_ngoi, ghe_tua):
        self.chan_ghe = chan_ghe
        self.cho_ngoi = cho_ngoi
        self.ghe_tua = ghe_tua
        
    def XuatThongTin(self):
        print("Chan ghe:", self.chan_ghe)
        print("Cho ngoi:", self.cho_ngoi)
        print("Ghe tua:", self.ghe_tua)
ghe = ghe("gỗ", "gỗ", "nhựa")
ghe.XuatThongTin()