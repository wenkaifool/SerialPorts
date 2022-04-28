# https://blog.csdn.net/qq_38787214/article/details/87902291

class Root(object):
    def __init__(self):
        self.x = '这是属性'

    def fun(self):
        print(self.x)
        print('这是方法')


class A(Root):
    def __init__(self):
        print('实例化时执行')


test = A()  # 实例化类
test.fun()  # 调用方法
test.x  # 调用属性
# 结果： 可以看到此时父类的方法继承成功，可以使用，但是父类的属性却未继承，并不能用


