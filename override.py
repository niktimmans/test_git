class A:

    def go(self):
        print('Go, A!')

class B(A):

    def go(self, name):
        print('Go, {}'.format(name))


a = A()
b = B()

a.go()
b.go('b')