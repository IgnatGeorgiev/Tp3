n = int(input("Entrer un entier  > 0: "))
i = 0
u = n
while u>1:
    if( n%2 == 0):
        u = u/2
    elif( n % 2 != 0) : 
        u = (3*u)+ 1
    i+=1
    if ( i > 100 ):
        print("Boucle infini")
        break
    #print(n)
print("Un prend la valeur 1 pour n = ",i)
