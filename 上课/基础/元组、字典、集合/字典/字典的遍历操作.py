person = {"name":"zhangsan","age":18,"height":220}
#第一种 for 获取key
for i in person:
    print(f"{i}: {person[i]}")
#第二种
for i in  person.values():
    print(f"{i}")
#第三种
for key in person.keys():
    print(f"{key}: {person[key]}")
#第四种
for i in person.items():
    print(f"{i[0]}: {i[1]}")
#第五种
person = [  {"name":"zhangsan1","age":18,"height":220},
            {"name":"zhangsan2","age":18,"height":220},
            {"name":"zhangsan3","age":18,"height":220},
            {"name":"zhangsan4","age":18,"height":220},
            {"name":"zhangsan5","age":18,"height":220}
            ]
for i in person:
    for a,b in i.items():
        print(f"{a}:{b}")

