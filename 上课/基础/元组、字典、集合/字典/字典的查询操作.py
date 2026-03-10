person = {"name":"zhangsan","age":18,"height":220}
# value = person["gender"]
# print(value)
#通过get获取值
print(person.get("name"))
print(person.get("width",70))
print(person.keys())
print(person.values())
print(person.items())