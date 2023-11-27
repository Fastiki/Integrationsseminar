from manim import *


class CreateCircle(MovingCameraScene):
    def rmv_all_objs(self):
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

    def construct(self):
        # Intro
        text = Text("PID Controller", font_size=144)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))

        greeting = Text("How do we move this robot?", color = BLUE, font="Noto Sans", font_size=50)
        explaination = Text("This can be accomplished by using PID controller!", font="Noto Sans", font_size=30)
        greeting.shift(2*UP)
        self.play(Write(greeting))
  
        square = Square()
        square.move_to(3*LEFT)
        square.generate_target()
        square.target.shift(5*RIGHT)
        dot = Square(color=RED)
        dot.move_to(square.target.get_center())
        self.add(square, dot)
        self.play(
            FadeIn(dot)
        )
        self.play(
            MoveToTarget(square, run_time=5.0)
        )
        self.wait(1)
        self.play(FadeOut(square), 
            FadeOut(dot),
            FadeOut(greeting))

        self.play(Write(explaination))        
        self.play(FadeOut(explaination))

        k = Tex(r"$P = K_p e(t)$", font_size=40)
        i = Tex(r"$I = K_i \int_{0}^{t}e(t)\,dt$", font_size=40)
        d = Tex(r"$D = K_d \frac{de(t)}{dt}$", font_size=40)

        c1 = Circle(radius=0.5, color=WHITE, fill_opacity=0).to_edge(LEFT)
        c1_text = Tex(r"$\sum$", font_size=50).next_to(c1.get_left())
        self.play(Write(c1))
        self.play(Write(c1_text))

        r1 = Rectangle(height=1, width=3.5, color=WHITE).to_edge(UL).shift(DOWN * 1, RIGHT * 4)
        r2 = Rectangle(height=1, width=3.5, color=WHITE).next_to(r1, DOWN * 4)
        r3 = Rectangle(height=1, width=3.5, color=WHITE).next_to(r2, DOWN * 4)

        arrow1 = Arrow(c1.get_edge_center(RIGHT), r1.get_edge_center(LEFT), buff=0)
        arrow2 = Arrow(c1.get_edge_center(RIGHT), r2.get_edge_center(LEFT), buff=0)
        arrow3 = Arrow(c1.get_edge_center(RIGHT), r3.get_edge_center(LEFT), buff=0)


        self.play(Write(r1))
        self.play(Write(arrow1))

        self.play(Write(r2))
        self.play(Write(arrow2))

        self.play(Write(r3))
        self.play(Write(arrow3))

        # Save the state of camera
        self.camera.frame.save_state()

        # Animation of the camera
        self.play(self.camera.frame.animate.move_to(r1).set(width=r1.width * 1.2))
        # test = Text("k", font_size=40)
        # self.play(Write(test.next_to(r1.get_left())))
        # self.play(ReplacementTransform(test, k))
        self.play(Write(k.next_to(r1.get_left())))
        self.play(self.camera.frame.animate.move_to(r2))
        self.play(Write(i.next_to(r2.get_left())))
        self.play(self.camera.frame.animate.move_to(r3))
        self.play(Write(d.next_to(r3.get_left())))
        self.wait()

        # Restore the state saved
        self.play(Restore(self.camera.frame))

        c2 = Circle(radius=0.5, color=WHITE, fill_opacity=0).next_to(r2, RIGHT * 10)
        c2_text = Tex(r"$\sum$", font_size=50).next_to(c2.get_left())
        self.play(Write(c2))
        self.play(Write(c2_text))

        arrow4 = Arrow(r1.get_edge_center(RIGHT), c2.get_edge_center(LEFT), buff=0)
        arrow5 = Arrow(r2.get_edge_center(RIGHT), c2.get_edge_center(LEFT), buff=0)
        arrow6 = Arrow(r3.get_edge_center(RIGHT), c2.get_edge_center(LEFT), buff=0)

        self.play(Write(arrow4))
        self.play(Write(arrow5))
        self.play(Write(arrow6))

        a = ArcBetweenPoints(c2.get_bottom(), c1.get_bottom(), angle=TAU / -3).add_tip()
        self.play(Write(a))

        self.wait(2)
        # self.play(FadeOut(d))

        # write code that animates how the PID controller works
