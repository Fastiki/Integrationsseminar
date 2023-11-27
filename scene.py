from manim import *


class CreateCircle(Scene):
    def rmv_all_objs(self):
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

    def construct(self):
        # circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        text = Text("PID Controller", font_size=144)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))
        # self.play(Create(circle))  # show the circle on screen
        # self.play(FadeOut(circle))

        k = Tex(r"$P = K_p e(t)$", font_size=100).to_edge(UL)
        i = Tex(r"$I = K_i \int_{0}^{t}e(t)\,dt$", font_size=100).to_edge(LEFT)
        d = Tex(r"$D = K_d \frac{de(t)}{dt}$", font_size=100).to_edge(DL)
        self.play(Write(k))
        self.wait()
        rectangel = Rectangle(height=3, width=5, color=WHITE)
        # self.play(FadeOut(k))
        self.play(Write(i))
        self.wait()
        # self.play(FadeOut(i))
        self.play(Write(d))
        self.wait()
        self.rmv_all_objs()

        # self.wait(5)
        # self.play(FadeOut(d))
