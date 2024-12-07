from manim import *

class Video4(ThreeDScene):
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
        
                
        # Ejemplo 1: Mostrar un círculo en una escena 3D
        circle = Circle()
        self.play(Create(circle))
        self.wait(1)
        self.clear()

        # Cambiar la orientación de la cámara
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=0 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait(1)
        self.clear()

        # Cambiar orientación de la cámara con phi y theta
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait(1)
        self.clear()

        # Cambiar orientación de la cámara con distancia
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6)
        self.play(Create(circle), Create(axes))
        self.wait(1)
        self.clear()

        # Animación de movimiento de cámara
        axes = ThreeDAxes()
        circle = Circle()
        self.play(Create(circle), Create(axes))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait(1)
        self.clear()

        # Animación de rotación y movimiento de cámara
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.begin_ambient_camera_rotation(rate=0.1)  # Rotar cámara automáticamente
        self.wait(5)
        self.stop_ambient_camera_rotation()  # Detener rotación
        self.move_camera(phi=80 * DEGREES, theta=-PI / 2)  # Cambiar posición de cámara
        self.wait(1)
