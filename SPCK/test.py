import json

a = {"user_name": "maingocchau"}
json_f = [
    {
        "user_name": "maingocchau",
        "password": "123456789",
        "email": "chauaurora9@gmail.com",
        "name": "Mai Ngọc Châu"
    }
]

# Kiểm tra xem a có trong json_f hay không
user_exists = any(user["user_name"] == a["user_name"] for user in json_f)

print("User exists:", user_exists)