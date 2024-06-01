import sys

l = list(range(1, 5))
i = iter(l)
while True:
    try:
        print(next(i))
    except StopIteration:
        sys.exit()


class MyTestCase:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x


case = MyTestCase()
i = iter(case)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

