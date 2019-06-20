def input1():
    sname=input("enter your name")
    dbname=input("enter the database name")
    username=input("enter your username")
    password=input("enter your passowrd")
    return(sname,dbname,username,password)



def main():
    
    
   sname,dbname,username,password=input1()
   print("Servername=",sname,"DBname=",dbname,"usrname=",username,"password=",password)
main()
