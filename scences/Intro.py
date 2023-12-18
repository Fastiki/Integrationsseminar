from manim import *

img_dir = "../img/"

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

        self.rmv_all_objs()

    def reallife(self):
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

        chat_bubbles = SVGMobject(
            img_dir + "chat_bubbles.svg",
            color="white",
            fill_color="white",
        )

        computer_alice = SVGMobject(
            img_dir + "computer.svg",
            color="white",
            fill_color="red",
        )

        computer_bob = SVGMobject(
            img_dir + "computer.svg",
            color="white",
            fill_color="blue",
        )

        computer = SVGMobject(
            img_dir + "computer.svg",
            color="white",
            fill_color="white",
        )

        cross = SVGMobject(
            img_dir + "cross.svg",
            color="red",
            fill_color="red",
        )

        key_alice = SVGMobject(
            img_dir + "key.svg",
            color="white",
            fill_color="gold",
        )

        key_bob = SVGMobject(
            img_dir + "key.svg",
            color="white",
            fill_color="gold",
        )

        mail = SVGMobject(
            img_dir + "mail.svg",
            color="white",
            fill_color="white",
        )
        
        # show alice & bob
        self.add(alice)
        alice.shift(LEFT * 5)

        self.add(bob)
        bob.shift(RIGHT * 5)
        self.wait(1)

        # show the chat bubbles
        chat_bubbles.shift(UP *2)
        self.play(DrawBorderThenFill(chat_bubbles), run_time=1.5)
        self.wait(1)

        # move alice & bob to chat bubbles
        self.play(
            AnimationGroup(
                bob.animate.shift(LEFT * 3), 
                alice.animate.shift(RIGHT * 3)), 
            run_time=2.5)
        self.wait(1)
        
        # morph alice & bob to computer_alice & computer_bob
        computer_bob.shift(RIGHT * 3)
        computer_alice.shift(LEFT * 3)
        self.play(
            Transform(alice, computer_alice),
            Transform(bob, computer_bob),
            run_time=2
        )
        self.wait(1)

        # cross over chat bubble
        cross.shift(UP *2)
        self.play(FadeIn(cross), run_time=1.5)
        self.wait(1) 

        # show three computer
        computer.shift(UP * 2)
        self.play(
            FadeOut(cross),
            FadeOut(chat_bubbles),
            FadeIn(computer),
            bob.animate.shift(RIGHT * 2 + DOWN * 1),
            alice.animate.shift(LEFT * 2 + DOWN * 1),
            run_time=1.5
        )
        self.wait(1)

        # add arrows between all computer & mail symbol
        mail.shift(DOWN * 2)
        mail.set_height(1) 
        mail.set_width(1)

        arrow_alice_bob = DoubleArrow(
                            alice.get_right(), 
                            bob.get_left(), 
                            buff=0, 
                            tip_length=0.4, 
                            color=WHITE
                        )
        
        arrow_mid = Arrow(
                            (alice.get_right() + bob.get_left()) / 2, 
                            computer.get_bottom(), 
                            buff=0, 
                            tip_length=0.4, 
                            color=WHITE
                        )

        self.play(
            GrowFromCenter(arrow_alice_bob),
            GrowArrow(arrow_mid),
            FadeIn(mail),
            run_time=1.5
        )
        self.wait(1)

        # show keys
        key_bob.shift(RIGHT * 5 + DOWN * 2.75)
        key_bob.set_height(1) 
        key_bob.set_width(1)

        key_alice.shift(LEFT * 5 + DOWN * 2.75)
        key_alice.set_height(1) 
        key_alice.set_width(1)

        self.play(
            FadeIn(key_bob),
            FadeIn(key_alice),
            run_time=1.5
        )

        self.wait(1)

        self.play(
            FadeOut(arrow_mid),
            run_time=1
        )

        self.wait(1)
        
        self.play(
            ApplyMethod(arrow_alice_bob.set_color, GREEN),
            run_time=1
        )

        self.wait(3)



    def construct(self):
        #self.intro()
        self.reallife()