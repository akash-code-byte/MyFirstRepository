number = 23
x = 1
while(x**2 < 23):
    x += 1
for y in range(2,x+1):
    if(number%y==0):
        print("is not a prime number")
        exit()
    else:
        print("is a prime number")
        exit()

number = int(input())
x = 2