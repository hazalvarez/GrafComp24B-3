from manim import *

class Video1(Scene):
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


        # Primera parte: TransformationText1V1
        self.camera.background_color = BLUE  # Cambiar el fondo a azul
        texto1 = Tex("Hola Mundo")
        texto2 = Tex("Holaaa Mundo")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Segunda parte: TransformationText1V2
        self.camera.background_color = GREEN  # Cambiar el fondo a verde
        texto1 = Tex("holaaaaa mundooooo")
        texto1.to_edge(UP)
        texto2 = Tex("HOLAAAAAAAAAAAAAAA")
        self.play(Write(texto1))
        self.wait()
        self.play(Transform(texto1, texto2))
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Tercera parte: TransformationText2
        self.camera.background_color = YELLOW  # Cambiar el fondo a amarillo
        text1 = Tex("holaaaaaaaaaaaaaaaa")
        text2 = Tex("ADIOOOOOOOOOOOOOOOS")
        text3 = Tex("adioooooooooooooos")
        text4 = Tex("Formula:")
        self.play(Write(text1))
        self.wait()
        # Trans text1 -> text2
        self.play(ReplacementTransform(text1, text2))
        self.wait()
        # Trans text2 -> text3
        self.play(ReplacementTransform(text2, text3))
        self.wait()
        # Trans text3 -> text4
        self.play(ReplacementTransform(text3, text4))
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Cuarta parte: CopyTextV1
        self.camera.background_color = PURPLE  # Cambiar el fondo a morado
        formula = MathTex(
            "\\frac{d}{dx}",  # 0
            "(",  # 1
            "u",  # 2
            "+",  # 3
            "v",  # 4
            ")",  # 5
            "=",  # 6
            "\\frac{d}{dx}",  # 7
            "u",  # 8
            "+",  # 9
            "\\frac{d}{dx}",  # 10
            "v"  # 11
        )
        formula.scale(2)
        self.play(Write(formula[0:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9])
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10])
        )
        self.wait()
