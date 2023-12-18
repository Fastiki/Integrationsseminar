from manim import *

img_dir = "..img/"

class Math(MovingCameraScene):
    def rmv_all_objs(self):
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

    def math(self):
        alice_text = Text("Alice", font_size=40)
        self.play(Write(alice_text))
        self.play(alice_text.animate.to_edge(UL).shift(DOWN * 1, RIGHT * 1), run_time=2)
        bob_text = Text("Bob", font_size=40)
        self.play(Write(bob_text))
        self.play(bob_text.animate.to_edge(UR).shift(DOWN * 1, LEFT * 1), run_time=2)

        pub = Text("Public", font_size=40)
        self.play(Write(pub))
        self.play(pub.animate.to_edge(UP).shift(DOWN * 1), run_time=2)

        help_line1 = Line(alice_text.get_right(), pub.get_left())
        help_line2 = Line(pub.get_right(), bob_text.get_left())

        line1 = Line(
            help_line1.get_center() + UP * 1, help_line1.get_center() + DOWN * 6
        )

        line2 = Line(
            help_line2.get_center() + UP * 1, help_line2.get_center() + DOWN * 6
        )

        self.play(Create(line1), run_time=2)
        self.play(Create(line2), run_time=2)

        # draw a vertical line from top to botom between alice and bob

        # draw a line between bob and public from top to bottom
        # line2 = Line(bob_text.get_top(), pub.get_bottom())
        # self.play(Create(line2), run_time=2)
        a = MathTex("a", font_size=40).next_to(alice_text, DOWN * 2)
        b = MathTex("b", font_size=40).next_to(bob_text, DOWN * 2)
        g = MathTex("g", font_size=40).next_to(pub, DOWN * 2)
        n = MathTex("n", font_size=40).next_to(g, DOWN * 2)

        alice = MathTex(r"g^a\mod n", font_size=40).next_to(a, DOWN * 2)
        bob = MathTex(r"g^b\mod n", font_size=40).next_to(b, DOWN * 2)

        self.play(Write(a))

        self.wait(1)

        self.play(Write(b))

        self.wait(1)

        self.play(Write(g))

        self.wait(1)

        self.play(Write(n))

        self.wait(1)

        self.play(Write(alice))
        self.wait(1)

        self.play(Write(bob))

        self.wait(1)

        alice_bob = MathTex(r"(g^b)^a\mod n", font_size=40).next_to(alice, DOWN * 6)
        bob_alice = MathTex(r"{(g^a)}^{b}\mod n", font_size=40).next_to(bob, DOWN * 6)

        # make a arrow from bob to alice_bob
        arrow1 = Arrow(bob.get_left(), alice_bob.get_right())
        self.play(Create(arrow1), run_time=1.5)
        self.play(Write(alice_bob))

        arrow2 = Arrow(alice.get_right(), bob_alice.get_left())
        self.play(Create(arrow2), run_time=1.5)
        self.play(Write(bob_alice))

        self.wait(1)

        bob_short = MathTex(r"g^{ab}\mod n", font_size=40).next_to(bob_alice, DOWN * 2)

        self.play(Write(bob_short))

        self.wait(1)

        alice_short = MathTex(r"g^{ba}\mod n", font_size=40).next_to(
            alice_bob, DOWN * 2
        )

        self.play(Write(alice_short))

        self.wait(1)


    def construct(self):
        self.math()