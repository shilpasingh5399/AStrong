#WAP to accept a number and check whether it is armstrong number or not

n=int(input("enter a number:"))
copy1,copy2=n,n
c=0
s=0
while(copy1>0):
    copy1=copy1//10
    c=c+1

while(copy2!=0):
    d=copy2%10
    s=s+pow(d,c)
    copy2=copy2//10

if s==n:
    print("Armstrong number")
else:
    print("Not Armstrong number")
    

    












    



    
