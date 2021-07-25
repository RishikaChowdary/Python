#student details using function overloading
class Student:
  def input(self):
          idn=int(input('enter id:'))
          name=input('enter name:')
          branch=input('enter branch:')
          age=int(input('enter age:'))
          pno=int(input('enter mobileno:'))
  def show(self,idn=None,name=None,branch=None,age=None,pno=None):
      if((idn!=None and name!=None)and(branch!=None and age!=None)and(pno!=None)):
          print('idn:',idn,'name:',name,'branch:',branch,'age:',age,'pno:',pno)
      elif((idn!=None and name!=None)and(branch!=None and age!=None)):
          print('idn:',idn,'name:',name,'branch:',branch,'age:',age)
      elif((idn!=None and name!=None)and(branch!=None)):
          print('idn:',idn,'name:',name,'branch:',branch)
      elif(idn!=None and name!=None):
          print('idn:',idn,'name:',name)
      elif(idn!=None):
          print('idn:',idn)
      else:
          print(' ')
obj1=Student()
obj2=Student()
list=[obj1,obj2]
obj1.input()
obj2.input()
for i in list:
   i.show(idn='idn',name='name')
   i.show()
