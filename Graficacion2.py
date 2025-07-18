from manim import *

# Comentarios generados por copilot para futura modificacion por parte de un tercero

class Toma1(ThreeDScene):
    def construct(self):
        formula = MathTex(
            r"\text{Graficar } f\left(x\right)\:=\:\frac{e^x}{x}"
        )
        formula.to_edge(UP)
        self.play(Write(formula), run_time=3)
        self.wait(1)

        lineas_texto = [
            "Para esto, determine:",
            "> El dominio de f",
            "> Las asíntotas de f",
            "> Los p.c de f",
            "> Los intervalos de monotonía",
            "> Los intervalos de concavidad",
            "> Los puntos de inflexión"
        ]

        textos = VGroup(*[
            Text(linea, font_size=26).set_x(-5)
            for linea in lineas_texto
        ])
        textos.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        textos.next_to(formula, DOWN, buff=1)

        for linea in textos:
            self.play(Write(linea))
            self.wait(1.5)


class Toma2(ThreeDScene):
    def construct(self):
        formula1 = MathTex(
            r"(i)\quad x \ne 0\\",
            font_size=48
        )

        formula2 = MathTex(
            r"\text{dom } f = \mathbb{R} - \{0\}\\",
            font_size=48
        )
        formula2.set_color_by_tex("{0}", RED)

        formula3 = MathTex(
            r"\text{dom}(f) = (-\infty, 0)\; \cup\; (0, +\infty)\\",
            font_size=48
        )

        formulas = VGroup(formula1, formula2, formula3).arrange(DOWN, aligned_edge=ORIGIN, buff=0.7)

        for formula in formulas:
            self.play(Write(formula))
            self.wait(1.5)


class Toma3(ThreeDScene):
    def construct(self):
        f1 = MathTex(
            r"(ii)\quad f \text{ es continua en su dominio.}",
            font_size=42
        )
        f2 = MathTex(
            r"\text{Por tanto, } f \text{ no tiene asíntotas verticales } x = c \text{ con } c \in \text{dom } f.",
            font_size=42
        )
        f3 = MathTex(
            r"\text{No obstante, } \lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \left( \frac{e^x}{x} \right) = \left( \frac{1}{0} \right) = +\infty",
            font_size=42
        )
        f4 = MathTex(
            r"\lim_{x \to 0^-} f(x) = -\infty",
            font_size=42
        )
        f5 = MathTex(
            r"\text{Por lo tanto, } x = 0 \text{ es una asíntota vertical de } f.",
            font_size=42
        )

        formulas = VGroup(f1, f2, f3, f4, f5).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        formulas.to_edge(UP)

        for formula in formulas:
            self.play(Write(formula))
            self.wait(1.5)


class Toma4(ThreeDScene):
    def construct(self):
        f1 = MathTex(
            r"(ii)\ \text{Por un lado, } \lim_{x \to -\infty} \frac{e^x}{x} = \lim_{x \to -\infty} e^x \cdot \lim_{x \to -\infty} \frac{1}{x} = e^{-\infty} \cdot \frac{1}{-\infty}",
            font_size=30
        )
        f2 = MathTex(
            r"= 0 \cdot 0 = 0",
            font_size=30
        )
        f3 = MathTex(
            r"\text{Por tanto, } \lim_{x \to -\infty} \frac{e^x}{x} = 0",
            font_size=30
        )

        f4 = MathTex(
            r"\text{Por otro lado, } \lim_{x \to +\infty} \frac{e^x}{x} = \lim_{x \to +\infty} e^x \cdot \lim_{x \to +\infty} \frac{1}{x} = \infty \cdot 0\ \text{ (indeterminada)}",
            font_size=30
        )
        f5 = MathTex(
            r"\text{Aplicamos L'Hôpital: } \lim_{x \to +\infty} \frac{e^x}{x} = \lim_{x \to +\infty} \frac{\frac{d}{dx}(e^x)}{\frac{d}{dx}(x)}",
            font_size=30
        )
        f6 = MathTex(
            r"= \lim_{x \to +\infty} \frac{e^x}{1} = +\infty",
            font_size=30
        )
        f7 = MathTex(
            r"\text{Por tanto, } y = 0 \text{ es la única asíntota horizontal de } f",
            font_size=30
        )

        formulas = VGroup(f1, f2, f3, f4, f5, f6, f7).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        formulas.to_edge(UP)
        self.play(Write(f1))
        self.wait(1.5)
        self.play(TransformFromCopy(f1, f2))
        self.wait(1.5)
        self.play(Write(f3))
        self.wait(1.5)
        self.play(Write(f4))
        self.wait(1.5)
        self.play(TransformFromCopy(f4, f5))
        self.wait(1.5)
        self.play(TransformFromCopy(f5, f6))
        self.wait(1.5)
        self.play(Write(f7))
        self.wait(2)


