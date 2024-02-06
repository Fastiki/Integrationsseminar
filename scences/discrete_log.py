from manim import *

class DiscreteLog(MovingCameraScene):

    def discrete_log(self):
        def set_clock_white():
            angle_increment = TAU / 12
            start_angle = PI / 2
            sectors = VGroup()  # Group for all sectors

            for i in range(12):
                angle = start_angle - i * angle_increment
                sector = Sector(start_angle=angle, angle=-angle_increment, outer_radius=2, color="white", fill_opacity=1).set_stroke("black", width=3)
                sectors.add(sector) 

            self.add(sectors)

        def animate_sectors(num=12, atime=0.1):

            for i in range(num):
                angle = -i * TAU / 12 + PI / 2
                sector = Sector(start_angle=angle, angle=-TAU / 12, outer_radius=2, color="red", fill_opacity=1)
                sector_with_border = VGroup(sector, sector.copy().set_fill(WHITE, opacity=0).set_stroke(WHITE, width=3))
                
                self.play(Create(sector_with_border), run_time=atime)  

                CLOCK_COUNTER.become(Text(f"Clock Count: {i + 1}", font_size=36, color=WHITE).shift(3*DOWN, 3*LEFT))


        title = Text("46 mod 12", font_size=36).to_edge(UP)
        self.add(title)
        CLOCK_COUNTER = Text("Clock Count: 0", font_size=36, color=WHITE).shift(3*DOWN, 3*LEFT)
        self.add(CLOCK_COUNTER)

        Clock_ROTATIONS = Text("Clock Rotations: 0", font_size=36, color=WHITE).shift(3*DOWN, 3*RIGHT)
        self.add(Clock_ROTATIONS)

        set_clock_white()
        self.wait(2)
        animate_sectors(num=12, atime=0.15)
        Clock_ROTATIONS.become(Text(f"Clock Rotations: 1", font_size=36, color=WHITE).shift(3*DOWN, 3*RIGHT))
        set_clock_white()
        animate_sectors(num=12, atime=0.2)
        Clock_ROTATIONS.become(Text(f"Clock Rotations: 2", font_size=36, color=WHITE).shift(3*DOWN, 3*RIGHT))
        set_clock_white()
        animate_sectors(num=12, atime=0.25)
        Clock_ROTATIONS.become(Text(f"Clock Rotations: 3", font_size=36, color=WHITE).shift(3*DOWN, 3*RIGHT))
        set_clock_white()
        animate_sectors(num=10, atime=0.45)
        self.wait(2)


    def construct(self):
        self.discrete_log()
