from manim import *

img_dir = "../img/"


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

    def create_numbers(self, quantity, circle):
        numbers = []
        for i in range(quantity):  # Change 12 to the number of numbers you want
            angle = (
                -i * TAU / quantity + TAU / 4
            )  # Change 12 to the number of numbers you want
            number = Text(str(i + 1)).scale(
                0.5
            )  # Change the scale if the numbers are too small/big
            number.move_to(
                circle.point_at_angle(angle) * 1.2
            )  # Change 1.2 to move the numbers closer/farther from the circle
            numbers.append(number)
        return numbers

    def rotation_pointer(self):
        # Create a circle
        circle = Circle(radius=3, color=BLUE)
        # Create a line
        line = Line(circle.get_center(), circle.get_top())
        # Add the circle and line to the scene
        self.add(circle, line)

        # Group the circle and numbers
        numbers = self.create_numbers(20, circle)

        # Create the numbers
        group = VGroup(circle, line, *numbers)

        # self.add(group)
        self.play(DrawBorderThenFill(group), run_time=4, rate_functions=linear)

        self.wait(2)

        # Rotate the line around the center of the circle
        self.play(
            Rotate(line, 1.2 * PI * 30, about_point=circle.get_center(), run_time=10),
            rate_func=exponential_decay,
            repeat=1,
        )

        self.wait(2)

        # Move the circle to the right
        self.play(group.animate.shift(LEFT * 3), run_time=2)

        self.wait(2)

        outcome = Text("1", font_size=40).to_edge(UP).shift(DOWN * 1, RIGHT * 4)

        formular = MathTex(r"g^{a}\mod 20 = 1").to_edge(UP).shift(DOWN * 1, RIGHT * 4)

        self.play(Write(formular))

        self.wait(2)

        # create a alice and bob
        question_mark = (
            SVGMobject(
                img_dir + "question_mark.svg",
                color="white",
                fill_color="white",
            )
            .next_to(formular, DOWN * 6)
            .scale(1.5)
        )

        self.play(Write(question_mark))

        self.wait(2)

    def lets_say(self):
        a = MathTex("a=10", font_size=60).to_edge(UP)
        g = MathTex("g=3", font_size=60).to_edge(UP).shift(DOWN * 1)
        n = MathTex("n=17", font_size=60).to_edge(UP).shift(DOWN * 2)

        self.play(Write(a), run_time=1.5)
        self.wait(1)
        self.play(Write(g), run_time=1.5)
        self.wait(1)
        self.play(Write(n), run_time=1.5)
        self.wait(1)

        formular = MathTex(r"g^{a}\mod n", font_size=60).to_edge(UP).shift(DOWN * 4)

        self.play(Write(formular), run_time=1.5)

        self.wait(2)

        formular_with_numbers = MathTex(r"3^{10}\mod 17").move_to(formular)

        self.play(Transform(formular, formular_with_numbers), run_time=1.5)

        formular_with_result = MathTex(r"3^{10}\mod 17 = 5").move_to(formular)

        self.wait(2)

        self.play(Transform(formular, formular_with_result), run_time=1.5)

        self.wait(1)

        group = VGroup(a, g, n, formular)

        self.play(group.animate.move_to(RIGHT * 2 + UP *2).scale(0.7), run_time=1.5)

    def construct(self):
        # self.math()
        self.lets_say()
        self.rotation_pointer()
        pass