class Toma5(ThreeDScene):
    def construct(self):
        f1 = MathTex(
            r"(ii)\ \lim_{x \to +\infty} \frac{f(x)}{x} = \dots",
            font_size=42
        )
        f1.to_edge(UP)
        self.play(Write(f1))
        self.wait(1.5)

        f2 = MathTex(
            r"\lim_{x \to \infty} \frac{e^x}{x^2} \rightarrow \frac{\infty}{\infty}",
            font_size=42
        )
        self.play(Write(f2))
        self.wait(1.5)

        f3 = MathTex(
            r"\lim_{x \to \infty} \frac{e^x}{2x} \rightarrow  \frac{\infty}{\infty}",
            font_size=42
        )
        f3.move_to(f2)
        self.play(Transform(f2, f3))
        self.wait(1.5)

        f4 = MathTex(
            r"\lim_{x \to \infty} \frac{1}{2} \cdot e^x = +\infty",
            font_size=42
        )
        f4.move_to(f3)
        self.play(Transform(f2, f4))
        self.wait(1.5)

        f5 = MathTex(
            r"\text{Así, } f \text{ no tiene asíntotas oblicuas.}",
            font_size=42
        )
        f5.next_to(f2, DOWN, buff=1)
        self.play(Write(f5))
        self.wait(2)


class Toma6(ThreeDScene):
    def construct(self):
        f1 = MathTex(
            r"(ii)\ \text{Dom } f \text{ no es un intervalo que contiene sus extremos, así que } f \text{ no tiene p.c. fronterizos.}",
            font_size=30
        )
        f1.to_edge(UP)
        self.play(Write(f1))
        self.wait(2)

        f2a = MathTex(
            r"\text{Por otro lado, } f'(x) = \frac{(x - 1)e^x}{x^2}",
            font_size=30
        )
        f2a.next_to(f1, DOWN, buff=0.5)
        self.play(Write(f2a))
        self.wait(1.5)

        f2b = MathTex(
            r"= \frac{xe^x - e^x}{x^2}",
            font_size=30
        )
        f2b.next_to(f2a, DOWN, buff=0.3)
        self.play(TransformFromCopy(f2a, f2b))
        self.wait(1.5)

        f3 = MathTex(
            r"\text{Así que } f' \text{ no está definida para } x = 0 \text{ y } f'(x) = 0 \text{ pero } 0\notin dom\:f",
            font_size=30
        )
        f3.next_to(f2b, DOWN, buff=0.5)
        self.play(Write(f3))
        self.wait(2)


class Toma7(ThreeDScene):
    def construct(self):
        f1 = MathTex(
            r"(iii)\ \text{En resumen:}",
            font_size=42
        )
        f1.to_edge(UP)
        self.play(Write(f1))
        self.wait(2)

        f2 = MathTex(
            r"a)\ \text{f no tiene puntos críticos fronterizos.}",
            font_size=42
        )
        f2.next_to(f1, DOWN, buff=0.5)
        self.play(Write(f2))
        self.wait(2)

        f3 = MathTex(
            r"b)\ \text{f no tiene puntos críticos singulares.}",
            font_size=42
        )
        f3.next_to(f2, DOWN, buff=0.5)
        self.play(Write(f3))
        self.wait(2)

        f4 = MathTex(
            r"c)\ x = 1\ \text{es un punto crítico estacionario.}",
            font_size=42
        )
        f4.next_to(f3, DOWN, buff=0.5)
        self.play(Write(f4))
        self.wait(2)


