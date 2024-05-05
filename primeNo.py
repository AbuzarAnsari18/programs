#To print a prime no code.
n = int(input("Enter a number: "))

if n>1:
    for i in range (2,n):
        if n%2==0:
            print(n,"is not a prime no")
    
    else:
        print(n,"is a prime no")
else:
    print(n,"is a prime no")


        
        
        
