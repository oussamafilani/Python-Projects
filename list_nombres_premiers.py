n = int(input("entre un nombre "))
for i in range(2, n) :

        premier = True
        for j in range(2, i) :
            if i % j == 0 :
                premier = False
                break

        if premier:
            print(i)



