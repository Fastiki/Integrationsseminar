from manim import *

img_dir = "../img/"


class Mathe(MovingCameraScene):
    def rmv_all_objs(self):
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

    def mathe(self):
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

        # insert explenation
        even = MathTex(r"=", font_size=40)

        # remove all objects except alice_bob and bob_alice
        self.play(FadeOut(alice_text),
                  FadeOut(pub),
                  FadeOut(bob_text),
                  FadeOut(a),
                  FadeOut(b),
                  FadeOut(g),
                  FadeOut(n),
                  FadeOut(alice),
                  FadeOut(bob),
                  FadeOut(line1),
                  FadeOut(line2),
                  FadeOut(arrow1),
                  FadeOut(arrow2),
                  run_time=0
                    )
        
        # move alice_bob and bob_alice to top

        self.wait(2)
        self.play(Write(even), run_time=2)

        self.play(alice_bob.animate.to_edge(UL).shift(DOWN * 1, RIGHT * 3), 
                  bob_alice.animate.to_edge(UR).shift(DOWN * 1, LEFT * 3), 
                  even.animate.to_edge(UP).shift(DOWN * 1.2),
                  run_time=2)   
    
        self.wait(2)

        question_mark = (
            SVGMobject(
                img_dir + "question_mark.svg",
                color="white",
                fill_color="white",
            )
            .scale(1.5)
        )

        self.play(Write(question_mark))   
        self.wait(1) 

        self.play(question_mark.animate.shift(LEFT*5))

        self.wait(1)

        self.play(FadeOut(alice_bob),
                  FadeOut(bob_alice),
                  FadeOut(even))
        
        self.wait(2)

        # Create text and speech bubble
        power_rules = [
            MathTex(r"\textbf{Power Rules:}", font_size=40),
            MathTex(r"a^m \cdot a^n = a^{m + n}", font_size=40),
            MathTex(r"\frac{a^m}{a^n} = a^{m - n}", font_size=40),
            MathTex(r"(a^m)^n = a^{m \cdot n}", font_size=40)
        ]

        # Position the text on the screen
        for i, rule in enumerate(power_rules):
            rule.next_to(question_mark, RIGHT * 15.5 + UP * 0.2).shift(DOWN * i)

        bubble = (
            SVGMobject(
                img_dir + "speechbubble.svg")
                .scale(3)
                .set_color(WHITE)
                .set_fill(color=WHITE, opacity=1)
        )

        # Set position of the speech bubble
        bubble.next_to(question_mark, RIGHT*7)


        # Add animations
        self.play(
            Create(bubble),
        )

        self.play(*[Write(rule) for rule in power_rules])

        self.wait(2)

        self.play(power_rules[-1].animate.set_color(YELLOW))

        self.wait(2)

        # remove questionmark and bubble

        self.play(FadeOut(question_mark),
                 FadeOut(bubble),
                 *[FadeOut(rule) for rule in power_rules[:-1]])


        self.play(
            power_rules[-1].animate.to_edge(UP).shift(LEFT * 1.35 + DOWN * 1),
            run_time=2
        )

        self.wait(2)

        self.play(
                FadeIn(alice_bob),
                FadeIn(bob_alice),
                FadeIn(even),
                alice_bob.animate.shift(DOWN * 2),
                bob_alice.animate.shift(DOWN * 2),
                even.animate.shift(DOWN * 2),
        )
        

        self.wait(2)



        bob_short = MathTex(r"g^{ab}\mod n", font_size=40).next_to(even, DOWN * 7)

        arrow_left = Arrow(alice_bob.get_left()+ DOWN * 0.5, bob_short.get_left())
        arrow_right = Arrow(bob_alice.get_right()+ DOWN * 0.5, bob_short.get_right())

        self.play(Create(arrow_left),
                  Create(arrow_right), run_time=1.5)
    
        self.play(Write(bob_short))

        self.wait(2)

        self.play(FadeOut(arrow_left),
                  FadeOut(arrow_right),
                  FadeOut(alice_bob),
                  FadeOut(bob_alice),
                  FadeOut(even),
                  FadeOut(power_rules[-1]))
        
        self.wait(2)


        alice_short = bob_short.copy()
        # bob_short.next_to(arrow_left.get_end(), LEFT)

        self.play(FadeIn(alice_text),
                  FadeIn(pub),
                  FadeIn(bob_text),
                  FadeIn(a),
                  FadeIn(b),
                  FadeIn(g),
                  FadeIn(n),
                  FadeIn(alice),
                  FadeIn(bob),
                  FadeIn(line1),
                  FadeIn(line2),
                  FadeIn(arrow1),
                  FadeIn(arrow2),
                  run_time=2
                    )
        
        self.wait(2)

        self.play(bob_short.animate.next_to(arrow1.get_end(), LEFT),
                  alice_short.animate.next_to(arrow2.get_end(), RIGHT),
                  run_time=2)
        
        self.wait(2)


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
        self.mathe()
        self.rmv_all_objs()
        self.lets_say()
        self.rmv_all_objs()
        self.rotation_pointer()
        self.rmv_all_objs()