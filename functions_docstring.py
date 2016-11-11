def Hello(name='everybody'):
    """Greets a person"""
    print('Hello' + name + "!")


print("The docstring of the function Hello: " + Hello.__doc__)
