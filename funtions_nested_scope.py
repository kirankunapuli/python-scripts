x = 99


def f1():
    x = 88

    def f2():
        print(x)

    f2()


f1()


def f1():
    x = 99

    def f2():
        print(x)

    return f2


action = f1()
action()
