n=int(input("Enter the number: ")) #Range of the fibonacci series
a=int(input("Enter the first number: ")) #First number of the fibonacci series
b=int(input("Enter the second number: ")) #Second number of the fibonacci series
c=0
print(a)
print(b)
for c in range (n):
    
    c=a+b     #Value of a and b is added to give the value to c
    a=b        #Value of a is updated
    b=c         #Value of is updated
    if c<=n:
        print(c)
    else:
        print()
    
