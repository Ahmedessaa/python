def mario_pyramid(n) :
    for i in range (1,n+1):
        print((n-i)*" "+i*'*')
        
n=int(input("enter height of the pyramid: "))
