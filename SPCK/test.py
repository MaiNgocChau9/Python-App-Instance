import unidecode

# Chuỗi có dấu tiếng Việt
chuoi_co_dau = "Đây là ví dụ về chuỗi có dấu tiếng Việt."

# Sử dụng unidecode để loại bỏ dấu
chuoi_khong_dau = unidecode.unidecode(chuoi_co_dau)