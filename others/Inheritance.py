class A:
    z = -1

    def f(self, x):
        return B(x - 1)


class B(A):
    n = 4

    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y + 1)


class C(B):
    """
    >>> C(2).n
    4
    >>> a.z == C.z
    True
    >>> a.z == b.z
    False
    >>> type(b.z.z.z)
    <class 'int'>
    """
    def f(self, x):
        return x


a = A()
b = B(1)
b.n = 5