class Toma8(Scene):
    def construct(self):
        linea_h = Line(LEFT * 6, RIGHT * 6)
        self.add(linea_h)

        linea_0 = DashedLine(UP * 3 + ORIGIN, DOWN * 3 + ORIGIN)
        linea_1 = DashedLine(UP * 3 + RIGHT * 4, DOWN * 3 + RIGHT * 4)
        self.add(linea_0, linea_1)
        p1 = MathTex(r"(", font_size=50).move_to(LEFT * 6 + UP * 0.05)
        p2 = MathTex(r")", font_size=50).move_to(LEFT * 0.05 + UP * 0.05)

        p3 = MathTex(r"(", font_size=50).move_to(RIGHT * 0.06 + UP * 0.05)
        p4 = MathTex(r")", font_size=50).move_to(RIGHT * 3.95 + UP * 0.05)

        p5 = MathTex(r"(", font_size=50).move_to(RIGHT * 4.05 + UP * 0.05)
        p6 = MathTex(r")", font_size=50).move_to(RIGHT * 6 + UP * 0.05)
        self.add(p1, p2, p3, p4, p5, p6)

        txt_menos_inf = MathTex(r"-\infty", font_size=30).move_to(LEFT * 6 + DOWN * 0.3)
        txt_0 = MathTex(r"0", font_size=30).move_to(RIGHT * 0.2 + DOWN * 0.3)
        txt_1 = MathTex(r"1", font_size=30).move_to(RIGHT * 4.3 + DOWN * 0.3)
        txt_mas_inf = MathTex(r"+\infty", font_size=30).move_to(RIGHT * 6.8 + DOWN * 0.3)
        self.add(txt_menos_inf, txt_0, txt_1, txt_mas_inf)

        f1 = MathTex(r"f\:'\left(-1\right)\:=\:-2e^{-1}\:<\:0", font_size=36).shift(LEFT * 4 + UP * 2.5)
        f1abajo1 = MathTex(r"f'(x) < 0", font_size=32).next_to(f1, DOWN, buff=0.6).align_to(f1, LEFT)

        f2 = MathTex(r"f'\left(\frac{1}{2}\right) < 0", font_size=36).next_to(f1, RIGHT, buff=3).shift(DOWN * -0.1)
        f2abajo2 = MathTex(r"f'(x) < 0", font_size=32).next_to(f2, DOWN, buff=0.5).align_to(f2, LEFT)

        f3 = MathTex(r"f'(2) > 0", font_size=36).next_to(f2, RIGHT * 0.57, buff=3).shift(DOWN * -0.1)
        f3abajo3 = MathTex(r"f'(x) > 0", font_size=32).next_to(f3, DOWN, buff=0.6).align_to(f3, LEFT)

        texto_final = MathTex(r"f \text{ es estrictamente decreciente en } (-\infty,0)", font_size=36).to_edge(DOWN)

        self.play(Write(f1), Write(f1abajo1))
        self.wait(1.5)

        self.play(Write(f2), Write(f2abajo2))
        self.wait(1.5)

        self.play(Write(f3), Write(f3abajo3))
        self.wait(1.5)

        self.play(Write(texto_final))
        self.wait(2)


class Toma9(ThreeDScene):
    def construct(self):
        f0 = MathTex(
            r"(v)",
            font_size=42
        )
        f0.to_edge(UP)
        self.play(Write(f0))
        self.wait(1)

        f1 = MathTex(
            r"f'\left(x\right)=\:\left(x-1\right)e^x x^{-2}",
            font_size=42
        )
        f1.next_to(f0, DOWN, buff=0.8).move_to(ORIGIN)
        self.play(Write(f1))
        self.wait(1.5)

        f2 = MathTex(
            r"f''\left(x\right)=\:e^x x^{-2}+\left(x-1\right)e^x x^{-2}-2\left(x-1\right)e^x x^{-3}",
            font_size=42
        )
        f2.move_to(f1)
        self.play(Transform(f1, f2))
        self.wait(1.5)

        f3 = MathTex(
            r"f''\left(x\right)=\:\frac{e^x}{x^3}\left(x+x\left(x-1\right)-2\left(x-1\right)\right)",
            font_size=42
        )
        f3.move_to(f1)
        self.play(Transform(f1, f3))
        self.wait(1.5)

        f4 = MathTex(
            r"f''\left(x\right)=\:\frac{e^x}{x^3}\left(x^2 - 2x + 2\right)",
            font_size=42
        )
        f4.move_to(f1)
        self.play(Transform(f1, f4))
        self.wait(1.5)

        f5 = MathTex(
            r"f'' \text{ existe en todo el dominio y } f'' \text{ nunca es 0.}",
            font_size=42
        )
        f5.next_to(f4, DOWN, buff=0.8).align_to(f0, ORIGIN)
        self.play(Write(f5))
        self.wait(2)


