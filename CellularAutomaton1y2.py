import tkinter as tk  # Biblioteca estándar de Python para crear la interfaz gráfica
import random  # Proporciona funciones para trabajar con números aleatorios
import sys  # Funciones y variables para trabajar con el intérprete de Python
from antlr4 import *  # Reconocedor de lenguajes
from antlr4.InputStream import InputStream  # Biblioteca para pedir el input de la instrucción
from CellularAutomatonLexer import CellularAutomatonLexer
from CellularAutomatonParser import CellularAutomatonParser
from myVisitor import MyVisitor  # Importar funciones de MyVisitor

if __name__ == '__main__':
    while True:  # Inicio del bucle hasta que el usuario dé una instrucción correcta
        print("Ingrese una instrucción: ")

        input_stream = InputStream(sys.stdin.readline())  # Leer instrucciones desde el cmd

        try:  # Try para manejar algún tipo de error en la entrada

            lexer = CellularAutomatonLexer(input_stream)  # Crea un objeto lexer (CellularAutomatonLexer).
            token_stream = CommonTokenStream(lexer)  # Crea un token stream utilizando el lexer.

            parser = CellularAutomatonParser(token_stream)  # Crea un parser (CellularAutomatonParser) utilizando el token stream
            tree = parser.prog()  # Construye un árbol sintáctico
            visitor = MyVisitor()  # Crea un objeto MyVisitor para recorrer el árbol sintáctico

            result = visitor.visit(tree)  # Visita el árbol sintáctico utilizando el visitor y obtiene el resultado
            break  # Término de la entrada de instrucciones
        except: print("No se reconoce la instrucción")  # Mostrar en pantalla si la sintaxis no es la correcta para crear la instrucción

    infeccion_adyacente_activada = result[3]  # Asignación de booleano para permitir que las células se infecten entre capas
    # result[3] contiene el booleano ingresado por el usuario

    # Parámetros del modelo
    ANCHO, ALTO = result[2], result[2]  # Se asignan los parámetros de altura y anchura de cada capa
    TAMANO_CELDA = 10  # Tamaño de cada célula
    ANCHO_CAPA = ANCHO // TAMANO_CELDA  # Calcular el número de células en la capa en las direcciones horizontal y vertical
    ALTO_CAPA = ALTO // TAMANO_CELDA
    NUM_CAPAS = result[1]  # Asignación del número de capas

    # Los valores de cada estado de las células
    SUSCEPTIBLE = "S"
    EXPUESTO = "E"
    INFECTADO = "I"
    RECUPERADO = "R"

    # Inicialización del autómata celular
    capas = []  # Lista con las capas
    tiempos_expuestos = []  # Tiempos de cada capa

    for _ in range(NUM_CAPAS):  # Inicializar cada capa y su correspondiente matriz de tiempos expuestos
        capa = [[SUSCEPTIBLE for _ in range(ANCHO_CAPA)] for _ in range(ALTO_CAPA)]  # Inicializa una capa con todas las células en estado "SUSCEPTIBLE"
        tiempo_expuesto = [[0 for _ in range(ANCHO_CAPA)] for _ in range(ALTO_CAPA)]  # Inicializa una matriz de tiempos expuestos, inicialmente todos en cero

        # Agregar cantidad de infectados en cada capa
        infectados_agregados = 0  # Contador de infectados agregados
        while infectados_agregados < result[0]:  # Compara el contador con la cantidad de infectados solicitados por la instrucción
            x, y = random.randint(0, ANCHO_CAPA - 1), random.randint(0, ALTO_CAPA - 1)  # Generar coordenadas aleatorias (x, y) dentro de los límites de la capa
            if capa[y][x] == SUSCEPTIBLE:  # Verifica si la célula en las coordenadas generadas es susceptible
                capa[y][x] = INFECTADO  # Se cambia su estado a "INFECTADO"
                infectados_agregados += 1  # Se incrementa el contador de infecciones agregadas
        capas.append(capa)  # Se agregan las capas
        tiempos_expuestos.append(tiempo_expuesto)  # Se agregan los tiempos correspondientes

    # Crear ventanas separadas de Tkinter para cada capa
    root = tk.Tk()  # Crea una instancia de la clase Tk que representa la ventana principal de la interfaz gráfica
    root.title("Autómata Celular SEIR de Capas Múltiples")  # Establece el título de la ventana

    root.geometry(str(ANCHO * NUM_CAPAS) + "x" + str(ALTO))  # Define las dimensiones de la ventana en píxeles

    lienzos = []  # Lista que contendrá los lienzos (canvas) para cada capa del autómata celular.
    for i in range(NUM_CAPAS):  # Se utiliza un bucle para crear un lienzo para cada capa
        lienzo = tk.Canvas(root, width=ANCHO, height=ALTO)  # Crea un lienzo en la ventana principal "root"
        lienzo.pack(side="left")  # Indica que el widget Canvas (lienzo)
        lienzos.append(lienzo)  # Se agrega a la lista de lienzos

    def dibujar_capas():  # Función que se encarga de dibujar las células de cada capa en sus estados actuales en los lienzos
        for i, lienzo in enumerate(lienzos):  # Itera sobre cada lienzo en la lista de lienzos y su índice
            lienzo.delete("celda")  # Borra la representación anterior de las células en el lienzo. Se utiliza el tag "celda" para identificar los objetos a borrar
            for y in range(ALTO_CAPA):  # Itera sobre las filas de la capa actual
                for x in range(ANCHO_CAPA):  # Itera sobre las columnas de la capa actual
                    valor_celda = capas[i][y][x]  # Obtiene el valor (estado) de la célula en la posición actual
                    # Determina el color según el estado de la célula
                    color = "green" if valor_celda == SUSCEPTIBLE else "yellow" if valor_celda == EXPUESTO else "red" if valor_celda == INFECTADO else "blue"
                    # Crea una célula en el lienzo con las coordenadas y dimensiones correspondientes
                    lienzo.create_rectangle(x * TAMANO_CELDA, y * TAMANO_CELDA, (x + 1) * TAMANO_CELDA, (y + 1) * TAMANO_CELDA, fill=color, outline="black", tags="celda")

    def actualizar_capas():
        nuevas_capas = []  # Lista para las nuevas capas
        nuevos_tiempos_expuestos = []  # Lista para los nuevos tiempos expuestos
        for i in range(NUM_CAPAS):  # Bucle sobre cada capa del autómata celular
            nueva_capa = [[celda for celda in fila] for fila in capas[i]]  # Utilizando comprensión de listas, para no afectar directamente a los datos originales durante el proceso de actualización
            tiempo_expuesto = [[tiempo for tiempo in fila] for fila in tiempos_expuestos[i]]
            for y in range(ALTO_CAPA):  # Bucle anidado para iterar sobre cada célula de la capa actual
                for x in range(ANCHO_CAPA):
                    if capas[i][y][x] == SUSCEPTIBLE:  # Se verifica si la célula actual en la capa es "SUSCEPTIBLE"
                                                
                        vecinos_i_misma_capa = sum(1 for j in [-1, 0, 1] for k in [-1, 0, 1]# Bucles anidados para abarcar las posiciones relativas alrededor de la célula actual
                                                    if (j == 0 or k == 0) #verifica que la posición sea arriba, abajo, izquierda o derecha de la célula actual
                                                    and 0 <= x + j < ANCHO_CAPA and 0 <= y + k < ALTO_CAPA  # Evita el acceso a coordenadas fuera del rango
                                                    and capas[i][y + k][x + j] == INFECTADO)  # Se verifica si la célula en la posición del vecino está en estado "INFECTADO"

                        vecinos_i_capas_adyacentes = 0  # Contador para los vecinos infectados en capas adyacentes
                        if infeccion_adyacente_activada:  # Se verifica si está o no activada la propagación adyacente
                            if i > 0 and 0 <= y - 1 < ALTO_CAPA:  # Se verifica si la capa actual no es la primera y si la coordenada y - 1 está dentro de los límites de la capa
                                vecinos_i_capas_adyacentes += 1 if capas[i - 1][y][x] == INFECTADO else 0  # Verificar si hay un infectado en la capa superior
                            if 0 <= y + 1 < ALTO_CAPA and i < NUM_CAPAS - 1:  # Se verifica si la capa actual no es la última y si la coordenada y + 1 está dentro de los límites de la capa
                                vecinos_i_capas_adyacentes += 1 if capas[i + 1][y][x] == INFECTADO else 0  # Verificar si hay un infectado en la capa inferior

                        if vecinos_i_misma_capa >= 1 or vecinos_i_capas_adyacentes >= 1:  # Se verifica si hay al menos un vecino infectado en la misma capa o en capas adyacentes
                            nueva_capa[y][x] = EXPUESTO  # La célula actual se marca como expuesta
                            tiempo_expuesto[y][x] = 0  # Reinicio de contador de tiempo "EXPUESTO"

                    elif capas[i][y][x] == EXPUESTO:  # Se verifica si la célula actual en la capa es "EXPUESTO"
                   
                        tiempo_expuesto[y][x] += 1  # Se suma 1 al tiempo de la célula
                        if tiempo_expuesto[y][x] >= 3:  # Verifica que haya pasado al menos un tiempo para pasar a la siguiente fase
                            nueva_capa[y][x] = INFECTADO  # Transforma la célula en infectado
                    elif capas[i][y][x] == INFECTADO:  # Se verifica si la célula actual en la capa es "INFECTADO"

                        tiempo_expuesto[y][x] += 1  # Se suma 1 al tiempo de la célula
                        if tiempo_expuesto[y][x] >= 5:  # Verifica que haya pasado 5 tiempos para pasar a la siguiente fase
                            nueva_capa[y][x] = RECUPERADO  # Transforma la célula en "RECUPERADO"
                    elif capas[i][y][x] == RECUPERADO:  # Se verifica si la célula actual en la capa es "RECUPERADO"
                    
                        tiempo_expuesto[y][x] += 1  # Se suma 1 al tiempo de la célula
                        if tiempo_expuesto[y][x] >= 10:  # Verifica que haya pasado 10 tiempos para pasar a la siguiente fase
                            nueva_capa[y][x] = SUSCEPTIBLE  # Transforma la célula en "SUSCEPTIBLE"
            nuevas_capas.append(nueva_capa)  # Agregar la modificación de las capas en la lista
            nuevos_tiempos_expuestos.append(tiempo_expuesto)  # Agregar la modificación de los tiempos en la lista
        return nuevas_capas, nuevos_tiempos_expuestos  # Retornar las nuevas capas y nuevos tiempos

    def actualizar_y_redibujar():
        global capas, tiempos_expuestos  # Variables globales capas y tiempos_expuestos en lugar de crear nuevas variables locales con los mismos nombres
        capas, tiempos_expuestos = actualizar_capas()  # Llamar a la función actualizar_capas(), que actualiza las capas del autómata celular y los tiempos expuestos
        dibujar_capas()  # Llamar a la función dibujar_capas(), que se encarga de actualizar la representación gráfica del autómata celular en la interfaz gráfica de usuario
        root.after(1000, actualizar_y_redibujar)  # Programa la próxima llamada a la función actualizar_y_redibujar después de 1000 milisegundos (1 segundo)
        # Se establece un bucle en el que la función se llama repetidamente cada segundo, lo que simula el paso del tiempo en la simulación

    # Dibuja el autómata celular inicial
    dibujar_capas()

    # Inicia la simulación
    root.after(1000, actualizar_y_redibujar) #Inicia el bucle de simulación que se ejecutará continuamente, actualizando y redibujando el autómata celular en intervalos de 1 segundo.

    root.mainloop() # Inicia el bucle principal de Tkinter que manejará la interfaz gráfica y responderá a eventos hasta que se cierre la ventana.