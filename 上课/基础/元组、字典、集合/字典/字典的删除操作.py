#pop,popitem,clear
#pop根据key进行删除，返回删除的value，如果key不存在就报错
#popitem则是删除键值对,删除最后一个
#clear则是直接清空
person = {"name":"zhangsan","age":18,"height":220}
#第一种pop
print(person.pop("age"))#删除了这个值，返回value。然后如果key不存在的话，会报错
print(person)
#第二种 popitem
x = person.popitem()#删除最后一个，无法指定
print(x)
#第三种，clear清空
person.clear()
print(person)