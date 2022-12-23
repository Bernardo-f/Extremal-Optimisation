# Extremal Optimisation
 Trabajo de programacón 3

En este algoritmo se resolverá el problema de la mochila, el cual consiste en maximizar el precio de los elementos que se guarden en la mochila. 

## Instalación

1. Asegurate de tener instalado <a href="https://www.python.org/">Python</a> >= `3.0`

2. Instalar libreria numpy 
   ```sh
   pip install numpy
   ```
3. Instalar libreria pandas 
   ```sh
   pip install pandas
   ```
4. Instalar libreria  matplotlib.pyplot 
   ```sh
   pip install  matplotlib.pyplot
   ```
 ## Ejecución
 
   1. Para iniciar el algoritmo de debe ejecutar por consola el siguiente comando
   ```sh
   python3 main.py <Nombre archivo de entrada> <Valor semilla> <Número de iteraciones> <Valor de Tau>
   ```
Los parámetros de entradas serán de tipo:
* Nombre archivo de entrada: Variable de tipo `string` con el nombre del archivo .txt que contenga las distancia de las ciudades
* Valor de la semilla: Generador de los valores aleatorios. (Para una misma semilla se obtendrá siempre los mismos valores aleatorios) Es de cualquier tipo de variable.
* Número de iteraciones : Variable de tipo `entero` del número de siglos que se representa en la cantidad de generaciones que se van a crear,
* Valor de tau : valor con el que se construira la ruleta en distribucion de potencia.

## Parámetros de salida

* Array de largo del total de posibles cosas a guardar en mochila indicando con un 1 si van en la mochila o 0 en el caso contrario.

## Desarrolladores

* Fernando Fuentealba
* Bernardo Fernández
* Alexis Pinto
