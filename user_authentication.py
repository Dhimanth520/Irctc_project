import random

def register(conn,cursor):
        try:
            user_name=input("Enter the username: ")
            # db_user_name=cursor.execute("SELECT username FROM users WHERE username=?",(user_name,)).fetchone()
            
            # if db_user_name:
                # print("User already Exist...")
            # else:    
            while True:
                    user_pass=input("Enter the password: ")
                    check_db_pass=cursor.execute("SELECT password FROM users WHERE password=?",(user_pass,)).fetchall()
                    if check_db_pass:
                        print("User already Exists with tha Password Try a new Password")
                    else:    
                        confirm_pass=input("Enter the confirm password: ")
                        if confirm_pass!=user_pass:
                            print("-----Password missmatch-----")
                            
                        else:
                            cursor.execute("INSERT INTO users (username,password) VALUES (?,?) ",(user_name,user_pass))
                                # print("Registration Successfull.....")
                            user_id= cursor.execute("SELECT last_insert_rowid()").fetchone()[0]
                            
                            questions=[
                                    "What is your favorite color?",
                                    "What is your mother's maiden name?",
                                    "What is your first pet's name?",
                                    "What is your favorite movie?"
                                ]
                            print("------Answer the Authentication Question------")    
                            for question in questions:
                                answer=input(f"{question}: ")
                                cursor.execute("INSERT INTO questions (user_id,question,answer) VALUES (?,?,?)",(user_id,question,answer))
                                conn.commit()
                            print("-----Registration Successfull-----")
                            break
        except Exception as e:
            print(f"Error occured at {e}")            # break
                    
                
def login(conn,cursor):
    try:
        ask_name=input("Enter your username: ")
        name_present=cursor.execute("SELECT username FROM users WHERE username=?",(ask_name,)).fetchone()
        if name_present:
            # print("User already exists")
            ask_pass=input("Enter your Password: ")
            temp1=cursor.execute("SELECT id, password FROM users WHERE username=? ",(ask_name,))
            user=temp1.fetchone()
            if user:
                user_id,correct_password=user
                if ask_pass==correct_password:
                    print("-----Login successfull-----")
                else:
                    print("Unseccessfull Password Misss Match")
                    print(" ")
                
                    while True:
                        change_pass=input("Do u want to change the password yes or No: ")

                        if change_pass=="Yes".lower():
                            temp2=cursor.execute("SELECT question,answer FROM questions where user_id=?",(user_id,))
                            ask_questions=temp2.fetchall()

                            if ask_questions:
                                question,correct_answer=random.choice(ask_questions)
                                print("-----Answer the question which u have answered during registration-----")
                                answer=input(f"{question}: ")

                                if answer==correct_answer:
                                    print("-----You have answered the questuion correctly-----")
                                    print("-------Update the Password-------")
                                    while True:
                                        new_password=input("Enter the new Password: ")
                                        check_new_pass=cursor.execute("SELECT password FROM users WHERE password=?",(new_password,)).fetchall()
                                        if check_new_pass:
                                            print("User with this password already exist")
                                        else:   
                                            new_confirm_password=input("Enter the new Confirm Password: ")

                                            if new_confirm_password!=new_password:
                                                print("     OOps Password Missmatch     ")
                                            else:
                                                cursor.execute("UPDATE users SET password=? WHERE id=?",(new_confirm_password,user_id))
                                                conn.commit() 
                                                print(" ")   
                                                print("     Password changed successfully     ") 
                                                print(" ")
                                                break
                                    break
                                else:
                                    print("Your ans was incorrect...")
                            else:
                                print("No questions found..")
                        elif change_pass=="No".lower():
                            break
                        else:
                            print("Enter a valid input..")        
            else:
                print("User not found")
        else:
            print("User not Found Kindely Register ")
            register(conn,cursor)
    except Exception as e:
        print(f"Error occured at {e} ")        
def connection_close(self):
    cursor.close()