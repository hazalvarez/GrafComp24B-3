from manim import *
import numpy as np

class Shapes(Scene):
    def construct(self):
        # Agregar texto que se muestre durante toda la ejecución
        nombre_programa = Text("Citli López Campos", font_size=20)
        nombre_programa.to_edge(DOWN)
        self.add(nombre_programa)

        # Círculo con color diferente y relleno
        circulo = Circle(color=RED, fill_opacity=1)  # Círculo rojo y relleno completo
        createCircle = Create(circulo)  # Animación de creación
        self.play(createCircle)  # Mostrar la animación
        self.wait(1)
        self.play(FadeOut(circulo))  # Desaparecer el círculo

        # Rectángulo con color diferente y relleno
        rect = Rectangle(color=BLUE, height=3, width=1, fill_opacity=1)  # Rectángulo azul relleno
        self.play(Create(rect))  # Mostrar rectángulo
        self.wait(1)
        self.play(FadeOut(rect))  # Desaparecer rectángulo

        # Cuadrado con color diferente y relleno
        cuadrado = Square(color=GREEN, fill_opacity=1)  # Cuadrado verde y relleno completo
        cuadrado.move_to(np.array([-4, 2, 0]))  # Mover el cuadrado a una posición designada
        cuadrado2 = Square(color=YELLOW, fill_opacity=1)  # Cuadrado amarillo relleno
        cuadrado2.to_edge(UP)  # LLeva una figura al borde
        self.play(Create(cuadrado), Create(cuadrado2))  # Crear ambos cuadrados
        self.wait(1)
        self.play(FadeOut(cuadrado), FadeOut(cuadrado2))  # Desaparecer los cuadrados

        # Línea con color diferente
        linea = Line(np.array([2, 0, 0]), np.array([-2, 1, 0]), color=PURPLE)  # Línea morada
        self.play(Create(linea))  # Mostrar la línea
        self.wait(1)
        self.play(FadeOut(linea))  # Desaparecer la línea
