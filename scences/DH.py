from manim import *

from Intro import Intro
from Mathe import Mathe
from Farben import Farben

img_dir = "img/"


class DH(MovingCameraScene):
    def rmv_all_objs(self):
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )


    def construct(self):
        # Intro
        intro = Intro()
        intro.construct()
        # Intro.construct(Intro())

        # Farben.construct(Farben())
        farben = Farben()
        farben.construct()


        mathe = Mathe()
        mathe.construct()

        # Mathe.construct(Mathe())

        # create a alice and bob
        # self.alice_bob()
        # self.rmv_all_objs()

        # self.math()
