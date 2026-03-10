#range(开始位置，结束位置，步长)
#开始位置：从哪个数字开始 默认是0 可以写也可以不写
#结束位置：到那个数字结束，必须写
#步长：设置步长 可以写也可以不设置
for i in range(10):  #包头不包尾
    print(i,end=" ")
print()
for  i in range(10,0,-1):
    print(i,end=" ")
print()
for i in range(-10,-15,-1):
    print(i,end=" ")
