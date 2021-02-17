#generating a 3X3 matrix with 9 random prime numbers
import random
def asal(sayi):    
   for i in range(2,sayi):
       if (sayi % i) == 0:
           break
   else:
       liste.append(sayi)
liste = list()
for i in range(1,101):
    asal(i) 
dizi = []  
for i in range(3):
    dizi.append([])
    for j in range(3):
        rnd = random.choice(liste)
        dizi[i].append(rnd)
        liste.remove(rnd)
for i in dizi:
    for j in i:
        print(j, end=" ")
    print("")
