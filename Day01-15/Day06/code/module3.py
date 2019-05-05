def foo():
    pass


def bar():
    pass


if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
    num = int(input('请输入正整数: '))
    print('num:', num)

'''
如果我们导入的模块除了定义函数之外还中有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，
最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，
if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是“__main__”。
'''