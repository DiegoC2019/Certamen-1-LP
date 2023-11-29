import tkinter as tk
import random
import sys
from antlr4 import *
from antlr4.InputStream import InputStream

if __name__ == '__main__':
    while True:
        print("Ingrese una instrucción: ")
        input_stream = InputStream(sys.stdin.readline())

        try:
            #(análisis léxico y sintáctico)
            break
        except:
            print("No se reconoce la instrucción")

    infeccion_adyacente_activada = False
    ANCHO, ALTO = 100, 100
    TAMANO_CELDA = 10
    ANCHO_CAPA = ANCHO // TAMANO_CELDA
    ALTO_CAPA = ALTO // TAMANO_CELDA
    NUM_CAPAS = 3
  

    # Sección para la inicialización del autómata celular (código incompleto)
    SUSCEPTIBLE = "S"
    EXPUESTO = "E"
    INFECTADO = "I"
    RECUPERADO = "R"

    capas = []
    tiempos_expuestos = []

 

    def actualizar_capas():


        def actualizar_y_redibujar():
            global capas, tiempos_expuestos
            capas, tiempos_expuestos = actualizar_capas()
            dibujar_capas()
            root.after(1000, actualizar_y_redibujar)



    root = tk.Tk()
    root.title("Autómata Celular SEIR de Capas Múltiples")
    root.geometry(str(ANCHO * NUM_CAPAS) + "x" + str(ALTO))
    lienzos = [tk.Canvas(root, width=ANCHO, height=ALTO) for _ in range(NUM_CAPAS)]
    for lienzo in lienzos:
        lienzo.pack(side="left")

    def dibujar_capas():
        for i, lienzo in enumerate(lienzos):
            lienzo.delete("celda")
            for y in range(ALTO_CAPA):
                for x in range(ANCHO_CAPA):
                    color = "green"
                    lienzo.create_rectangle(x * TAMANO_CELDA, y * TAMANO_CELDA, (x + 1) * TAMANO_CELDA,
                                            (y + 1) * TAMANO_CELDA, fill=color, outline="black", tags="celda")

    dibujar_capas()
    root.mainloop()
