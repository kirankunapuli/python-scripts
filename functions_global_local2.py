def local():
    var = 0
    print(var)

local()
var = 100
print(var)

def glob1():
    global var
    var += 1  # Change global var
    print(var)

glob1()


def glob2():
    var = 0 # Change local var
    import thismod
    thismod.var += 1

    print(var)

glob2()

print(var)



