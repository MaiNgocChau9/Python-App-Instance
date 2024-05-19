a = [1,2,3,4,5,6,7,8,9,10]
b = [0]
for i in range(len(a)):
	b.append(b[i-1] + a[i])
b.pop(0)

print(a)
print(b)