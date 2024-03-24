def def_max(a, b, c): 
    
    max_num = a
    if b > max_num: max_num = b
    if c > max_num: max_num = c

    return max_num

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("Số lớn nhất trong 3 số a, b, c là:", def_max(a, b, c))


""" 
CÁCH KHÁC :)))

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print(max(a, b, c))

"""