#function overriding
class Base:
    def show(self):
        print('Inside base')
class Derived(Base):
    def show(self):
        super().show()
        print('Inside derived')
obj=Derived()
obj.show()
