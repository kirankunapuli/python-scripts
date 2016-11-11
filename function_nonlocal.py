def tester(start):
    state = start
    def nested(label):

        print(label, state)
        # state += 1
    return nested

F = tester(0)
F('spam')
F('eggs')
F('bacon')
