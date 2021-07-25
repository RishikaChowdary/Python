#multithreading
from threading import*;
from time import sleep;
class SubProcess1(Thread):
    def run(self):
        for i in range(0,5):
            sleep(1)
            print('subprocess1')
class SubProcess2(Thread):
    def run(self):
        for i in range(0,5):
            sleep(1)
            print('subprocess2')
class SubProcess3(Thread):
    def run(self):
        for i in range(0,5):
            sleep(1)
            print('subprocess3')
t1=SubProcess1()
t2=SubProcess2()
t3=SubProcess3()
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print('End of program,go out..')
                
