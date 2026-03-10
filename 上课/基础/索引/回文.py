text = input("请输入一段回文：我来验证")
print(text,end=" ")
print(text[::-1])
if text == text[::-1]:
    print("是")
else:
    print("否")