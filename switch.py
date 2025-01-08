#Write a menu driven program which has following options Write a menu driven program which has following options:  
# 1. Factorial of a number  
# 2. Prime or not  
# 3. Odd or even  
# 4. Exit 


while True:
    print("1. Factorial of a number")
    print("2. Prime or not")
    print("3. Odd or even")
    print("4. Exit")

    choice=int(input("Enter the choice 1-4 "))

    if choice==1:
        n=int(input("Enter the number u want to calculate the factorial : " ))
        fact=1
        for i in range(1,n+1):
            fact*=i
        print(fact)

    elif choice==2:
        n=int(input("Enter the number :"))
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count=count+1
        if count==2:
            print(n,"prime number")
        else:
            print("not a prime number ")

        """n=int(input("Enter the number : "))
        
        if n>1:
            is_prime=True
            i=2
            while i<=int(n**0.5):
                if n%i==0:
                    is_prime=False
                    break
                i+=1
                if is_prime:
                    print("This is the prime number")
                else:
                    print("not prime number ")"""
        
    elif choice==3:
        n=int(input("Enter the number : "))
        if n%2==0:
            print("Even ")
        else:
            print("odd")

    elif choice==4:
        print("Exiting the program ")
        break
    else:
        print("Invalid choice ")