class Base1:
    def show(self):
        print('Base1')
class Base2:
    def show(self):
        print('Base 2')
class Derived(Base1,Base2):
    def show(self):
        super().show()
        super().show()
        print('Derived')
obj=Derived()
obj.show()
