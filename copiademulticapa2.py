import tkinter as tk
import random

# Parámetros del modelo
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
NUM_LAYERS = 3  # Dos capas

# Valores de estado
SUSCEPTIBLE = "S"
EXPUESTO = "E"
INFECTADO = "I"
RECUPERADO = "R"

# Inicialización del autómata celular
grids = []
exposed_times = []

for _ in range(NUM_LAYERS):
    grid = [[SUSCEPTIBLE for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    exposed_time = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    # Agregar exactamente 5 infectados en cada capa
    infectados_added = 0
    while infectados_added < 5:
        x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
        if grid[y][x] == SUSCEPTIBLE:
            grid[y][x] = INFECTADO
            infectados_added += 1
    grids.append(grid)
    exposed_times.append(exposed_time)

# Crear ventanas separadas de Tkinter para cada capa
root = tk.Tk()
root.title("Multilayer SEIR Cellular Automaton")

root.geometry(str(WIDTH * NUM_LAYERS) + "x" + str(HEIGHT))

canvas_list = []
for i in range(NUM_LAYERS):
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack(side="left")
    canvas_list.append(canvas)

def draw_grids():
    for i, canvas in enumerate(canvas_list):
        canvas.delete("cell")
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                cell_value = grids[i][y][x]
                color = "green" if cell_value == SUSCEPTIBLE else "yellow" if cell_value == EXPUESTO else "red" if cell_value == INFECTADO else "blue"
                canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill=color, outline="black", tags="cell")

def update_grids():
    new_grids = []
    new_exposed_times = []  # Lista para los nuevos tiempos expuestos
    for i in range(NUM_LAYERS):
        new_grid = [[cell for cell in row] for row in grids[i]]
        exposed_time = [[time for time in row] for row in exposed_times[i]]
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if grids[i][y][x] == SUSCEPTIBLE:
                    # Regla 1: S a E si tiene 2 vecinos I en la misma capa o 1 vecino I en capas adyacentes (arriba o abajo)
                    neighbors_i_same_layer = sum(1 for j in range(-1, 2) for k in range(-1, 2)
                                                if (j != 0 or k != 0)  # Excluye la celda actual
                                                and 0 <= x + j < GRID_WIDTH and 0 <= y + k < GRID_HEIGHT
                                                and grids[i][y + k][x + j] == INFECTADO)

                    neighbors_i_adjacent_layers = 0
                    if i > 0 and 0 <= y - 1 < GRID_HEIGHT:  # Comprobar capa superior si no es la capa superior
                        neighbors_i_adjacent_layers += 1 if grids[i - 1][y - 1][x] == INFECTADO else 0
                    if 0 <= y + 1 < GRID_HEIGHT and i < NUM_LAYERS - 1:  # Comprobar capa inferior si no es la capa inferior
                        neighbors_i_adjacent_layers += 1 if grids[i + 1][y + 1][x] == INFECTADO else 0

                    if neighbors_i_same_layer >= 2 or neighbors_i_adjacent_layers >= 1:
                        new_grid[y][x] = EXPUESTO
                        exposed_time[y][x] = 0  # Reinicia el tiempo expuesto


                        
                elif grids[i][y][x] == EXPUESTO:
                    # Regla 2: E a I después de 1 actualización
                    exposed_time[y][x] += 1
                    if exposed_time[y][x] >= 1:
                        new_grid[y][x] = INFECTADO
                elif grids[i][y][x] == INFECTADO:
                    # Regla 3: I a R después de 2 actualizaciones
                    exposed_time[y][x] += 1
                    if exposed_time[y][x] >= 5:  # Modificado para 5 actualizaciones
                        new_grid[y][x] = RECUPERADO
                elif grids[i][y][x] == RECUPERADO:
                    # Regla 4: R a S después de 3 actualizaciones
                    exposed_time[y][x] += 1
                    if exposed_time[y][x] >= 10:  # Modificado para 10 actualizaciones
                        new_grid[y][x] = SUSCEPTIBLE
        new_grids.append(new_grid)
        new_exposed_times.append(exposed_time)
    return new_grids, new_exposed_times

def update_and_redraw():
    global grids, exposed_times
    grids, exposed_times = update_grids()
    draw_grids()
    root.after(1000, update_and_redraw)

# Dibuja el autómata celular inicial
draw_grids()

# Inicia la simulación
root.after(1000, update_and_redraw)

root.mainloop()
