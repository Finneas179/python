#字典就是键值对的形式来保存数据
person = {"name":"zhangsan","age":18,"height":220}
print(person)
#在字典里面 key是不允许重复的 如果重复了 就会覆盖value的值
person = {"name":"zhangsan","age":18,"height":220,"name":"aaa"}#这里面就是把name的值变掉了
print(person)

a = dict()
print(a)