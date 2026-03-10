#猜心跳
import random
heartbeat = random.randint(70,120)
userbeat = 0
while True:
    userbeat = int(input("你猜测的心跳:"))
    if userbeat>heartbeat:
        print("大了")
    elif userbeat<heartbeat:
        print("小了")
    else:
        print("猜对了")