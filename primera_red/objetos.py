import numpy as np

# Definir el entorno (por ejemplo, un laberinto)
# 0: espacio vacío
# 1: obstáculo
# 2: objetivo
# 3: agente
entorno = np.array([
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 0, 2],
    [0, 0, 0, 3]
])

# Definir los parámetros del aprendizaje por refuerzo
gamma = 0.8  # factor de descuento
alpha = 0.1  # tasa de aprendizaje
episodios = 1000

# Inicializar la tabla Q con ceros
q_table = np.zeros((np.prod(entorno.shape), 4))

# Convertir el entorno en un estado unidimensional
def estado_a_idx(estado):
    return np.ravel_multi_index(estado, entorno.shape)

# Convertir el índice en un estado bidimensional
def idx_a_estado(idx):
    return np.unravel_index(idx, entorno.shape)

# Ejecutar el aprendizaje por refuerzo
for _ in range(episodios):
    estado = (3, 3)  # estado inicial
    while True:
        idx_estado = estado_a_idx(estado)
        acciones_posibles = np.where(entorno[idx_a_estado(idx_estado)] != 1)[0]
        accion = np.random.choice(acciones_posibles)
        nuevo_estado = idx_a_estado(accion)[0], idx_a_estado(accion)[1]
        recompensa = 0
        if entorno[nuevo_estado] == 2:
            recompensa = 1
        q_table[idx_estado, accion] = (1 - alpha) * q_table[idx_estado, accion] + alpha * (recompensa + gamma * np.max(q_table[estado_a_idx(nuevo_estado)]))
        if entorno[nuevo_estado] == 2:
            break
        estado = nuevo_estado

# Mostrar la tabla Q aprendida
print("Tabla Q aprendida:")
print(q_table)