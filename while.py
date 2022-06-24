n=int(input("Enter the last number: "))
q=0
while q<=n:
    if q%2==0:
        print("the number is even: ",q)
    else:
        print("The number is odd: ",q)
    q+=1