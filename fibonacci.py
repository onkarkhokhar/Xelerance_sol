ser = []
max = int(input("Enter max value:"))
first = 0
second = 1
print(first)
print(second)
while (first + second < max):
        n = first + second
        ser.append(n)
        print(n)
        temp = first
        first = second
        second = temp + second

total = 0
for i in ser:
    if i % 2 != 0:
        total += i
print("odd number sum is:"+str(total))
