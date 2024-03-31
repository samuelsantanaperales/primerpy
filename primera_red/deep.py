from sklearn.linear_model import LinearRegression
import numpy as np

# Datos de ejemplo
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 3, 4, 5])

# Inicializar el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X, y)

# Realizar predicciones
predicciones = modelo.predict([[10]])

# Imprimir las predicciones
print("Predicción para x = 5:", predicciones)