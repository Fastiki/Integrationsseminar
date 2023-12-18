from manim import *

img_dir = "img/"

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

    def construct(self):
        self.intro()