from manim import *


class Toma1(ThreeDScene):
    def construct(self):
        formula = MathTex(
            r"\text{Sea } f\colon [-5,\infty) \to [0,+\infty) \text{ una función}"
        )
        formula.to_edge(UP)
        self.play(Write(formula), run_time=3)
        self.wait(1)

        datos = MathTex(
            r"(i)\quad f(-5) = 4\\"
            r"f(-2) = 0\\"
            r"f(-1) = 0\\"
            r"f(1) = 6"
        )
        datos.next_to(formula, DOWN, buff=1)
        self.play(Write(datos))
        self.wait(2)


class Toma2(ThreeDScene):
    def construct(self):
        formulaDefinicion = MathTex(
            r"(ii) \forall \varepsilon > 0\; \exists N > 0\; \forall x \in \mathrm{Dom}(f)["
            r"\; x > N \Rightarrow \left|f(x) - 3\right| < \varepsilon]"
        )
        formulaDefinicion.to_edge(UP)
        self.play(Write(formulaDefinicion), run_time=3)
        self.wait(1)
        formulaLimite = MathTex(
            r"\lim_{x \to +\infty} f(x) = 3"
        )
        self.play(Write(formulaLimite), run_time=3)
        self.wait(1)


class Toma3(Scene):
    def construct(self):
        formula1 = MathTex(
            r"(iii) \forall M > 0\; \exists \delta > 0\; \forall x \in \mathrm{Dom}(f),\\"
        )
        formula = MathTex(r"\; 0 < -x - 1 < \delta \Rightarrow f(x) > M")
        parte_a1 = MathTex(r"0 < -x - 1 < \delta")
        parte_b1 = MathTex(r"f(x) > M")
        grupo_ab1 = VGroup(parte_a1, parte_b1).arrange(RIGHT, buff=1)
        grupo_principal = VGroup(formula1, formula, grupo_ab1).arrange(DOWN, buff=0.75)
        limite_final = MathTex(r"\lim_{x \to -1^-} +\infty")
        limite_final.next_to(grupo_principal, DOWN, buff=1)
        todo = VGroup(grupo_principal, limite_final).move_to(ORIGIN)
        self.play(Write(formula1), run_time=2)
        self.wait(0.5)
        self.play(Write(formula), run_time=2)
        self.wait(0.5)
        self.play(Write(parte_a1), Write(parte_b1))
        self.wait(1)
        parte_a2 = MathTex(r"1 < -x < \delta + 1").move_to(parte_a1)
        parte_b2 = MathTex(r"f(x) \Rightarrow +\infty").move_to(parte_b1)
        self.play(Transform(parte_a1, parte_a2), Transform(parte_b1, parte_b2))
        self.wait(1.5)
        parte_a3 = MathTex(r"-1 - \delta < -x < -1").move_to(parte_a1)
        self.play(Transform(parte_a1, parte_a3))
        self.wait(1.5)
        parte_a4 = MathTex(r"x \Rightarrow -1").move_to(parte_a1)
        self.play(Transform(parte_a1, parte_a4))
        self.wait(1.5)
        self.play(Write(limite_final))
        self.wait(2)


class Toma4(Scene):
    def construct(self):
        parte1 = MathTex(r"\text{(iv) } f \text{ es continua en }")
        intervalo_rojo = MathTex(r"(-5,-1)").set_color(RED)
        parte2 = MathTex(r"\text{ y en }")
        intervalo_azul = MathTex(r"[-1,+\infty)").set_color(BLUE)
        formula1 = VGroup(parte1, intervalo_rojo, parte2, intervalo_azul).arrange(RIGHT, buff=0.1)
        formula1.move_to(ORIGIN)
        formula2 = MathTex(
            r"\lim_{x \to 5^+} f(x) = f(-5)"
        ).set_color(RED)
        formula3 = MathTex(
            r"\lim_{x \to -1^+} f(x) = f(-1)"
        ).set_color(BLUE)
        formulas = VGroup(formula1, formula2, formula3).arrange(DOWN, buff=0.6)
        formulas.move_to(ORIGIN)
        self.play(Write(formula1))
        self.wait(1)
        self.play(Write(formula2))
        self.wait(1)
        self.play(Write(formula3))
        self.wait(2)


