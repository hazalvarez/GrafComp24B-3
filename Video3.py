from manim import *

class Video3(Scene):
    def construct(self):

        # Fondo de la portada
        background = Rectangle(width=config.frame_width, height=config.frame_height, fill_color=WHITE, fill_opacity=1)
        portada_text = VGroup(
            Text("Centro Universitario UAEM Zumpango", font_size=40),
            Text("Graficación Computacional", font_size=35),
            Text("Citli López Campos", font_size=30),
            Text("Ingeniería en Computación", font_size=25),
            Text("02 de diciembre de 2024", font_size=20)
        ).arrange(DOWN, buff=0.5).set_color(BLACK)
        
        self.add(background)
        self.play(FadeIn(portada_text))
        self.wait(3)
        self.play(FadeOut(portada_text))
        self.remove(background)


        # Primera animación: PlotGraph
        self.camera.background_color = PINK  # Cambiar el fondo a azul
        axes1 = Axes(
            x_range=[4, 7, 0.5],
            y_range=[20, 50, 5],
            axis_config={"color": BLUE},
        ).add_coordinates()

        x_label1 = axes1.get_x_axis_label("x", direction=DOWN)
        y_label1 = axes1.get_y_axis_label("y", direction=RIGHT)

        graph1 = axes1.plot(lambda x: x**2, x_range=[5, 7], color=GREEN, use_smoothing=False)
        dot1 = Dot(axes1.coords_to_point(4, 20), color=RED)

        self.play(Create(axes1), Write(x_label1), Write(y_label1))
        self.play(Create(graph1))
        self.play(FadeIn(dot1))
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Segunda animación: PlotSinCos
        self.camera.background_color = GREEN  # Cambiar el fondo a verde
        axes2 = Axes(
            x_range=[-3 * PI / 2, 3 * PI / 2, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            tips=False,
        ).add_coordinates()

        sin_graph = axes2.plot(lambda x: np.sin(x), color=PINK, use_smoothing=False)
        cos_graph = axes2.plot(lambda x: np.cos(x), color=BLUE, use_smoothing=False)

        sin_label = axes2.get_graph_label(sin_graph, label="\\sin(x)")
        cos_label = axes2.get_graph_label(cos_graph, label="\\cos(x)")

        self.play(Create(axes2))
        self.play(Create(sin_graph), Write(sin_label))
        self.play(Create(cos_graph), Write(cos_label))
        self.wait()
