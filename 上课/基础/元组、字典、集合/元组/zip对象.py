#zip将多个列表对应位置的元素压缩成一个元组并返回一个zip对象
a = ["aaa","bbb","ccc","ddd"]
b = [18,19,17,18]
c = [1.87,1.76,1.68,1.72]
for i in range(len(a)):
    print(f"name:{a[i]},age:{b[i]},height:{c[i]}")
d = zip(a,b,c)
for a,b,c in d:
    print(f"name:{a},age:{b},height:{c}")
