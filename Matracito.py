from manim import *

class Matracitoo(Scene):
    def construct(self):
        # Crear el texto "Matracito"
        title = Text("Matracito").scale(2)  # Escalar para hacerlo más grande
        # Animaciones para el texto
        self.play(Write(title))  # Escribe el título
        self.wait()
        # Transformación del título
        transform_title = Text("Matracito ...").scale(1.5)
        transform_title.to_corner(UP + LEFT)
        self.play(Transform(title, transform_title))  # Transforma el título
        self.wait()

        #SE CREA EL TRIANGULOOOOOOOOO
        triangle = Triangle().set_color('#00B0F0').set_fill('#00B0F0', opacity=1).scale(3)  # Relleno azul con opacidad completa
        triangle.move_to(DOWN)
        self.play(DrawBorderThenFill(triangle))  # Dibujar y rellenar el triángulo
        self.wait()

        #SE CREA EL RECTANGULOOOOOOOOOOO
        rectangle = Rectangle(height=2, width=0.9).set_color('#00B0F0').set_fill('#00B0F0', opacity=1)  # Rectángulo azul, pequeño y relleno
        rectangle.next_to(triangle, UP, buff=-1.4)  # Colocarlo cerca de la punta del triángulo
        self.play(DrawBorderThenFill(rectangle))  # Dibujar y rellenar el rectángulo
        self.wait()

        # SE CREA LA ELIPSEEEEEEE
        ellipse = Ellipse(width=0.9, height=0.4).set_color('#C1E5F5').set_fill('#C1E5F5', opacity=1)  # Elipse azul con relleno
        ellipse.next_to(rectangle, UP, buff=-0.2) 
        self.play(DrawBorderThenFill(ellipse)) 
        self.wait()

        # SE CREAN LOS CIRCULOS BLANCOS DE LOS OJOS EN LA PARTE DERECHE E IZQUIERDA 
        circle = Circle(radius=0.5, color=WHITE).set_fill(WHITE, opacity=1)  # Círculo blanco
        circlee = Circle(radius=0.5, color=WHITE).set_fill(WHITE, opacity=1)
        circle.move_to(triangle.get_vertices()[1] + np.array([3.3, 2, 9]))  # Colocar el círculo a la derecha de la punta del triángulo
        circlee.move_to(triangle.get_vertices()[1] + np.array([2, 2, 2]))  # Colocar el círculo a la izquierda de la punta del triángulo
        self.play(DrawBorderThenFill(circle), DrawBorderThenFill(circlee))  
        self.wait()

        # SE CREAN LOS SEGUNDOS CIRCULOS DE LOS OJOS EN COLOR NEGRO (LOS QUE VAN ADENTRO) EN AMBOS LADOS
        circle = Circle(radius=0.36, color=BLACK).set_fill(BLACK, opacity=1)  # Círculo negro
        circle2 = Circle(radius=0.36, color=BLACK).set_fill(BLACK, opacity=1)  
        pos_right = triangle.get_vertices()[1] + np.array([3.45, 1.89, 0])  # Posición a la derecha de la punta del triángulo
        pos_left = triangle.get_vertices()[1] + np.array([1.88, 1.88, 0])  # Posición a la izquierda de la punta del triángulo
        circle.move_to(pos_right)
        circle2.move_to(pos_left)
        self.play(DrawBorderThenFill(circle), DrawBorderThenFill(circle2))  
        self.wait()

        # SE CREA EL TERCER CIRULO PEQUEÑO BLANCO DE LOS OJOS, EN AMBOS LADOS 
        circle = Circle(radius=0.1, color=WHITE).set_fill(WHITE, opacity=1) #círculo blanco
        ciircle = Circle(radius=0.1, color=WHITE).set_fill(WHITE, opacity=1) 
        circle.move_to(triangle.get_vertices()[1] + np.array([3.3, 1.99, 8]))  # Colocar el círculo a la derecha de la punta del triángulo
        ciircle.move_to(triangle.get_vertices()[1] + np.array([2, 1.99, 8]))  # Colocar el círculo a la izquierda de la punta del triángulo
        self.play(DrawBorderThenFill(circle), DrawBorderThenFill(ciircle)) 
        self.wait()

        # SE CREA EL CUARTO CIRCULO DE LOS OJOS, EN AMBOS LADOS MUCHO MAS PEQUEÑO 
        circle = Circle(radius=0.01, color=WHITE).set_fill(WHITE, opacity=1)  # Círculo blanco
        circcle = Circle(radius=0.01, color=WHITE).set_fill(WHITE, opacity=1) 
        circle.move_to(triangle.get_vertices()[1] + np.array([3.65, 1.89, 8]))  # Colocar el círculo a la derecha de la punta del triángulo
        circcle.move_to(triangle.get_vertices()[1] + np.array([1.68, 1.89, 8]))  # Colocar el círculo a la izquierda de la punta del triángulo
        self.play(DrawBorderThenFill(circle),DrawBorderThenFill(circcle))  
        self.wait()

        # SE CREA LA PEQUEÑA LINEA DE LA BOCAAAAAA
        line = Line(
            start=triangle.get_center() + np.array([-0.4, -1.2, 0]),  # Punto inicial desplazado hacia la izquierda
            end=triangle.get_center() + np.array([0.4, -1.2, 0]),  # Punto final desplazado hacia la derecha
            color=BLACK
        )
        self.play(Create(line))  # Mostrar la línea inicialmente
        self.wait(2)  # Esperar 2 segundo

        # Obtener las coordenadas de los vértices del triángulo
        vertices = triangle.get_vertices()
        # Coordenadas de la "hipotenusa" (línea inferior del triángulo)
        left_vertex = vertices[0]  # Vértice izquierdo
        right_vertex = vertices[2]  # Vértice derecho
        # Encontrar el punto medio de la hipotenusa
        midpoint = (left_vertex + right_vertex) / 2
        # Crear la línea diagonal desde el punto medio hacia arriba a la derecha
        diagonal_line = Line(
            start=midpoint,
            end=midpoint + np.array([1, 1.5, 0]),  # Ajustar la longitud y dirección de la línea
            color=WHITE
        )
        # Crear la línea diagonal desde el punto medio hacia arriba a la izquierda (como un efecto espejo)
        diagonal_line_left = Line(
            start=midpoint + np.array([-2.6, 0, 0]),  # Desplazar más a la izquierda, manteniendo la altura
            end=midpoint + np.array([-2.6 - 1, 1.5, 0]),  # Mantener el ángulo reflejado (diagonal hacia arriba a la izquierda)
            color=WHITE
        )
        self.play(Create(diagonal_line), Create(diagonal_line_left))
        self.wait()

        # SE CREAN LAS PIERNAS DE MATRACITOOOOOOOO
        vertical_line1 = Line(
            start=triangle.get_bottom() + np.array([-0.5, 0, 0]),  # Ajustar la posición en la base del triángulo
            end=triangle.get_bottom() + np.array([-0.5, -1, 0]),  # Mantener la misma longitud
            color=WHITE
        )
        vertical_line2 = Line(
            start=triangle.get_bottom() + np.array([0.5, 0, 0]), 
            end=triangle.get_bottom() + np.array([0.5, -1, 0]),  
            color=WHITE
        )
        self.play(Create(vertical_line1), Create(vertical_line2))
        self.wait()

        # SE CREAN LAS PATITAAAAS DE MATRACITOOOO
        horizontal_line1 = Line(
            start=vertical_line1.get_end() + np.array([-0.2, 0.27, 0]),  # Elevar hacia arriba
            end=vertical_line1.get_end() + np.array([0.2, 0.27, 0]),  # Mover a la derecha
            color=WHITE
        )
        horizontal_line2 = Line(
            start=vertical_line2.get_end() + np.array([-0.2, 0.27, 0]), 
            end=vertical_line2.get_end() + np.array([0.2, 0.27, 0]), 
            color=WHITE
        )
        self.play(Create(horizontal_line1), Create(horizontal_line2))
        self.wait()

        # ===== Para diagonal_line (primera línea diagonal) =====
        # Obtener la posición de la punta de la línea diagonal
        end_point = diagonal_line.get_end()
        # Calcular la dirección de la línea diagonal
        direction = (end_point - diagonal_line.get_start()) / np.linalg.norm(end_point - diagonal_line.get_start())  # Normalizar la dirección
        # Retroceder 0.3 unidades desde el extremo de la línea diagonal
        offset = 0.3  
        # Nueva posición para las líneas cortas
        short_line_start = end_point - direction * offset  # Retrocede desde el extremo de la línea diagonal
        # Asegúrate de que short_line_start esté dentro de los límites de la línea diagonal
        if np.linalg.norm(short_line_start - diagonal_line.get_start()) < 0.1:  # Verifica que no se desplace demasiado
            short_line_start = diagonal_line.get_start() + direction * 0.1  # Coloca la línea un poco más cerca del inicio
        # Crear las líneas cortas para diagonal_line
        short_line1 = Line(
            start=short_line_start,
            end=short_line_start + np.array([-0.2, 0.2, 0]),  # Línea corta hacia la izquierda
            color=WHITE
        )
        short_line2 = Line(
            start=short_line_start,
            end=short_line_start + np.array([0.2, 0, 0.2]),  # Línea corta hacia la derecha
            color=WHITE
        )
        # Animar las líneas cortas en diagonal_line
        self.play(Create(short_line1), Create(short_line2))
        # ===== Para diagonal_line_left (segunda línea diagonal, como reflejo) =====
        # Obtener la posición de la punta de la línea diagonal_left
        end_point_left = diagonal_line_left.get_end()
        # Calcular la dirección de la línea diagonal_left
        direction_left = (end_point_left - diagonal_line_left.get_start()) / np.linalg.norm(end_point_left - diagonal_line_left.get_start())  # Normalizar la dirección
        # Retroceder 0.3 unidades desde el extremo de la línea diagonal_left
        offset_left = 0.3 
        # Nueva posición para las líneas cortas en diagonal_line_left
        short_line_start_left = end_point_left - direction_left * offset_left  # Retrocede desde el extremo de la línea diagonal
        # Asegúrate de que short_line_start_left esté dentro de los límites de la línea diagonal_left
        if np.linalg.norm(short_line_start_left - diagonal_line_left.get_start()) < 0.1:  # Verifica que no se desplace demasiado
            short_line_start_left = diagonal_line_left.get_start() + direction_left * 0.1  # Coloca la línea un poco más cerca del inicio
        # Crear las líneas cortas para diagonal_line_left
        short_line1_left = Line(
            start=short_line_start_left,
            end=short_line_start_left + np.array([0.2, 0.2, 0]),  # Línea corta hacia la izquierda
            color=WHITE
        )
        short_line2_left = Line(
            start=short_line_start_left,
            end=short_line_start_left + np.array([-0.2, 0, 0.2]),  # Línea corta hacia la derecha
            color=WHITE
        )
        self.play(Create(short_line1_left), Create(short_line2_left))
        self.wait()

        # SE CAMBIA LA BOCA ORIGINAL  POR UNA TRISTE
        u_shape = Arc(
            radius=0.4,  # Tamaño del arco
            start_angle=0,  # Ángulo de inicio del arco en radianes 0=eje positivo en x 
            angle=PI,  # Ángulo total del arco
            color=BLACK
        ).shift(triangle.get_center() + np.array([0, -1.2, 0])) 
        self.play(FadeOut(line))  # Desaparecer la línea
        self.play(FadeIn(u_shape))  # Mostrar la boca nueva
        self.wait()

        # Crear el texto "Adióoooooos"
        final = Text("Adióoooooos").scale(1)
        final.to_edge(DOWN+LEFT*0.4)
        self.play(Write(final))
        self.wait()
