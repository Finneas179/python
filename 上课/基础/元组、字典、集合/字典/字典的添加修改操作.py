person = {"name":"zhangsan","age":18,"height":220}
#第一种
person["name"]="aaa"
print(person)
#如果key不存在的话，就会添加一个key，如果说存在就直接修改
person["gender"]="male"
print(person)

#第二种
#使用update
person2 = {"name":"zhangsan","age":18,"height":220,"gender":"male"}
person.update(person2)
print(person)