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
        self.wait(3)
        self.play(FadeOut(intro))

        self.wait(1)

        self.rmv_all_objs()

        text = Text("1976", font_size=40).to_edge(UP, 0.5)
        diffie = Text("Whitfield Diffie", font_size=40).to_edge(DOWN + LEFT)
        hellman = Text("Martin Hellman", font_size=40).to_edge(DOWN + RIGHT)
        ax1x2 = Text("ax1x2", font_size=40)
        martin = ImageMobject(img_dir + "Martin-Hellman.jpg").to_edge(RIGHT, 2).scale(2)
        whitfield = ImageMobject(img_dir + "Whitfield_Diffie.png").to_edge(LEFT, 2).scale(2)
        self.play(Write(text), run_time=1)

        self.wait(1)

        self.play(Write(diffie), FadeIn(whitfield), run_time=1)

        self.wait(1)

        self.play(Write(hellman), FadeIn(martin), run_time=1)

        self.wait(1)

        self.play(Write(ax1x2), run_time=1)

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

        text_alice = Text("Alice")
        text_alice.next_to(alice, DOWN)
        alice_group = VGroup(alice, text_alice)
        self.play(DrawBorderThenFill(alice), Write(text_alice), run_time=1.5)
        self.wait(0.5)
        self.play(alice_group.animate.shift(LEFT * 5), run_time=1.5)

        self.wait(1)

        text_bob = Text("Bob")
        text_bob.next_to(bob, DOWN)
        bob_group = VGroup(bob, text_bob)
        self.play(DrawBorderThenFill(bob), Write(text_bob), run_time=1.5)
        self.wait(0.5)
        self.play(bob_group.animate.shift(RIGHT * 5), run_time=1.5)

        self.wait(3)

        # show the chat bubbles
        chat_bubbles.shift(UP * 2)
        self.play(DrawBorderThenFill(chat_bubbles), run_time=1.5)
        self.wait(1)

        # move alice & bob to chat bubbles
        self.play(
            AnimationGroup(
                bob_group.animate.shift(LEFT * 3),
                alice_group.animate.shift(RIGHT * 3),
            ),
            run_time=2.5,
        )
        self.wait(5)

        # morph alice & bob to computer_alice & computer_bob
        computer_bob.shift(RIGHT * 3)
        computer_alice.shift(LEFT * 3)
        self.play(
            Transform(alice, computer_alice),
            Transform(bob, computer_bob),
            text_alice.animate.move_to(computer_alice.get_bottom() + DOWN * 0.5),
            text_bob.animate.move_to(computer_bob.get_bottom() + DOWN * 0.5),
            run_time=2,
        )
        self.wait(1)

        bob_group = VGroup(bob, text_bob)
        alice_group = VGroup(alice, text_alice)

        # cross over chat bubble
        cross.shift(UP * 2)
        self.play(FadeIn(cross), run_time=1.5)
        self.wait(1)

        # show three computer
        computer.shift(UP * 2)
        self.play(
            FadeOut(cross),
            FadeOut(chat_bubbles),
            bob_group.animate.shift(RIGHT * 2 + DOWN * 1),
            alice_group.animate.shift(LEFT * 2 + DOWN * 1),
            run_time=1.5,
        )
        self.wait(3)

        self.play(FadeIn(computer))


        # add arrows between all computer & mail symbol
        mail.shift(DOWN * 2)
        mail.set_height(1)
        mail.set_width(1)

        arrow_alice_bob = DoubleArrow(
            alice.get_right(), bob.get_left(), buff=0.1, tip_length=0.4, color=WHITE
        )

        arrow_mid = Arrow(
            (alice.get_right() + bob.get_left()) / 2,
            computer.get_bottom(),
            buff=0,
            tip_length=0.4,
            color=WHITE,
        )
        
        self.wait(3)

        self.play(
            GrowFromCenter(arrow_alice_bob),
            FadeIn(mail),
            run_time=1.5,
        )
        self.wait(1)

        self.play(GrowArrow(arrow_mid))

        # show keys
        key_bob.shift(RIGHT * 5 + UP)
        key_bob.set_height(1)
        key_bob.set_width(1)

        key_alice.shift(LEFT * 5 + UP)
        key_alice.set_height(1)
        key_alice.set_width(1)

        self.play(FadeIn(key_bob), FadeIn(key_alice), run_time=1.5)

        self.wait(3)

        self.play(FadeOut(arrow_mid), run_time=1)

        self.wait(1)

        self.play(ApplyMethod(arrow_alice_bob.set_color, GREEN), run_time=1)

        self.wait(3)

    def construct(self):
        self.intro()
        self.reallife()
        self.rmv_all_objs()
