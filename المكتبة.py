#كلاس للمستخدم
from enum import member
import time
import os
def clear_screen():
    os.system("cls" if os.name=="nt"else"clear")

class Gym:
    def __init__(self,first_name,last_name,membership,statu="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.membership=membership
        self.statu=statu

    def display_user(self):
        print(f"\nfirst name is:{self.first_name}\n")
        print(f"\n last name is: {self.last_name}\n")
        print(f"membership id is:{self.membership}\n")
        print(f"statu is {self.statu}\n")
def creat_member():
    clear_screen
    first_name=input("entre your first name:\n")
    last_name=input("entre your last name:\n")
    membership=input("enter your membership:\n")
    statu=input("entre your statu , or click entre:")
    if not statu:
        statu="inactive"
    return Gym(first_name,last_name,membership,statu)
#function serch
def serch_member(members):
    clear_screen
    print("\n serch by\n")
    print("1. membership id")
    print("2.first name")
    print("membership  statu")
    
    serch_choise=input("entre your choise:")

    found_member=[]
    if serch_choise=="1":
        serch_id=input("entre membership id to serch:")
        for x in members:
            if x.membership==serch_id:
                found_member.append(x)
                break
    elif serch_choise=="2":
        serch_name=input("entre first name to serch:")
        for x in members:
            if x.first_name==serch_name:
                found_member.append(x)
    elif serch_choise=="3":
        statu_serch=input("entre statu to serch active(active/anactive)")
        for x in members:
            if x.statu==statu_serch:
                found_member.append(x)
    if found_member:
        clear_screen
        print("found members:")
        for x in found_member:
            x.display_user()
    else:
        print("member not found")






members=[]
while True:
    print("welcom to gym membership mangment\n")
    print("choos an action:\n")
    print("1.add new member")
    print("2.displayall membership\n")
    print("3.serch for amember\n")
    print("4.exite")
    choise=input("entre your choise")
    clear_screen()
    if choise =="1":
        members.append(creat_member())
        print("member add succssful")
        time.sleep(2)
    elif choise =="2":
        clear_screen()
        
        if members:
             print("display all membership")

             for i in members:
                i.display_user()
        else:
            print("membership didnt find it")
    elif choise =="3":
        if members:

           serch_member(members)
        else:
            print("no member to serch")
       
    elif choise=="4":
        print("exiting....")
    else:
        print("pleas try again ")    
       


        




        






