#将右边的结果赋给左边的变量进行储存
name = 'long'
print(name)
#拆包
a,b=5,6#5到a，6到b
print(a,b)
a=5
temp1=a
b=10
temp2=b
b=temp1
a=temp2
print('a:',a,'       ','b:',b)