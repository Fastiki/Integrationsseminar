from manim import *

img_dir = "img/"

class Farben(MovingCameraScene):
    def rmv_all_objs(self):
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

    def farben(self):
        # Alice, Public and Bob appear
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


        ### Schritt 1 ####
        ### Alice und Bob ###
        alice = Rectangle(width=3, height=2).next_to(alice_text, DOWN * 0.05)
        alice.set_fill(RED, opacity=1)
        alice.set_stroke(RED, width=2)
        alice.scale(0.35)
        bob = Rectangle(width=3, height=2).next_to(bob_text, DOWN * 0.05)
        bob.set_fill(BLUE, opacity=1)
        bob.set_stroke(BLUE, width=2)
        bob.scale(0.35)	

        a = MathTex("a", font_size=40).next_to(alice, DOWN * 2)
        b = MathTex("b", font_size=40).next_to(bob, DOWN * 2)
        n = MathTex("n", font_size=40).next_to(pub, DOWN * 2)


        g_square = Rectangle(width=3, height=2).next_to(n, DOWN * 0.05)
        g_square.set_fill(YELLOW, opacity=1)
        g_square.set_stroke(YELLOW, width=2)
        g_square.scale(0.35)
      
        g = MathTex("g", font_size=40).next_to(g_square, DOWN * 2)

        ### Alice ###
        ag_rectangel = Rectangle(width=3, height=2).next_to(a, DOWN * 5)
        ag_rectangel.set_fill(ORANGE, opacity=1)
        ag_rectangel.set_stroke(ORANGE, width=2)
        ag_rectangel.scale(0.35)

        ag = MathTex("ag", font_size=40).next_to(ag_rectangel, DOWN * 2)

        yellow_copy = g_square.copy()
        yellow_copy.generate_target()
        yellow_copy.target.next_to(ag_rectangel, UP * 0.1)
      
        red_copy = alice.copy()
        red_copy.generate_target()
        red_copy.target.next_to(ag_rectangel, UP * 0.1)

        ag_rectangel.generate_target()
        ag_rectangel.target.next_to(ag_rectangel, RIGHT * 6.5)
        ag.generate_target()
        ag.target.next_to(ag, RIGHT * 10)

        ### Bob ###
        bg_rectangel = Rectangle(width=3, height=2).next_to(b, DOWN * 5)
        bg_rectangel.set_fill(GREEN, opacity=1)
        bg_rectangel.set_stroke(GREEN, width=2)
        bg_rectangel.scale(0.35)

        bg = MathTex("bg", font_size=40).next_to(bg_rectangel, DOWN * 2)

        yellow_b_copy = g_square.copy()
        yellow_b_copy.generate_target()
        yellow_b_copy.target.next_to(bg_rectangel, UP * 0.1)

        blue_copy = bob.copy()
        blue_copy.generate_target()
        blue_copy.target.next_to(bg_rectangel, UP * 0.1)

        bg_rectangel.generate_target()
        bg_rectangel.target.next_to(bg_rectangel, LEFT * 6.5)
        bg.generate_target()
        bg.target.next_to(bg, LEFT * 10)

        ### Animation ###


        self.play(Write(a), Create(alice), run_time=0)

        self.wait(1)

        self.play(Write(b), Create(bob), run_time=0)

        self.wait(1)

        self.play(Write(n), run_time=0)
        
        self.wait(1)

        self.play(Write(g), Create(g_square), run_time=0)

        self.wait(1)

        self.play(
            yellow_copy.animate.move_to(ag_rectangel.get_center()),
            red_copy.animate.move_to(ag_rectangel.get_center()),
            run_time=1
        ) 

        self.play(Write(ag), Create(ag_rectangel), FadeOut(yellow_copy), FadeOut(red_copy), run_time=0)

        self.wait(1)

        self.play(MoveToTarget(ag_rectangel), MoveToTarget(ag))

        self.wait(2)

        self.play(
            yellow_b_copy.animate.move_to(bg_rectangel.get_center()),
            blue_copy.animate.move_to(bg_rectangel.get_center()),
            run_time=1
        ) 

        self.play(Write(bg), Create(bg_rectangel), FadeOut(yellow_b_copy), FadeOut(blue_copy), run_time=0)

        self.wait(1)

        self.play(MoveToTarget(bg_rectangel), MoveToTarget(bg))

        self.wait(2)

        ### Schritt 2 ###
        ### Alice ###
        abg_rectangel = Rectangle(width=3, height=2).next_to(a, DOWN * 2)
        abg_rectangel.set_fill(GRAY_BROWN, opacity=1)
        abg_rectangel.set_stroke(GRAY_BROWN, width=2)
        abg_rectangel.scale(0.35)


        red_a_copy = alice.copy()
        red_a_copy.generate_target()
        red_a_copy.target.next_to(a, DOWN * 2)

        orange_copy = ag_rectangel.copy()
        orange_copy.generate_target()
        orange_copy.target.next_to(a, DOWN * 2)

        abg = MathTex("abg", font_size=40).next_to(abg_rectangel, DOWN * 2)

        ### Bob ###
        abg_b_rectangel = Rectangle(width=3, height=2).next_to(b, DOWN * 2)
        abg_b_rectangel.set_fill(GRAY_BROWN, opacity=1)
        abg_b_rectangel.set_stroke(GRAY_BROWN, width=2)
        abg_b_rectangel.scale(0.35)


        blue_a_copy = bob.copy()
        blue_a_copy.generate_target()
        blue_a_copy.target.next_to(b, DOWN * 2)

        green_copy = bg_rectangel.copy()
        green_copy.generate_target()
        green_copy.target.next_to(b, DOWN * 2)

        abg_b = MathTex("abg", font_size=40).next_to(abg_b_rectangel, DOWN * 2)


        ### Animation ###
        self.play(
            red_a_copy.animate.move_to(abg_rectangel.get_center()),
            orange_copy.animate.move_to(abg_rectangel.get_center()),
            run_time=1
        ) 

        self.play(Write(abg), Create(abg_rectangel), FadeOut(red_a_copy), FadeOut(orange_copy), run_time=0)

        self.wait(2)

        self.play(
            blue_a_copy.animate.move_to(abg_b_rectangel.get_center()),
            green_copy.animate.move_to(abg_b_rectangel.get_center()),
            run_time=1
        ) 

        self.play(Write(abg_b), Create(abg_b_rectangel), FadeOut(blue_a_copy), FadeOut(green_copy), run_time=0)


        self.wait(5)

        # Clear Screen
        self.play(FadeOut(alice_text),
                 FadeOut(bob_text),
                 FadeOut(alice),
                 FadeOut(bob),
                 FadeOut(pub),
                 FadeOut(line1),
                 FadeOut(line2),
                 FadeOut(a),
                 FadeOut(b),
                 FadeOut(n),
                 FadeOut(g),
                 FadeOut(ag),
                 FadeOut(ag_rectangel),
                 FadeOut(bg),
                 FadeOut(bg_rectangel),
                 FadeOut(g_square))
        
        self.wait(2)

        ### Schritt 3 ###
        secret = Text("shared secret", font_size=40)
        self.play(Write(secret))
        self.wait(2)
    
        # make a arrow from bob to alice_bob
        arrow1 = Arrow(abg_rectangel.get_right(), secret.get_left())
        self.play(Create(arrow1), run_time=1.5)

        arrow2 = Arrow(abg_b_rectangel.get_left(), secret.get_right())
        self.play(Create(arrow2), run_time=1.5)

        self.wait(2)


    def construct(self):
        self.farben()