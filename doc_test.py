class C:
    def __init__(self):
        self._x = 1

        @property # x - property(x)
        def x(self):
            "I'm the 'x' property."
            return self._x

        @x.setter
        def x(self , value):
            self._x = value

        @x.deleter
        def x(self):
            del self._x


if __name__ == '__main__':
    c = C()
    print(c.x)       # c.getx()
    c.x = 2          # c.setx(2)
    # del c.x         # c.delx()
    print(C.x.__doc__)