def def_max(a, b, c): 
    
    max_num = a
    if b > max_num: max_num = b
    if c > max_num: max_num = c

    return max_num

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print(def_max(a, b, c))


""" 
CÁCH KHÁC :)))

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print(max(a, b, c))

"""