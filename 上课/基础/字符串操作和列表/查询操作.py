gift  = [1,2,3,4,5,1,1]
#查询元素的索引
gift[0]="aaa"
gift.remove(2)
print(gift)
index = gift.index(3)
print(index)
try:
    index = gift.index(88)
except ValueError:
    print("未找到该元素，可能不在")

sum = gift.count(1)
print(sum)