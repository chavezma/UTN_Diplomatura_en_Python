#### Ejercicio 01:

Cree una función lamba que compruebe si un número es par o impar

```python
    es_par = lambda nro: nro % 2 == 0
    print(es_par(7))
```

#### Ejercicio 02:

Crear una función lambda que sea equivalente a la siguiente función:

```python
def multiplicar_por_tres(valor):
        res = 3 * valor
        return res
```

```python
    por_tres = lambda nro: nro * 3
    print(por_tres(6))
```
#### Ejercicio 03:
Crear una función lambda que sea equivalente a la siguiente función:

```python
def sumar(valor1, valor2):
        res = valor1 + valor2
        return res
```

```python
    sumar = lambda val_1, val_2: val_1 + val_2
    print(sumar(4, 7))
```

#### Ejercicio 04:
Crear una función lambda que tome como parámetro una frase y la escriba al revés. 

```python
    reverse = lambda frase: ''.join(frase[i] for i in range(len(frase) - 1, -1, -1))
    print(reverse("mi oracion es una fiesta"))
```
#### Ejercicio 05:
Cree un programa que utilizando una función, solicite la edad de la persona e imprima todos los años que la persona ha cumplido según el siguiente formato de ejemplo. 
1, 2, 3, 4, 5
Y 
5, 4, 3, 2, 1

```python
enum = lambda num: "".join(str(i) + "," for i in range(1, num + 1) if i < num) + str(num)
reversed_enum = lambda num: "".join(str(i) + "," for i in range(num, 1, -1) if i > 0) + str(1)

def pedir_edad():
    edad = int(input("Ingrese su edad: "))
    print(enum(edad))
    print(reversed_enum(edad))

pedir_edad()
```
#### Ejercicio 06:
Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes:
[3, 44, 21, 78, 5, 56, 9]

```python
lista = [3, 44, 21, 78, 5, 56, 9, 7]

def swap(la_lista, i, j):
    temp = lista[j]
    lista[j] = lista[i]
    lista[i] = temp

def ordena_lista_iterativo(ls):
    la_lista = ls
    for x in range(0, len(ls)):
        for y in range(0, len(ls)):
            if x < y and ls[x] > ls[y]:
                swap(ls, x, y)

    return la_lista

def ordena_lista_recursivo(ls):
    if len(ls) == 2:
        return sorted(ls)

    if len(ls) == 1:
        return ls

    pivot = int(len(ls) / 2)

    return merge(ordena_lista_recursivo(ls[0:pivot]), ordena_lista_recursivo(ls[pivot:]))

def merge(l1, l2):
    nueva_lista = []

    while len(l1) > 0 and len(l2) > 0:
        while l1 and l2:
            if l1[0] < l2[0]:
                nueva_lista.append(l1[0])
                del l1[0]
            else:
                nueva_lista.append(l2[0])
                del l2[0]

    if len(l1) > 0:
        while l1:
            nueva_lista.append(l1[0])
            del l1[0]
    else:
        while l2:
            nueva_lista.append(l2[0])
            del l2[0]

    return nueva_lista

# merge([3, 4], [1, 2])

print("--------------------------------------------")
print("resultado iterativo => ", ordena_lista_iterativo(lista))
print("resultado recursivo => ", ordena_lista_recursivo(lista))
```
#### Ejercicio 07:
isinstance(x, list) permite consultar si el elementos x es del tipo lista.
A partir de la siguiente función recursiva que permite recorrer los niveles de una lista:

lista = ["elemento1n1", "elemento2n1", "elemento3n1",
["elemento1n2", "elemento2n2", "elemento3n2",
["elemento1n3", "elemento2n3", "elemento3n3"]]]

```python
def recorre_lista(item):
    for x in item:
        if isinstance(x, list):
            recorrer_lista(x)
        else:
            print(x)

recorrer_lista(lista)
```
Optimice el código de forma que el programa considere:
•	Un valor de lista por defecto
•	Permita tomar un segundo parámetro que lleve un registro del nivel en el cual se encuentra (en qué grado del anidamiento)
•	Permita tomar un valor por defecto de cero para el parámetro anterior.
•	Presente la salida según el siguiente formato:

elemento1n1
elemento2n1
elemento3n1
    elemento1n2
    elemento2n2
    elemento3n2
        elemento1n3
        elemento2n3
        elemento3n3

```python
    def analiza_lista(la_lista=[], nivel=1):
        for elem in la_lista:
            if isinstance(elem, list):
                analiza_lista(elem, nivel + 1)
            else:
                tab = "".ljust(5 * nivel)
                print(f"{tab}{elem}")

    analiza_lista(lista)
```