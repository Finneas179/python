for i in range(1,10):
    for j in range(1,i+1):#这里要i+1，因为右边不包括
        print(f"{i}*{j} = {i*j}",end=" ")#end是未来防止换行
    print()#让他换行
else:
    print("九九乘法表，打印完毕")
