#Employee management system
class Emp:
    def input(self):
        self.id=int(input('enter employee id:'))
        self.name=input('enter employee name:')
        self.dept=input('enter employee department:')
        self.pos=input('enter employee position:')
        self.dob=input('enter employee dob:').split('-')
        self.doj=input('enter employee doj:').split('-')
    def CalAge(self,E_dob):
        dob_day=int(E_dob[0])
        dob_month=int(E_dob[1])
        dob_year=int(E_dob[2])
        cur_day=26
        cur_month=11
        cur_year=2019
        age_day=cur_day-dob_day
        age_month=cur_month-dob_month
        age_year=cur_year-dob_year
        self.age=print(age_day,'days',age_month,'months',age_year,'years')
    def CalExperience(self,E_doj):
        doj_day=int(E_doj[0])
        doj_month=int(E_doj[1])
        doj_year=int(E_doj[2])
        cur_day=26
        cur_month=11
        cur_year=2019
        exp_day=cur_day-doj_day
        exp_month=cur_month-doj_month
        exp_year=cur_year-doj_year
        self.experience=print(exp_day,'days',exp_month,'months',exp_year,'years')
    def Show(self):
        print(self.id,' ',self.name,' ',self.dept,' ',self.pos)
obj1=Emp()
obj2=Emp()
obj3=Emp()
obj1.input()
obj1.CalAge(obj1.dob)
obj1.CalExperience(obj1.doj)
obj1.Show()

