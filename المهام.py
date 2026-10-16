import time
list_task=[]
def massege():
    print("*"*50)
    print("welcom to the to_do list app! ")
    print("choose an option:")
    print("1. add task ")
    print("2. view tasks ")
    print("3. delet task")
    print("4. exite ")
    print("*"*50)
i=0
while i<5 : 
    massege()
    
    choise=input("enter your choise (1_4):\n ")
    if choise == "1":
       add_task=input("enter your task:\n ")

       list_task.append(add_task)
       i+=1
       print("### task add ###")
       print("*" *50)

    elif choise =="2":
        if not list_task:
            print("no tasks add yet: ")
        else:
            
            i=1
            for d in list_task:
                print(f"your tasks is {i,d}")
                i+=1
            
    
    elif choise =="3" :
        if not list_task:
            print("no tasks add yet: ")   
        else:
            print("your tasks:")
            i=1
            for d in list_task:
                print(1,d)
                i+=1
        ch_nm_del=int(input("enter task number you want delet"))
        if ch_nm_del>= 1 and ch_nm_del< len(list_task):
            print(f" delted tasks:{list_task.pop(ch_nm_del-1)}")
            print(f"your tasks is:{list_task}")
        else:
            print(" not correct : ")
    elif choise =="4":
        print("you exite good bye ************")
    else:
        print("your choise invalid try again*********** ")

        
   