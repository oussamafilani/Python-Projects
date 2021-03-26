class C:
    def __init__(self):
        self._x = 1

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


if __name__ == '__main__':
    c = C()
    print(c.x)       # c.getx()
    c.x = 2          # c.setx(2)
    # del c.x         # c.delx()
    print(C.x.__doc__)