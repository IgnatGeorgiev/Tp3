type = input("A,B,C,D,E,F,G?")
n = int(input("Lignes?"))
if(type == 'A') :
    i = 1
    while i <= n:

        #
        #*
        #**
        #***
        #****
        k=0
        while k < i:
            print("*", end="")
            k+=1
        print()
        i+=1
elif(type == 'B') :
    i = 1
    while i <= n:
        k=0
        j = 0
        while j < n-i :
            print(" ", end="")
            j+=1
        while k < i:
            print("*", end="")
            k+=1
        print()
        i+=1
elif(type == 'C') :
    i = n
    while i >= 1:
        k=i
        while k > 0:
            print("*", end="")
            k-=1
        print()
        i-=1
elif(type == 'D') :
    i = n
    while i >= 1:
        k=i
        j = n-i
        while j >0 :
            print(" ", end="")
            j-=1
        while k > 0:
            print("*", end="")
            k-=1
        print()
        i-=1
elif(type == 'E') :  
    i = 0
    while i<n :
        j = 0
        while j<n-i-1:
            print(' ', end='')
            j+=1
        k = 0
        while k < (2*i)+1:
            print('*', end='')
            k+=1
        print()
        i+=1
#elif(type == 'F') :
#elif(type == 'G') :
