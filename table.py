n=int(input("Enter the number:"))
for i in range(1,n+1):
    print(i,end=" ")
for k in range(1,11):
    print()
    for j in range(1,n+1):
        print(j*k,end=" ")