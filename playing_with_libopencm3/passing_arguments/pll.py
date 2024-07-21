from manim import *

class Pll(Scene):
    def construct(self):
        axes1 = Axes(
            x_range=[-PI/2, 4*PI, PI/2], y_range=[-1.5, 1.5, 1], axis_config={"color":BLUE}, y_length=3
        ).to_edge(UP)

        axes2 = Axes(
            x_range=[-PI/2, 4*PI, PI/2], y_range=[-1.5, 1.5, 1], axis_config={"color":BLUE}, y_length=3
        ).to_edge(DOWN)

        c1_phase = ValueTracker(PI/4)
        c1_frequency = 0.2
        c1_amp = 1
        c1 = always_redraw(
            lambda: axes1.plot(
                lambda t: c1_amp * np.sin(2*PI*c1_frequency*t +c1_phase.get_value()), x_range=[-PI/2, 2*PI], color=ORANGE
            )
        )

        c2_phase = 0
        c2_frequency = 0.2
        c2_amp = 1
        c2 = axes2.plot(
            lambda t: c2_amp * np.sin(2*PI*c2_frequency*t +c2_phase), x_range=[-PI/2, 2*PI], color=GREEN
        )

        self.add(axes1, axes2, c1, c2)
        self.play(c1_phase.animate.set_value(0), run_time=3, rate_func=linear)
        self.wait()