from manim import *

class DiscreteLog(MovingCameraScene):

    def rmv_all_objs(self):
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )

    def intro(self):
            arrow1 = Arrow(start=LEFT, end=RIGHT, color=GREEN).scale(2).shift(1*UP)
            text1 = Text("easy", color=GREEN).next_to(arrow1, UP)
            self.play(Create(arrow1), Write(text1), run_time=2)

            self.wait(2)

            arrow2 = Arrow(start=RIGHT, end=LEFT, color=RED).scale(2).shift(1*DOWN)
            text2 = Text("hard", color=RED).next_to(arrow2, DOWN)
            self.play(Create(arrow2), Write(text2), run_time=2)

            self.wait(2)

            self.rmv_all_objs()

    def discrete_log_simple(self):
        def set_clock_white(atime=2):
            angle_increment = TAU / 12
            start_angle = PI / 2
            sectors = VGroup()  # Group for all sectors

            for i in range(12):
                angle = start_angle - i * angle_increment
                sector = Sector(start_angle=angle, angle=-angle_increment, outer_radius=2, color="black", fill_opacity=1).set_stroke("white", width=3)
                sectors.add(sector) 

            # self.add(sectors)
            self.play(Create(sectors), run_time=atime)

        def animate_sectors(num=12, atime=0.1):

            for i in range(num):
                angle = -i * TAU / 12 + PI / 2
                sector = Sector(start_angle=angle, angle=-TAU / 12, outer_radius=2, color="white", fill_opacity=1)
                sector_with_border = VGroup(sector, sector.copy().set_fill(WHITE, opacity=0).set_stroke(BLACK, width=3))
                
                self.play(Create(sector_with_border), run_time=atime)  

                CLOCK_COUNTER.become(Text(f"Clock Count: {i + 1}", font_size=36, color=WHITE).shift(3*DOWN, 3*LEFT))


        title = Text("46 mod 12", font_size=36).to_edge(UP)
        # self.add(title)
        self.play(Write(title))
        CLOCK_COUNTER = Text("Clock Count: 0", font_size=36, color=WHITE).shift(3*DOWN, 3*LEFT)
        self.play(Write(CLOCK_COUNTER))
        # self.add(CLOCK_COUNTER)

        Clock_ROTATIONS = Text("Clock Rotations: 0", font_size=36, color=WHITE).shift(3*DOWN, 3*RIGHT)
        self.play(Write(Clock_ROTATIONS))
        # self.add(Clock_ROTATIONS)

        set_clock_white(0.15*12)
        self.wait(10)
        animate_sectors(num=12, atime=0.15)
        Clock_ROTATIONS.become(Text(f"Clock Rotations: 1", font_size=36, color=WHITE).shift(3*DOWN, 3*RIGHT))
        set_clock_white(0.2*12)
        animate_sectors(num=12, atime=0.2)
        Clock_ROTATIONS.become(Text(f"Clock Rotations: 2", font_size=36, color=WHITE).shift(3*DOWN, 3*RIGHT))
        set_clock_white(0.25*12)
        animate_sectors(num=12, atime=0.25)
        Clock_ROTATIONS.become(Text(f"Clock Rotations: 3", font_size=36, color=WHITE).shift(3*DOWN, 3*RIGHT))
        set_clock_white(0.45*10)
        animate_sectors(num=10, atime=0.45)
        self.wait(4)

        self.rmv_all_objs()
        self.wait(1)

        erg = Text("46 mod 12 = 10", font_size=36)
        self.play(Write(erg))
        # self.add(erg)
        self.wait(2)

        self.rmv_all_objs()

    def discrete_log_prime(self):

        def set_clock_white():
            angle_increment = TAU / 6
            start_angle = PI / 2
            sectors = VGroup()  

            for i in range(1, 7):
                angle = start_angle - i * angle_increment
                sector = Sector(start_angle=angle, angle=-angle_increment, outer_radius=2, color="black", fill_opacity=1).set_stroke("white", width=3)
                label = MathTex(str(i)).move_to(2.5 * RIGHT * np.cos(angle) + 2.5 * UP * np.sin(angle)).scale(0.5)
                self.add(label)
                sectors.add(sector) 

            self.add(sectors)

        def set_clock_with_colored_sector(colored_sector_index):
            angle_increment = TAU / 6
            start_angle = PI / 2
            sectors = VGroup()
            fill_color = RED  

            for i in range(1, 7):
                angle = start_angle - i * angle_increment

                label = MathTex(str(i)).move_to(2.5 * RIGHT * np.cos(angle) + 2.5 * UP * np.sin(angle)).scale(0.5)
                self.add(label)

                if i == colored_sector_index or i in USED_SECTORS: 
                    sector = Sector(start_angle=angle, angle=-angle_increment, outer_radius=2, color="black", fill_opacity=1, fill_color=fill_color).set_stroke("black", width=3)
                else:
                    sector = Sector(start_angle=angle, angle=-angle_increment, outer_radius=2, color="black", fill_opacity=1).set_stroke("white", width=3)
                sectors.add(sector)

            self.add(sectors)

        def set_clock_with_colored_sector2(colored_sector_index):
            angle_increment = TAU / 6
            start_angle = PI / 2
            sectors = VGroup()
            fill_color = BLUE  

            for i in range(1, 7):
                angle = start_angle - i * angle_increment

                label = MathTex(str(i)).move_to(2.5 * RIGHT * np.cos(angle) + 2.5 * UP * np.sin(angle)).scale(0.5)
                self.add(label)

                if i == colored_sector_index or i in USED_SECTORS2: 
                    sector = Sector(start_angle=angle, angle=-angle_increment, outer_radius=2, color="black", fill_opacity=1, fill_color=fill_color).set_stroke("black", width=3)
                else:
                    sector = Sector(start_angle=angle, angle=-angle_increment, outer_radius=2, color="black", fill_opacity=1).set_stroke("white", width=3)
                sectors.add(sector)

            self.add(sectors)

        USED_SECTORS = []
        title = MathTex(r"3^{a}\mod 7 = ?", font_size=60).to_edge(UP)
        self.play(Write(title))
        self.wait(20)
        
        set_clock_white()
        self.wait(1)

        set_clock_with_colored_sector(6)  
        USED_SECTORS.append(6)
        title1 = MathTex(r"3^{0}\mod 7 = 1", font_size=60).to_edge(UP)
        title.become(title1)
        self.wait(1)

        set_clock_with_colored_sector(2)
        USED_SECTORS.append(2)
        title2 = MathTex(r"3^{1}\mod 7 = 3", font_size=60).to_edge(UP)
        title.become(title2)
        self.wait(1)

        set_clock_with_colored_sector(1)
        USED_SECTORS.append(1)
        title2 = MathTex(r"3^{2}\mod 7 = 2", font_size=60).to_edge(UP)
        title.become(title2)
        self.wait(1)

        set_clock_with_colored_sector(5)
        USED_SECTORS.append(5)
        title2 = MathTex(r"3^{3}\mod 7 = 6", font_size=60).to_edge(UP)
        title.become(title2)
        self.wait(1)

        set_clock_with_colored_sector(3)
        USED_SECTORS.append(3)
        title2 = MathTex(r"3^{4}\mod 7 = 4", font_size=60).to_edge(UP)
        title.become(title2)
        self.wait(1)

        set_clock_with_colored_sector(4)
        USED_SECTORS.append(4)
        title2 = MathTex(r"3^{5}\mod 7 = 5", font_size=60).to_edge(UP)
        title.become(title2)
        self.wait(2)

        title2 = MathTex(r"3^{a}\mod 7", font_size=60).to_edge(UP)
        title.become(title2)

        title3 = Text("a is EQUALLY DISTRIBUTED", font_size=36, color="green").shift(3.5*DOWN)
        self.play(Write(title3))


        # SHOW AGAIN
        USED_SECTORS2 = []    
        set_clock_white()
        self.wait(17)

        set_clock_with_colored_sector2(6)  
        USED_SECTORS2.append(6)
        title1 = MathTex(r"3^{6}\mod 7 = 1", font_size=60).to_edge(UP)
        title.become(title1)
        self.wait(1)

        set_clock_with_colored_sector2(2)
        USED_SECTORS2.append(2)
        title2 = MathTex(r"3^{7}\mod 7 = 3", font_size=60).to_edge(UP)
        title.become(title2)
        self.wait(1)

        set_clock_with_colored_sector2(1)
        USED_SECTORS2.append(1)
        title2 = MathTex(r"3^{8}\mod 7 = 2", font_size=60).to_edge(UP)
        title.become(title2)
        self.wait(1)

        set_clock_with_colored_sector2(5)
        USED_SECTORS2.append(5)
        title2 = MathTex(r"3^{9}\mod 7 = 6", font_size=60).to_edge(UP)
        title.become(title2)
        self.wait(1)

        set_clock_with_colored_sector2(3)
        USED_SECTORS2.append(3)
        title2 = MathTex(r"3^{10}\mod 7 = 4", font_size=60).to_edge(UP)
        title.become(title2)
        self.wait(1)

        set_clock_with_colored_sector2(4)
        USED_SECTORS2.append(4)
        title2 = MathTex(r"3^{11}\mod 7 = 5", font_size=60).to_edge(UP)
        title.become(title2)
        self.wait(20)

        self.rmv_all_objs()


    def compare(self):
        title = Text("Why modulo is useful in encryption", font_size=36).shift(3*UP)
        self.play(Write(title))
        self.wait(1)

        # Einfacher Weg
        formula = MathTex(r"3^{29}\mod 17 = x", font_size=60).shift(1.5*UP + 1*LEFT) 
        self.play(Write(formula))
        self.wait(2)

        text = Text("Easy!", color="green").shift(1.5*UP + 3*RIGHT) 
        self.play(Write(text))
        self.wait(1)

        #Schwerer Weg
        formula2 = MathTex(r"3^{a}\mod 17 = 12", font_size=60).shift(1.5*DOWN + 1*LEFT) 
        self.play(Write(formula2))
        self.wait(2)

        text2 = Text("Hard!", color="red").shift(1.5*DOWN + 3*RIGHT) 
        self.play(Write(text2))
        self.wait(5)

        self.wait(10)
        self.rmv_all_objs()


    def construct(self):
        self.intro()
        self.discrete_log_simple()
        self.discrete_log_prime()
        self.compare()
