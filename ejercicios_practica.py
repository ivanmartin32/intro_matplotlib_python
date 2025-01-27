#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np
import matplotlib.pyplot as plt


def ej1():
    # Line Plot
    # Se desea graficar los valores de X e Y en un gráfico de línea

    # Función que se desea graficar:
    # y1 = x**2

    x = list(range(-10, 11, 1))
    # Estamos aprovechando el concepto de comprension de listas
    # para generar los valores que toma "Y" por cada valor de "X"
    y = []
    for i in x:
        y.append(i**2)

    # Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "Y" en función de "X"
    # Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección

    fig = plt.figure()
    fig.suptitle('Figura N°1', fontsize=30)
    ax = fig.add_subplot()
    ax.plot(x, y, color='tab:purple', label='y1 = x**2')
    ax.grid()
    ax.legend()
    plt.show()
    print("Fin")


def ej2():
    # Line Plot
    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación es la siguiente:
    x = list(np.linspace(-4, 4, 20))
    # Estamos aprovechando el concepto de comprension de listas
    # para generar los valores que toma "Y" por cada valor de "X"
    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    # Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    fig = plt.figure()
    fig.suptitle('Figura N°2', fontsize=30)
    ax = fig.add_subplot()
    ax.plot(x, y1, color='tab:green', label='y1 = x**2')
    ax.plot(x, y2, color='tab:pink', label='y2 = x**3')
    ax.grid()
    ax.legend()
    plt.show()
    print("Fin")


def ej3():
    # Scatter Plot
    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función a implementar
    # y = tanh(x) --> tangente hiperbólica

    # Implementacion
    y = np.tanh(x)

    # Graficar la función utilizando "scatter"

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Elegir un marker a elección

    fig = plt.figure()
    fig.suptitle('Figura N°3', fontsize=30)
    ax1 = fig.add_subplot(1, 2, 1) 
    ax2 = fig.add_subplot(1, 2, 2) 
    ax1.plot(x, y, c='tab:blue', label='y = tanh')
    ax2.scatter(x, y, c='tab:red', label='y = tanh')
    ax1.grid()
    ax2.grid()
    ax1.legend()
    ax2.legend()
    plt.show()
    print("Fin")


def ej4():
    # Figura con múltiples gráficos
    # Line Plot
    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(-10, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Figura N°4', fontsize=30)
    ax1.plot(x, y1, 'tab:blue')
    ax1.set_title('y1 = x^2', fontsize=6)
    ax1.grid(ls='dashed')
    ax1.legend()
    ax2.plot(x, y2, 'tab:orange')
    ax2.set_title('y1 = x^3', fontsize=6)
    ax2.grid(ls='dashdot')
    ax2.legend()
    ax3.plot(x, y3, 'tab:green')
    ax3.set_title('y1 = x^4', fontsize=6)
    ax3.grid(ls='dashed')
    ax3.legend()
    ax4.plot(x, y4, 'tab:red')
    ax4.set_title('y4 = raiz_cuadrada', fontsize=6)
    ax4.grid(ls='dashdot')
    ax4.legend()
    plt.show()
    print("Fin")
                                

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
