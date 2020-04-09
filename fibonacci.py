ser=[]
def F(a):
    
    f=0                                        
    s=1   
    
    if a<=0:
       print("The requested series is",f)
    else:
        print(f,s,end=" ")
        for x in range(2,a):
           next=f+s                           
           ser.append(next)
           f=s
           s=next
num=int(input("Enter the term:"))
F(num)
total=0
for i in ser:
    if i<=num:
        print(i)
        if i%2 != 0:
            total+=i
print (total+1)
