class A:
    def method_a(self):
        print("From A")

class B:
    def method_b(self):
        print("From B")

class C(A, B):
    pass

c = C()
c.method_a()
c.method_b()

