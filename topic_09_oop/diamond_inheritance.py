class A:
    def move(self):
        print(f'Moving {self.__class__.__name__}')


class B(A):
    def move(self):
        super().move()
        print('Move like B')


class C(A):
    def move(self):
        super().move()
        print('Move like C')


class D(C, B):
    pass


class E(B, C):
    def move(self):
        super(C, self).move()  


class F(B, C):
    def move(self):
        super(B, self).move()


d = D()
e = E()
f = F()
# d.move()
# e.move()
f.move()
