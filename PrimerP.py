from manim import *

class FirstScene(Scene):

    def construct(self):
        sq = Square()
        circ = Circle().set_fill(opacity=1)
        self.play(Transform(sq, circ))
        self.wait()  # Asegúrate de que esta línea esté correctamente indentada
#Revisado
