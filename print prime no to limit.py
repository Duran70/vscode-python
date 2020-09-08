x=10
y=100
for i in range(x,y):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