class Toma5(Scene):
    def construct(self):
        formula1 = MathTex(
            r"\text{(v) } f'(x) < 0 \quad \text{cuando} \quad x \in (-5,-2) \cup (1,+\infty)"
        )
        texto1 = MathTex(
            r"> f \text{ es estrictamente decreciente en } (-5,-2)"
        )
        texto2 = MathTex(
            r"> f \text{ es estrictamente decreciente en } (1, +\infty)"
        )
        grupo = VGroup(formula1, texto1, texto2).arrange(DOWN, buff=0.6)
        grupo.move_to(ORIGIN)
        self.play(Write(formula1))
        self.wait(1)
        self.play(Write(texto1))
        self.wait(1)
        self.play(Write(texto2))
        self.wait(2)


class Toma6(Scene):
    def construct(self):
        formula0 = MathTex(
            r"\text{(vi) } f'(x) > 0 \quad \text{cuando} \quad x \in (-2,-1) \cup (-1,1)"
        )
        formula1 = MathTex(
            r"> f \text{ es estrictamente creciente en } (-2,-1)"
        )
        formula2 = MathTex(
            r"> f \text{ es estrictamente creciente en } (-1,1)"
        )
        grupo = VGroup(formula0, formula1, formula2).arrange(DOWN, buff=0.6)
        grupo.move_to(ORIGIN)
        self.play(Write(formula0))
        self.wait(1)
        self.play(Write(formula1))
        self.wait(1)
        self.play(Write(formula2))
        self.wait(2)


class Toma7(Scene):
    def construct(self):
        formula0 = MathTex(
            r"\text{(vii) } f''(x) < 0 \quad \text{cuando} \quad x \in (-5,-2) \cup (-1,1)"
        )
        formula1 = MathTex(
            r"> f \text{ es cóncava hacia abajo en } (-5, -2)"
        )
        formula2 = MathTex(
            r"> f \text{ es cóncava hacia abajo en } (-1, 1)"
        )
        grupo = VGroup(formula0, formula1, formula2).arrange(DOWN, buff=0.6)
        grupo.move_to(ORIGIN)
        self.play(Write(formula0))
        self.wait(1)
        self.play(Write(formula1))
        self.wait(1)
        self.play(Write(formula2))
        self.wait(2)


class Toma8(Scene):
    def construct(self):
        formula0 = MathTex(
            r"\text{(vii) } f''(x) > 0 \quad \text{cuando} \quad x \in (-2,-1) \cup (-1, +\infty)"
        )
        formula1 = MathTex(
            r"> f \text{ es cóncava hacia arriba en } (-2, -1)"
        )
        formula2 = MathTex(
            r"> f \text{ es cóncava hacia arriba en } (1, +\infty)"
        )
        grupo = VGroup(formula0, formula1, formula2).arrange(DOWN, buff=0.6)
        grupo.move_to(ORIGIN)
        self.play(Write(formula0))
        self.wait(1)
        self.play(Write(formula1))
        self.wait(1)
        self.play(Write(formula2))
        self.wait(2)


class Toma9(Scene):
    def construct(self):
        # Crear eje x desde -6 hasta 7
        eje_x = NumberLine(
            x_range=[-6, 7, 1],
            length=13,
            include_tip=True,
            include_numbers=True,
        )
        eje_x.to_edge(DOWN, buff=2)

        # Símbolo [ sobre -5
        corchete_inicio = Tex(r"[", font_size=60)
        corchete_inicio.next_to(eje_x.n2p(-5), UP, buff=0.1)

        # Símbolo ) sobre extremo derecho para +∞
        parentesis_final = Tex(r")", font_size=60)
        parentesis_final.next_to(eje_x.n2p(6.8), UP, buff=0.1)

        # Etiquetas por intervalo
        etiquetas = [
            ("Decreciente", -3.5, UP),
            (r"Cóncava\\hacia\\abajo", -3.5, DOWN),
            ("Creciente", -1.5, UP),
            (r"Cóncava\\hacia\\arriba", -1.5, DOWN),
            ("Creciente", 0, UP),
            (r"Cóncava\\hacia\\abajo", 0, DOWN),
            ("Decreciente", 4, UP),
            (r"Cóncava\\hacia\\arriba", 4, DOWN),
        ]

        textos = VGroup()
        for texto, x, direccion in etiquetas:
            if "Cóncava" in texto:
                t = Tex(texto, font_size=24)
            else:
                t = Text(texto, font_size=15)
            t.next_to(eje_x.n2p(x), direccion, buff=0.6)
            textos.add(t)
        lineas = VGroup()
        for x in [-2, -1, 1]:
            linea = DashedLine(
                start=eje_x.n2p(x) + DOWN * 1,
                end=eje_x.n2p(x) + UP * 1,
                dash_length=0.1,
                color=GRAY,
            )
            lineas.add(linea)
        self.play(Create(eje_x))
        self.play(Write(corchete_inicio), Write(parentesis_final))
        self.play(Create(lineas))
        self.play(Write(textos))
        self.wait(3)

