import numpy as np

# Definición de los parámetros del puente y la carga
longitud_viga = 10.0  # Longitud de la viga en metros
carga_centro = 10000.0  # Carga aplicada en el centro de la viga en Newtons

# Definición de la matriz de rigidez de la viga
matriz_rigidez = np.array([[2.0, -1.0], [-1.0, 2.0]])

# Definición del vector de fuerzas aplicadas
vector_fuerzas = np.array([0.0, carga_centro])

# Resolución del sistema de ecuaciones lineales para obtener las reacciones en los puntos de apoyo
reacciones = np.linalg.solve(matriz_rigidez, vector_fuerzas) #np.linalg.solve lo que hace es que calcula su inversa.

# Cálculo de las fuerzas internas en la viga
fuerzas_internas = np.dot(matriz_rigidez, reacciones) #np.dot lo que hace es que los arrays que se van a multiplicar.

# Impresión de los resultados
print("Reacciones en los puntos de apoyo:")
print("Reacción en el punto de apoyo izquierdo:", reacciones[0], "N")
print("Reacción en el punto de apoyo derecho:", reacciones[1], "N")
print()
print("Fuerzas internas en la viga:")
print("Fuerza interna en el punto de inicio de la viga:", fuerzas_internas[0], "N")
print("Fuerza interna en el punto de finalización de la viga:", fuerzas_internas[1], "N")
