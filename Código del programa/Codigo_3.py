#Este codigo es similar al código 2 solo que en este caso se introdujo un comando o varios los cuales añaden una gráfica lineal para mejor entendimiento del código (el comando o comandos que generan la imagen fueron descubiertos u obetnidos con ayuda del programa chat gpt)
#Este no sería el código final ya que al reproducir el código la imagen no se genera y para esto se le pedirá ayuda al profesor

import numpy as np
import matplotlib.pyplot as plt

# Obtener los datos del usuario
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

# Creación del arreglo de posiciones en la viga
posiciones = np.linspace(0, longitud_viga, num=100)

# Cálculo de las fuerzas internas en cada posición de la viga
fuerzas_en_posiciones = np.interp(posiciones, [0, longitud_viga], fuerzas_internas)

# Impresión de los resultados
print("Reacciones en los puntos de apoyo:")
print("Reacción en el punto de apoyo izquierdo:", reacciones[0], "N")
print("Reacción en el punto de apoyo derecho:", reacciones[1], "N")
print()
print("Fuerzas internas en la viga:")
print("Fuerza interna en el punto de inicio de la viga:", fuerzas_internas[0], "N")
print("Fuerza interna en el punto de finalización de la viga:", fuerzas_internas[1], "N")

# Gráfica de las fuerzas internas en la viga
plt.plot(posiciones, fuerzas_en_posiciones)
plt.xlabel("Posición en la viga (metros)")
plt.ylabel("Fuerza interna (Newtons)")
plt.title("Distribución de fuerzas internas en la viga")
plt.grid(True)
plt.show()