from manim import *

class Toma10(Scene):
    def funcion_fx(self, x):
        return -1 / (x + 1) - 1

    def construct(self):
        # Crear ejes
        axes = Axes(
            x_range=[-6, 7, 1],
            y_range=[-1, 6, 1],
            x_length=13,
            y_length=6,
            axis_config={"include_tip": True, "include_numbers": True},
            x_axis_config={"numbers_to_include": np.arange(-6, 7, 1)},
        )
        axes.to_edge(DOWN, buff=1.5)
        self.play(Create(axes))

        # Función 1: Parábola entre -5 < x < -2
        f1 = axes.plot(
            lambda x: -4/9 * (x + 5)**2 + 4,
            x_range=[-4.99, -2.01],
            color=BLUE,
        )
        self.play(Create(f1))

        # Función 2: Hipérbola tipo, asintótica en x = -1
        # En lugar de usar Create(f2), construimos líneas pequeñas para animar
        x_vals = [x/100 for x in range(-199, -101)]  # -1.99 a -1.01, paso 0.01
        points = [axes.c2p(x, self.funcion_fx(x)) for x in x_vals]
        lines = VGroup()
        for i in range(len(points)-1):
            line = Line(points[i], points[i+1], color=GREEN, stroke_width=3)
            lines.add(line)
        self.add(lines)  # Añadimos antes de animar
        self.play(LaggedStartMap(Create, lines), run_time=3)

        # Función 3: Raíz cuadrada desde (-1, 0) a (1, 4)
        f3 = axes.plot(
            lambda x: 2 * np.sqrt(x + 1),
            x_range=[-1, 1],
            color=YELLOW,
        )
        self.play(Create(f3))

        # Función 4: -|√x| desde (1,4) hacia derecha, asintota en y=3
        f4 = axes.plot(
            lambda x: -np.sqrt(x - 1) + 4,
            x_range=[1.01, 6.8],
            color=RED,
        )
        self.play(Create(f4))

        # Puntos clave
        puntos = VGroup(
            Dot(axes.c2p(-5, 4), color=BLUE),
            Dot(axes.c2p(-2, 0), color=GREEN),
            Dot(axes.c2p(-1, 0), color=YELLOW),
            Dot(axes.c2p(1, 4), color=RED),
        )
        self.play(FadeIn(puntos))

        # Líneas verticales x = -2, -1, 1
        lineas = VGroup()
        for x in [-2, -1, 1]:
            linea = DashedLine(
                start=axes.c2p(x, -1),
                end=axes.c2p(x, 6),
                dash_length=0.1,
                color=GRAY,
            )
            lineas.add(linea)
        self.play(Create(lineas))

        # Asintota horizontal y = 3
        asintota_y = DashedLine(
            start=axes.c2p(1, 3),
            end=axes.c2p(7, 3),
            dash_length=0.1,
            color=GRAY,
        )
        self.play(Create(asintota_y))

        # Corchete y paréntesis
        corchete_inicio = Tex(r"[", font_size=60).next_to(axes.c2p(-5, 0), UP, buff=0.1)
        parentesis_final = Tex(r")", font_size=60).next_to(axes.c2p(6.8, 0), UP, buff=0.1)
        self.play(Write(corchete_inicio), Write(parentesis_final))

        # Etiquetas explicativas
        etiquetas = [
            ("Decreciente", -3.5, UP),
            (r"Cóncava\\hacia\\abajo", -3.5, DOWN),
            ("Creciente", -1.5, UP),
            (r"Asintótica\\en\\x=-1", -1.5, DOWN),
            ("Creciente", 0, UP),
            (r"Raíz", 0, DOWN),
            ("Decreciente", 4, UP),
            (r"Asintótica\\y=3", 4, DOWN),
        ]

        textos = VGroup()
        for texto, x, direccion in etiquetas:
            t = Tex(texto, font_size=24) if "\\" in texto else Text(texto, font_size=15)
            t.next_to(axes.c2p(x, 0), direccion, buff=0.6)
            textos.add(t)
        self.play(FadeIn(textos))
        self.wait(3)