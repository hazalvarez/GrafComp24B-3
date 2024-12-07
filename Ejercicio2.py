from manim import *
import numpy as np

class AllShapes(Scene):
    def construct(self):
        # Agregar texto que se muestre durante toda la ejecución
        nombre_programa = Text("Citli López Campos", font_size=30)
        nombre_programa.to_edge(UP)
        self.add(nombre_programa)

        # Definir los colores para las figuras
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, PINK, TEAL, GOLD, MAROON]
        color_index = 0

        # Definir las figuras con colores y rellenos cuando corresponda
        self.anim(Arc(radius=0.5, color=colors[color_index % len(colors)]))
        color_index += 1
        self.anim(ArcBetweenPoints(np.array([2, 0, 0]), np.array([-2, 0, 0]), color=colors[color_index % len(colors)]))
        color_index += 1
        self.anim(CurvedArrow(np.array([2, 0, 0]), np.array([-2, 0, 0]), color=colors[color_index % len(colors)]))
        color_index += 1
        self.anim(CurvedDoubleArrow(np.array([2, 0, 0]), np.array([-2, 0, 0]), color=colors[color_index % len(colors)]))
        color_index += 1
        self.anim(Circle(color=colors[color_index % len(colors)], fill_opacity=1))
        color_index += 1
        self.anim(Dot(color=colors[color_index % len(colors)]))
        color_index += 1
        self.anim(Dot(color=colors[color_index % len(colors)], radius=0.05))  # Reemplazar SmallDot con un Dot más pequeño
        color_index += 1
        self.anim(Ellipse(color=colors[color_index % len(colors)], fill_opacity=1))
        color_index += 1
        self.anim(AnnularSector(color=colors[color_index % len(colors)], fill_opacity=1))
        color_index += 1
        self.anim(Sector(color=colors[color_index % len(colors)], fill_opacity=1))
        color_index += 1
        self.anim(Annulus(color=colors[color_index % len(colors)], fill_opacity=1))
        color_index += 1
        self.anim(Line(np.array([2, 0, 0]), np.array([-2, 0, 0]), color=colors[color_index % len(colors)]))
        color_index += 1
        self.anim(DashedLine(np.array([2, 0, 0]), np.array([-2, 0, 0]), color=colors[color_index % len(colors)]))
        color_index += 1

        # Tangent line requires a mobject
        c = Circle(color=colors[color_index % len(colors)], fill_opacity=1)
        self.play(Create(c))
        color_index += 1
        self.anim(TangentLine(c, 0.2, color=colors[color_index % len(colors)]))
        self.play(FadeOut(c))
        color_index += 1

        self.anim(Elbow(color=colors[color_index % len(colors)]))
        color_index += 1
        self.anim(Arrow(np.array([2, 0, 0]), np.array([-2, 0, 0]), color=colors[color_index % len(colors)]))  # Reemplazar ArrowTip
        color_index += 1
        self.anim(Vector(np.array([1, 0, 0]), color=colors[color_index % len(colors)]))
        color_index += 1
        self.anim(DoubleArrow(np.array([2, 0, 0]), np.array([-2, 0, 0]), color=colors[color_index % len(colors)]))
        color_index += 1
        self.anim(Polygon(np.array([2, 0, 0]), np.array([-2, 0, 0]), np.array([1, 1, 0]), np.array([-2, -3, 0]), color=colors[color_index % len(colors)]))
        color_index += 1
        self.anim(RegularPolygon(n=5, color=colors[color_index % len(colors)], fill_opacity=1))
        color_index += 1
        self.anim(Triangle(color=colors[color_index % len(colors)], fill_opacity=1))
        color_index += 1
        # Eliminado ArrowTip
        color_index += 1
        self.anim(Rectangle(color=colors[color_index % len(colors)], fill_opacity=1))
        color_index += 1
        self.anim(Square(color=colors[color_index % len(colors)], fill_opacity=1))
        color_index += 1
        self.anim(RoundedRectangle(color=colors[color_index % len(colors)], fill_opacity=1))

    def anim(self, mob):
        self.play(Create(mob))  # Crear la figura
        self.wait(1)  # Esperar 1 segundo
        self.play(FadeOut(mob))  # Desaparecer la figura
