anon_object_2 = type("", (), {})()

foo = type("", (), dict(y=1))()

print(foo.y == 1)

def anonymous(cls):
    return cls()


@anonymous
class foo:

    x = 42

    def bar(self):
        return self.x


