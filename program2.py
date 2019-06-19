def insert():
     n1=int(input("enter no1"))
     n2=int(input("enter no 2"))
     return n1,n2

def compute(a,b):
    sum1=a+b;
    return sum1

def main():
    a,b=insert()
    sum1=compute(a,b)
    print("sum of two numbers =",sum1)

main()
     

     
