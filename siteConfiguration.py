

class Visitor(metaclass=SiteConfiguration):

    counter = 0

    def __init__(self):

        Visitor.counter += 1

    x = Visitor()
    print(x.counter)

    y = Visitor()
    print(y.counter)
