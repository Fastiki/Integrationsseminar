from manim import *

img_dir = "..img/"

class Intro(MovingCameraScene):
    def rmv_all_objs(self):
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

    def intro(self):
        # Intro
        intro = Text("Diffie-Hellman Key Exchange", font_size=60)
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))

        self.wait(2)

        self.rmv_all_objs()

        # create a alice and bob
        alice = SVGMobject(
            img_dir + "frau.svg",
            color="white",
            fill_color="red",
        )

        eve = SVGMobject(
            img_dir + "frau.svg",
            color="white",
            fill_color="white",
        )

        bob = SVGMobject(
            img_dir + "mann.svg",
            color="white",
            fill_color="blue",
        )

        self.play(DrawBorderThenFill(alice), run_time=1.5)
        self.play(alice.animate.shift(LEFT * 5), run_time=1.5)
        text_alice = Text("Alice")
        text_alice.next_to(alice, DOWN)
        self.play(Write(text_alice))

        self.wait(1)

        self.play(DrawBorderThenFill(bob), run_time=1.5)
        self.play(bob.animate.shift(RIGHT * 5), run_time=1.5)
        text = Text("Bob")
        text.next_to(bob, DOWN)
        self.play(Write(text), run_time=1)

        self.wait(3)

        # create a arrow from alice to bob and back
        arrow1 = Arrow(alice.get_right() + UP * 0.25, bob.get_left() + UP * 0.25)
        self.play(Create(arrow1), run_time=1.5)

        self.wait(2)

        arrow2 = Arrow(bob.get_left() + DOWN * 0.25, alice.get_right() + DOWN * 0.25)
        self.play(Create(arrow2), run_time=1.5)

        self.wait(1)

    def construct(self):
        self.intro()