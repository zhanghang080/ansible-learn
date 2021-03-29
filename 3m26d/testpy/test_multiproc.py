from Student import *
import threading

from multiprocessing import Process
from multiprocessing import Queue,Pipe,Manager

def testFunc_thread(stu:Student,func):
    print("线程：",id(stu))
    print(id(func))
    print(func)
def testFunc_process(dic,stu:Student,func):
    print("进程：",id(stu))
    print("dic id :",id(dic))
    print(id(func))
    print(func)
    
    print(dic["student"])
    print(id(dic["student"]))
    dic["student"].name = "james heller"
    print(dic["student"].infoo())
def main():
    manager = Manager()
    dic = manager.dict()
    stud = Student("alex",23,"male",100)
    
    print(id(stud))
    
    th = threading.Thread(target=testFunc_thread,args=(stud,testFunc_thread))
    th.start()
    pro = Process(target=testFunc_process,args=(dic,stud,testFunc_process))
    dic["student"] = stud
    pro.start()
    pro.join()
    th.join()
    print(stud.infoo())
    print(id(stud))
    print(type(dic))
    print(dic)
    lis1 = []
    print("dic id :",id(dic))
    print("===================")
    import time
    for i in range(20):
        
        ida = id(dic["student"])
        
        print(ida)
       
  
   
if (__name__ =="__main__"):
    main()




