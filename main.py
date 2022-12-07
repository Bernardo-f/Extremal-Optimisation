import numpy as np 
import sys

def random_int_to_n(n):
    return np.random.randint(n)

def random_0_to_1():
    return np.random.random()

def ruleta(c):
    aux = np.arange(1,c+1)**-tau
    aux /= np.sum(aux)
    aux = np.cumsum(aux)
    print(aux)
    return aux

#Se obtiene el indice de un individuo de la poblacion randomicamente segun la probabilidad de cruza
def getIndexTorneo(random, arrayProb):
    for i in range(0, n):
        if random <= arrayProb[i]:
            return i

def first_solution(n,elements):
    solucion = np.random.randint(2,size=n)
    print(elements)
    while not verify_weight(solucion,elements):
        # print(solucion)
        auxElements = elements.copy()
        auxElements[:,1] = elements[:,1]*solucion
        auxElements = auxElements[auxElements[:,1].argsort()]
        solucion[auxElements[len(auxElements)-1][0]-1] = 0
        solucion[random_int_to_n(n)] = 1

    return solucion

def verify_weight(solucion,elements):
    # print(np.sum(solucion*elements[:,1]))
    if np.sum(solucion*elements[:,1]) <= c:
        return True
    else:
        return False

def calculateFitness():
    arrayPrecio = arraySolucion * elements[:,1]
    arrayPrecio = arrayPrecio[np.where(arrayPrecio!=0)]
    return np.sum(arrayPrecio)
   
    

def solve():
    i = 0
    # Calcula precio/peso y los ordena de menor a mayor ( numero mayor es mejor , numero menor es peor)
    auxElements = elementsFloat.copy()
    auxElements[:,1] = (elements[:,2]/elements[:,1])
    auxElements = auxElements[auxElements[:,1].argsort()]
    fitnessValue = 0
    while i < iteraciones or fitnessValue >= c:
        indexObtenido = getIndexTorneo(random_0_to_1(), Ruleta)
        # print("index obtenido", indexObtenido)
        # print(auxElements[:,1][indexObtenido])
        # print("sol antes", arraySolucion)
        if(arraySolucion[indexObtenido] == 0):
            arraySolucion[indexObtenido] = 1
            if(not verify_weight(arraySolucion, elements)):
                arraySolucion[indexObtenido] = 0
        else:
            arraySolucion[indexObtenido] = 0
        # print("sol despues", arraySolucion)
        # print(auxElements)
        fitnessValue = calculateFitness()
        print("actual fitness", fitnessValue)
        print("i ",i)
        i+=1
    print(arraySolucion)
    print(elements)

      
       
      

    
    # while not verify_weight(posibleSolucion):


# py .\main.py knapPI_1_50_100000.csv 10 10 1.4 

if len(sys.argv) == 5:
   archivo_entrada = sys.argv[1]
   seed = int(sys.argv[2])
   iteraciones = int(sys.argv[3])
   tau = float(sys.argv[4])
else:
   print('Formato de argumentos ingresados no es válido: <Nombre archivo de entrada> <Valor semilla> <Número de iteraciones> <Valor de Tau>.')
   exit()

np.random.seed(seed=seed)
test = np.genfromtxt(archivo_entrada, delimiter=" ", skip_header=1,max_rows=3,dtype=int,usecols=(1))
n = test[0] # Cantidad variables
c = test[1] # Mejor precio
z = test[2] # Mejor peso



elements = np.genfromtxt(archivo_entrada, delimiter=",",skip_header=5,max_rows=n,dtype=int,usecols=(0,1,2))
elementsFloat = np.genfromtxt(archivo_entrada, delimiter=",",skip_header=5,max_rows=n,dtype=float,usecols=(0,1,2))

# print("n:",n," c:",c)
Ruleta = ruleta(n)

arraySolucion = first_solution(n,elements)


solve()

# while iteraciones > 0 or  np.sum(elements[:,2] * solucion) <= z:








