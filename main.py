import numpy as np 
import sys
import pandas as pd
import matplotlib.pyplot as plt

def random_int_to_n(n):
    return np.random.randint(n)

def random_0_to_1():
    return np.random.random()

def ruleta(c,tau):
    aux = np.arange(1,c+1)**-tau 
    aux /= np.sum(aux)
    aux = np.cumsum(aux)
    return aux

#Se obtiene el indice de un individuo de la poblacion randomicamente segun la probabilidad de cruza
def getIndexTorneo(random, arrayProb):
    for i in range(0, n):
        if random <= arrayProb[i]:
            return i

def first_solution(n,elements):
    solucion = np.random.randint(2,size=n)
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
    if np.sum(solucion*elements[:,2]) <= c:
        return True
    else:
        return False

def calculateFitness(array):
    return np.sum(array * elements[:,1])
   
def solve(tau):
    list_fitness = []
    i = 0
    # Calcula precio/peso y los ordena de menor a mayor ( numero mayor es mejor , numero menor es peor)
    Ruleta = ruleta(n,tau)
    auxElements = elements.copy()
    auxElements[:,1] = (elements[:,1]/elements[:,2])
    auxElements = auxElements[-auxElements[:,1].argsort()]

    
    fitnessValue = 0
    arraySolucion = first_solution(n,elements)
    bestSolucionArray = arraySolucion
    bestSolucionFitness = calculateFitness(arraySolucion)
    # print("best array inicial", bestSolucionArray)
    # print("best fitness inicial", bestSolucionFitness)
    while i < iteraciones and fitnessValue < z:
        indexObtenido = getIndexTorneo(random_0_to_1(), Ruleta)
        pos = auxElements[indexObtenido][0] - 1
        if(arraySolucion[pos] == 0):
            arraySolucion[pos] = 1
            if(not verify_weight(arraySolucion, elements)):
                arraySolucion[pos] = 0
        else:
            arraySolucion[pos] = 0
        fitnessValue = calculateFitness(arraySolucion)
        if(fitnessValue > bestSolucionFitness):
            bestSolucionArray = arraySolucion.copy()
            bestSolucionFitness = calculateFitness(bestSolucionArray)
            # print("i", i)
            list_fitness.append(bestSolucionFitness)
        i+=1
    # print("best array", bestSolucionArray) 
    # print("best fitness", calculateFitness(bestSolucionArray)) 
    return list_fitness
    

# py .\main.py knapPI_1_50_100000.csv 10 10 1.4 

if len(sys.argv) == 5:
   archivo_entrada = sys.argv[1]
   seed = int(sys.argv[2])
   iteraciones = int(sys.argv[3])
   tau = float(sys.argv[4])
else:
   print('Formato de argumentos ingresados no es v??lido: <Nombre archivo de entrada> <Valor semilla> <N??mero de iteraciones> <Valor de Tau>.')
   exit()

# archivo_entrada = "knapPI_1_50_100000.csv"
# seed = 10
# iteraciones = 100
# tau = 1.4

np.random.seed(seed=seed)
#test = np.genfromtxt(archivo_entrada, delimiter=" ", skip_header=1,max_rows=3,dtype=int,usecols=(1))
test = pd.read_csv(archivo_entrada,header=None,delimiter=" ",skiprows=1,nrows=3,usecols=[1]).to_numpy()
n = test[0][0] # Cantidad variables
c = test[1][0] # Mejor precio
z = test[2][0] # Mejor peso

#elements = np.genfromtxt(archivo_entrada, delimiter=",",skip_header=5,max_rows=n,dtype=int,usecols=(0,1,2))
elements = pd.read_csv(archivo_entrada,header=None,skiprows=5,nrows=n,usecols=[0,1,2]).to_numpy()

# elementsFloat = np.genfromtxt(archivo_entrada, delimiter=",",skip_header=5,max_rows=n,dtype=float,usecols=(0,1,2))



listFiness = []
tau_inicial = tau
while tau < 1.9:
    tau += 0.1
    listFiness.append(solve(tau))

print(listFiness)
plt.suptitle('Diagrama')
plt.xlabel('valor de tau')
plt.ylabel('Fitness')
plt.boxplot(listFiness)
plt.xticks(np.arange(1,len(listFiness)+1),np.arange(tau_inicial,tau-0.1,0.1,dtype=float).round(1))
plt.show()



