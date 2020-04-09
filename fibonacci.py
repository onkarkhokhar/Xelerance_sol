ser=[]
max =int(input("Enter the term:"))
first = 0
second = 1
print(first)
print(second)
ser.append(first)
ser.append(second)
while(True):
	if(first+second < max):
		print(first+second)
		n=first+second
		ser.append(n)
		temp = first
		first = second
		second = temp+second

for i in ser:
        if i%2 != 0:
            total+=i
print (total)
