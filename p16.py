#passing object as arguments to the member function of class and returning objects
class Time:
    def input(self):
        self.t1=input('enter first time:').split(':')
        self.t2=input('enter second time:').split(':')
    def addTime(self,Object):
        temp=Time()
        self.t1_hrs=int(t1[0])
        self.t1_mins=int(t1[1])
        self.t1_sec=int(t1[2])
        self.t2_hrs=int(t2[0])
        self.t2_mins=int(t2[1])
        self.t2_sec=int(t2[2])
        temp.t3_hrs=self.t1_hrs+Object.t2_hrs
        temp.t3_mins=self.t1_mins+Object.t2_mins
        temp.t3_sec=self.t1_sec+Object.t2_sec
        temp.t3=temp.t3_hrs:temp.t3_mins:temp.t3_sec
        if(temp.t3_hrs>23):
            t3=00:00:00
        if(temp.t3_mins>59):
            t3_hrs=t3_hrs+1
        if(temp.t3_sec>59):
            t3_mins=t3_mins+1
        return temp


        
        
