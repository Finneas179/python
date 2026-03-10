#元组只能查询
#要一个元组 ()
a=(1,2,3,"aaa")
print(a)
#小括号可以省略
b = 1,2,3,"aaa"
print(b)
#注意如果只有一个值的话，必须有逗号，否则就是赋值
c = (1)
print(type(c))  #这个地方就是一个int
d=tuple()
print(d)
#将可迭代数据转换成元组对象
k = tuple("1234567")
print(k)
o = tuple([1,2,3,4,555,555])
print(o)