from manim import *

class ADC(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 1], x_length=8,
            y_range=[0,6, 1],
            axis_config={"color": BLUE},
        ).to_edge(DR).add_coordinates()

        e = ValueTracker(0)

        rect = RoundedRectangle(corner_radius=.2, height=.5,color=RED).to_edge(UL)
        joystick_pos = Rectangle(height=.25, width=.2, color=BLUE_B, fill_opacity=.4).move_to(rect.get_left() + RIGHT/4)

        controller_title=Tex("joystick").next_to(rect, UP, buff=.2)

        joystick_pos = Rectangle(height=.25, width=.2, color=BLUE_B, fill_opacity=.4).move_to(rect.get_left() + RIGHT/4)

        curve = axes.plot(
            lambda t: 5*t, x_range=[0, 1], color=YELLOW
        )

        dividing_line = Line(
            start = axes.coords_to_point(0, 2.5),
            end = axes.coords_to_point(1, 2.5), color=RED
        )

        dividing_line.set_z_index(0)
        curve.set_z_index(1)

        bottom_box = Rectangle(stroke_width=0,width=8,height=2.5,color=BLUE_B, fill_opacity=.3).move_to(axes.coords_to_point(0, 0)+RIGHT*4+UP*5/4)
        top_box = Rectangle(stroke_width=0,width=8,height=2.5,color=PINK, fill_opacity=.3).move_to(axes.coords_to_point(0, 0)+RIGHT*4+(UP*5/4)+(UP*2.5))


        axis_labels = axes.get_axis_labels(x_label=Tex("joystick-position"), y_label=Tex("output-voltage"))
        playstation_controller = VGroup(rect, joystick_pos, controller_title).shift(DOWN)
        self.add(axes, axis_labels, playstation_controller)

        self.play(joystick_pos.animate.move_to(rect.get_right() - RIGHT/4), Create(curve), rate_func=linear, run_time=4)
        self.wait()
        self.play(GrowFromCenter(bottom_box), Create(top_box))
        self.play(Create(dividing_line))
        self.wait(4)
