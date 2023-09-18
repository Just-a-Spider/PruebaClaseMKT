from os import system

# Variables
M = [] 
f = 0
c = 0

def borrarTerminal():
    system('clear')

def ingresarDatos():
    global M, f, c
    borrarTerminal()
    print('----Ingresar Datos a la Matriz----')
    f = int(input('Cantidad de Filas: '))
    c = int(input('Cantidad de Columnas: '))
    M = [[0 for i in range(c)] for _ in range(f)]
    for i in range(f):
        for j in range(c):
            M[i][j] = int(input(f'M[{i}][{j}]: '))

def mostrarDatos():
    global M, f, c
    borrarTerminal()
    print('----Mostrando Datos de la Matriz----')
    for i in range(f):
        print('\n')
        for j in range(c):
            print(f'[{M[i][j]}]', end='')
    print('\n\n')

def sumarDatos():
    global M, f, c
    borrarTerminal()
    print('----Sumar Datos de la Matriz----')
    x = 0
    for i in range(f):
        for j in range(c):
            x += M[i][j]
    print(f'\nLa suma de los datos en la matriz es: {x}\n')

def sumarFila():
    global M, f, c
    borrarTerminal()
    print('----Sumar Fila----')
    suma = 0
    print(f'Filas disponibles: {f}')
    x = int(input('Escoga una fila: '))
    while x not in range(f+1):
        x = int(input('Por favor, ingrese una fila disponible: '))
    for _ in range(c):
        suma += M[x-1][_]
    print(f'\nLa suma de los datos en la fila {x} es: {suma}\n')

def sumarColumna():
    global M, f, c
    borrarTerminal()
    print('----Sumar Columna----')
    suma = 0
    print(f'Columnas disponibles: {c}')
    x = int(input('Escoga una fila: '))
    while x not in range(c):
        x = int(input('Por favor, ingrese una columna disponible'))
    for _ in range(c):
        suma += M[_][x-1]
    print(f'\nLa suma de los datos en la columna {x} es: {suma}\n')

def traza():
    pass

def menu(op):
    while op in ['s','S']:
        borrarTerminal()
        print('----Menu de Matriz----')
        print('1) Ingreso de Datos')
        print('2) Mostrar Matriz')
        print('3) Suma de la Matriz')
        print('4) Suma de una Fila')
        print('5) Suma de una Columna')
        print('6) Traza de la Matriz')
        print('7) Suma Diagonal Secundaria')
        print('8) Triangular Inferior a Cero')
        print('9) Triangular Superior a Cero')
        op = input('Escoja una opción: ')
        match op:
            case '1':
                ingresarDatos()
            case '2':
                mostrarDatos()
            case '3':
                sumarDatos()
            case '4':
                sumarFila()
            case '5':
                sumarColumna()
            case _:
                print('Opción no válida\n')
        op = input('Desea continuar?(s/n): ')

menu('s')