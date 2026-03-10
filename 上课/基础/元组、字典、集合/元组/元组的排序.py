a=[10,20,40,30]
#python自带的排序是生成新的对象
b = sorted(a,reverse=True)
print(b)
print(a)
a=tuple(b)
print(a)