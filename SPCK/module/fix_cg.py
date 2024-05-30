import json

json_product = json.load(open("product.json"))
json_category = json.load(open("Data/categorys.json"))

# Khởi tạo số lượng sản phẩm cho mỗi danh mục là 0
for category in json_category:
    category["product"] = 0

# Đếm số lượng sản phẩm cho mỗi danh mục
for product in json_product:
    for category in json_category:
        if category["name"] == product["category"]:
            category["product"] += 1

# Ghi đồi file JSON
json.dump(json_category, open("Data/categorys.json", "w"), indent=4, ensure_ascii=False)