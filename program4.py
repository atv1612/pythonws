def input1():
    sname=input("enter your name")
    dbname=input("enter the database name")
    username=input("enter your username")
    password=input("enter your passowrd")
    return(sname,dbname,username,password)


def connect(s,dbn,u,p):
    return (s,dbn,u,p)
    
def main():
    
    
   sname,dbname,username,password=input1()
   s,dbn,u,p= connect(sname,dbname,username,password)
   print("Servername=",s,"DBname=",dbn,"usrname=","password=",p)
    
