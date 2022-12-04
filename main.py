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
def getIndexTorneo(random, arrayProbCruza):
    for i in range(0, n):
        if random <= arrayProbCruza[i]:
            return i


def High_Heuristica():

    heuristica = [ (np.sum(solucion*elements[:,1]) - elements[:,1])*solucion ] - c


    ## descartar los que no estan seleccionados
    out = np.where(heuristica[0] == (-1*c)) ## indicesseleccionados
    first = int(out[0][0]) 


    ##print( np.sort(heuristica[0]))

    ## heuristica
    heuristica = np.argsort(heuristica[0])  ## ordernar de menor a mayot por indice
    cut = np.where(heuristica == first) ## buscar indice de corte
    size_cut = int(np.size(out[0])) ## rango del corte
    heuristica = np.delete(heuristica,heuristica[cut[0][0]:cut[0][0]+size_cut])
    heuristica = np.append(heuristica,out[0])

    return heuristica


def verify_weight(solucion):
    if np.sum(solucion*elements[:,1]) <= c:
        return True
    else:
        return False

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
test = np.genfromtxt(archivo_entrada, delimiter=" ", skip_header=1,max_rows=2,dtype=int,usecols=(1))
n = test[0]
c = test[1]

elements = np.genfromtxt(archivo_entrada, delimiter=",",skip_header=5,max_rows=n,dtype=int,usecols=(0,1,2))

print("n:",n," c:",c)
Ruleta = ruleta(n)

solucion = np.random.randint(2,size=n)
High_Heuristica()
print(Ruleta)


while True:
   
    if verify_weight(solucion):
        print("finalizado")
        break
    else:
        random = random_0_to_1()
        index = getIndexTorneo(random,Ruleta)
        heuristica = High_Heuristica()
        solucion[heuristica[index]] = 0

print(np.sum(solucion*elements[:,1]),c)

