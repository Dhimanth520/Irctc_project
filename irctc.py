import sqlite3
import random
from enum import Enum
from data_handle import create_table
from user_authentication import register,login
# from data_handle import create_table

class Irctc:
    def __init__(self,db="irst_project_trial2.db"):
        self.conn=sqlite3.connect(db)
        self.c=self.conn.cursor()
        # self.create_table()
        create_table(self.c)

if __name__=="__main__":
    obj=Irctc()
    class Options(Enum):
        Login=1
        Signup=2
    
        Exit=3
    while(True):
        print("________IRCTC SYSTEM________")
        print("________User Authentication________")
        print("""Choose Your Options: """)
        print("""1.Login\n2.Signup\n3.Exit""")
        Choice = int(input("Enter the Choice: "))
        try:
        
            select_choice=Options(Choice)
            if select_choice==Options.Login:
                login(obj.conn,obj.c)
            elif select_choice==Options.Signup:
                register(obj.conn,obj.c)  
            elif select_choice==Options.Exit:
                break    
            else:
                print("Invalid choice try again..")    
        except ValueError:
                print("Invalid input please chose the options between 1 to 3..")            
    obj.connection_close()