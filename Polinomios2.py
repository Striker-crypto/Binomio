import numpy as np

def formula(a,b,c):
    discrim = pow(b,2)-(4*a*c)
    return  discrim
def raices(a,b,disc):
    raiz1 = (-b+np.sqrt(disc))/(2*a)
    raiz2 = (-b-np.sqrt(disc))/(2*a)
    return  raiz1,raiz2

print("Introduzca los coeficientes a,b y c")
a = float(input("a :"))
b = float(input("b :"))
c = float(input("c :"))
disc = formula(a,b,c)
if disc<0:
    print("No hay solución en los números reales")
else:
    print("Las raices son")
    print(raices(a,b,disc))