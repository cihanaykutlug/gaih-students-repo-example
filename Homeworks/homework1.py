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
for i in range(3):
   print (str(random.choice(liste)) + " " +str(random.choice(liste))+" "+str(random.choice(liste)))