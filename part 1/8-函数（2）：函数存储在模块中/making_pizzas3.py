#使用as给函数指定别名以简化代码，这时可以在这个程序里重新定义一个make_pizza
from pizza import make_pizza as mp
def make_pizza():
    print("Welcome")
mp(22,'green peppers')
make_pizza()
