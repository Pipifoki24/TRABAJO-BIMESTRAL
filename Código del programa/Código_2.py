#Este código queda como segundo borrador ya que al momento de ejecutarlo en github no me deja ingresar los datos como por ejemplo me dejaría en alguna otra página o aplicación

import numpy as np

# Obtener los datos del usuario(en comparacion con el código 1 ahora nosotros asignamos el valor de longitud de la viga y la carga aplicada en el centro de la viga)
longitud_viga = float(input("Ingrese la longitud de la viga del puente (en metros): "))
carga_centro = float(input("Ingrese la carga aplicada en el centro de la viga (en Newtons): "))

# Definición de la matriz de rigidez de la viga
matriz_rigidez = np.array([[2.0, -1.0], [-1.0, 2.0]])

# Definición del vector de fuerzas aplicadas
vector_fuerzas = np.array([0.0, carga_centro])

# Resolución del sistema de ecuaciones lineales para obtener las reacciones en los puntos de apoyo
reacciones = np.linalg.solve(matriz_rigidez, vector_fuerzas)

# Cálculo de las fuerzas internas en la viga
fuerzas_internas = np.dot(matriz_rigidez, reacciones)

# Impresión de los resultados
print("Reacciones en los puntos de apoyo:")
print("Reacción en el punto de apoyo izquierdo:", reacciones[0], "N")
print("Reacción en el punto de apoyo derecho:", reacciones[1], "N")
print()
print("Fuerzas internas en la viga:")
print("Fuerza interna en el punto de inicio de la viga:", fuerzas_internas[0], "N")
print("Fuerza interna en el punto de finalización de la viga:", fuerzas_internas[1], "N")
