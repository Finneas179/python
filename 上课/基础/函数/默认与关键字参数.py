#默认参数必须写在常规写法的后面
def add(a,b=10):
    """
    :param a:
    :param b:
    :return:
    """
    return a+b

print(add(20))#这样的话没有传递b的话，就是直接用默认值
