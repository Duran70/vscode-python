# program to check if given number is perfect
n=int(input("Enter a number :"))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(n==s):
    print("given is a perfect number")
else:
    print("not a perfect number")