class Toma10(Scene):
    def construct(self):
        linea_h = Line(LEFT * 6, RIGHT * 6)
        self.add(linea_h)
        linea_0 = DashedLine(UP * 3 + ORIGIN, DOWN * 2 + ORIGIN)
        self.add(linea_0)
        txt_0 = MathTex(r"0", font_size=30).move_to(RIGHT * 0.2 + DOWN * 0.3)
        self.add(txt_0)
        p1 = MathTex(r")", font_size=50).move_to(LEFT * 0.05 + UP * 0.05)
        p2 = MathTex(r"(", font_size=50).move_to(RIGHT * 0.06 + UP * 0.05)
        self.add(p1, p2)
        txt_menos_inf = MathTex(r"-\infty", font_size=30).move_to(LEFT * 6 + DOWN * 0.3)
        txt_mas_inf = MathTex(r"\infty", font_size=30).move_to(RIGHT * 6 + DOWN * 0.3)
        self.add(txt_menos_inf, txt_mas_inf)

        f1 = MathTex(r"f\:''\left(-1\right)\:=\:-5e^{-1}\:<\:0", font_size=36).shift(LEFT * 3 + UP * 2.5)
        f1abajo1 = MathTex(r"f''(x) < 0", font_size=32).next_to(f1, DOWN, buff=0.6).align_to(f1, LEFT)

        f2 = MathTex(r"f\:''\left(1\right)\:=\:e>0", font_size=36).next_to(f1, RIGHT, buff=3).shift(DOWN * -0.1)
        f2abajo2 = MathTex(r"f''(x) > 0", font_size=32).next_to(f2, DOWN, buff=0.5).align_to(f2, LEFT)


        self.play(Write(f1), Write(f1abajo1))
        self.wait(1.5)

        self.play(Write(f2), Write(f2abajo2))
        self.wait(1.5)

        texto_concava_abajo = MathTex(r"f \text{ es cóncava hacia abajo en } (-\infty,0)", font_size=36).to_edge(DOWN * 2.5)
        texto_concava_arriba = MathTex(r"f \text{ es cóncava hacia arriba en } (0,\infty)", font_size=36).to_edge(DOWN).shift(DOWN * 0.1)

        self.play(Write(texto_concava_abajo))
        self.wait(2)

        self.play(Write(texto_concava_arriba))
        self.wait(2)

class Toma11(Scene):
    def construct(self):
        f1 = MathTex(
            r"(vi)\quad f\ \text{no tiene puntos de inflexión}",
            font_size=42
        )
        f1.move_to(ORIGIN)
        self.play(Write(f1))
        self.wait(2)


class Toma12(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 7, 1],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True},
            x_axis_config={"numbers_to_include": [-3, -2, -1, 0, 1, 2, 3]},
            y_axis_config={"numbers_to_include": [1, 2, 3, 4, 5, 6]},
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        graph = axes.plot(
            lambda x: np.exp(x) / x,
            x_range=[-4, -0.1, 0.01],
            color=BLUE
        )
        graph2 = axes.plot(
            lambda x: np.exp(x) / x,
            x_range=[0.1, 4, 0.01],
            color=BLUE
        )

        dashed_y_axis = DashedLine(
            start=axes.c2p(0, -10),
            end=axes.c2p(0, 6.5),
            color=RED
        )

        dashed_x1_up = DashedLine(
            start=axes.c2p(1, 1.2),
            end=axes.c2p(1, 7),
            color=RED
        )
        dashed_x1_down = DashedLine(
            start=axes.c2p(1, -2),
            end=axes.c2p(1, 0.8),
            color=RED
        )

        txt_izq_arriba = Tex("decreciente", font_size=30).move_to(axes.c2p(-2.2, 1))
        txt_izq_abajo = Tex("cóncava hacia abajo", font_size=30).move_to(axes.c2p(-2.2, -2.5))

        txt_centro_arriba = Tex("decreciente", font_size=30).move_to(axes.c2p(0.75, 1))
        txt_centro_abajo = Tex("cóncava hacia arriba", font_size=30).move_to(axes.c2p(2.2, -2.5))

        txt_der_arriba = Tex("creciente", font_size=30).move_to(axes.c2p(2.5, 1))

        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Create(graph2))
        self.play(Create(dashed_y_axis), Create(dashed_x1_up), Create(dashed_x1_down))
        self.play(
            Write(txt_izq_arriba),
            Write(txt_izq_abajo),
            Write(txt_centro_arriba),
            Write(txt_centro_abajo),
            Write(txt_der_arriba),
        )
        self.wait(3)
