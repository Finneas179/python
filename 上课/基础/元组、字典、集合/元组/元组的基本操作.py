a=(20,30,40)
b =(70,80,90)
c=a+b #两个拼接起来
print(a[2])
print(a[0:2])
#元组是不可以修改的，只能去访问
print(a.index(30))
print(c)
#然后如果说你写a=a+b，的话这个a是会被覆盖的

#排序
a=[20,10,30,40,70]#乱序
a.sort()#默认升序，从低往高走
#这个是原始数据，不是覆盖数据
#列表是支持可变的
print(a)
a.sort(reverse=True)
print(a)
