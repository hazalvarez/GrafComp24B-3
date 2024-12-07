from manim import *

class Video2(Scene):
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

        # Animación 1: MoveBraces
        self.camera.background_color = BLUE  # Cambiar el fondo a azul
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
        )
        self.wait()
        self.play(
            ReplacementTransform(brace1, brace2),
            ReplacementTransform(t1, t2)
        )
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Animación 2: MoveBracesCopy
        self.camera.background_color = GREEN  # Cambiar el fondo a verde
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
        )
        self.wait()
        self.play(
            ReplacementTransform(brace1.copy(), brace2),
            ReplacementTransform(t1.copy(), t2),
        )
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Animación 3: MoveFrameBox
        self.camera.background_color = YELLOW  # Cambiar el fondo a amarillo
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Animación 4: MoveFrameBoxCopy
        self.camera.background_color = RED  # Cambiar el fondo a rojo
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(
            ReplacementTransform(framebox1.copy(), framebox2, path_arc=-np.pi)
        )
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Animación 5: MoveFrameBoxCopy2
        self.camera.background_color = PURPLE  # Cambiar el fondo a morado
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        t1 = MathTex("g'f")
        t2 = MathTex("f'g")
        t1.next_to(framebox1, UP, buff=0.1)
        t2.next_to(framebox2, UP, buff=0.1)
        self.play(Create(framebox1), FadeIn(t1))
        self.wait()
        self.play(
            ReplacementTransform(framebox1.copy(), framebox2),
            ReplacementTransform(t1.copy(), t2),
        )
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Animación 6: Arrow1
        self.camera.background_color = TEAL  # Cambiar el fondo a teal
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        arrow = Arrow(LEFT, RIGHT)
        step1.move_to(LEFT * 2)
        arrow.next_to(step1, RIGHT, buff=0.1)
        step2.next_to(arrow, RIGHT, buff=0.1)
        self.play(Write(step1))
        self.wait()
        self.play(GrowArrow(arrow))
        self.play(Write(step2))
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Animación 7: Arrow2
        self.camera.background_color = PINK  # Cambiar el fondo a rosa
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = Arrow(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Arrow(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Animación 8: LineAnimation
        self.camera.background_color = RED_A  # Cambiar el fondo a rojo
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = Line(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Animación 9: DashedLineAnimation
        self.camera.background_color = ORANGE  # Cambiar el fondo a naranja
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = DashedLine(step1.get_right(), step2.get_left(), buff=0.1)
        arrow1.set_color(RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1)
        arrow2.set_color(BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()
        self.clear()  # Limpiar la pantalla

        # Animación 10: LineAnimation2
        self.camera.background_color = BLUE  # Cambiar el fondo a azul
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        line = Line(step1.get_right(), step2.get_left(), buff=0.1)
        self.play(Write(step1), Write(step2))
        self.play(Create(line))  # Usar Create en lugar de GrowArrow
        self.play(step2.animate.next_to(step2, LEFT * 2))  # Usar animate en lugar de pasar el método directamente
        self.wait()
        self.clear()  # Limpiar la pantalla