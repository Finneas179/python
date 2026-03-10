def find_balance():
    """
    查看用户与密码是不是正确
    :return:具体的结果
    """
    if "aaa"=="aaa" and"ccc"=="ccc":
        return True
        """
        如果说return直接写，不带上任何的返回值，就表示结束函数操作，返回None
        你想要提前结束函数的时候就可以使用这种操作
        这就相当于，循环里面的break的操作
        """
    else:
        return False
print(find_balance())

result = find_balance()
print(f"执行后的结果:{result}")

    #当我们这个代码在后期需要使用的时候，我们需要这个结果的时候，我们就要用return