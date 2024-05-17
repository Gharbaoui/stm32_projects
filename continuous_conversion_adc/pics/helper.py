from manim import *

class InputSignal(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 6*np.pi, np.pi/2],
            y_range=[0, 4, 1],
            axis_config={"color": BLUE}
        )
        axis_labels = axes.get_axis_labels(x_label="t", y_label="V")

        def signal_curve_func(x):
            return 1 + np.sin(x) * np.cos(2 * x)

        signal_curve = axes.plot(
            signal_curve_func, x_range=[0, 6*np.pi], color=ORANGE
        )

        self.add(axes, axis_labels)
        self.play(Create(signal_curve), run_time=6, rate_func=linear)
        self.wait()


def get_lines(axes, vertical_lines, color):

    top_points = [line.get_end() for line in vertical_lines]
    path = VMobject()
    path.set_points_as_corners(top_points)
    path.set_color(color)
    return path


class InputSignalWithADC(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 6*np.pi, np.pi/2],
            y_range=[0, 4, 1],
            axis_config={"color": BLUE}
        )
        axis_labels = axes.get_axis_labels(x_label="t", y_label="V")

        def signal_curve_func(x):
            return 1 + np.sin(x) * np.cos(2 * x)

        signal_curve = axes.plot(
            signal_curve_func, x_range=[0, 6*np.pi], color=ORANGE
        )

        num_of_lines1 = 13

        get_v_lines1 = axes.get_vertical_lines_to_graph(
            graph = signal_curve, x_range=[0, 6 * np.pi], num_lines=num_of_lines1
        )

        lines1 = get_lines(axes=axes, vertical_lines=get_v_lines1,color=WHITE)

        num_of_lines2 = num_of_lines1 * 2
        get_v_lines2 = axes.get_vertical_lines_to_graph(
            graph = signal_curve, x_range=[0, 6 * np.pi], num_lines=num_of_lines2, color=GREEN
        )
        lines2 = get_lines(axes=axes, vertical_lines=get_v_lines2, color=GREEN)
        
        num_of_lines3 = num_of_lines1 * 3
        get_v_lines3 = axes.get_vertical_lines_to_graph(
            graph = signal_curve, x_range=[0, 6 * np.pi], num_lines=num_of_lines3, color=PURPLE
        )
        lines3 = get_lines(axes=axes, vertical_lines=get_v_lines3, color=PURPLE)
        

        self.add(axes, axis_labels)
        self.play(Create(signal_curve), run_time=6, rate_func=linear)
        self.play(Create(get_v_lines1), rate_func=linear, run_time=6)
        self.play(Create(lines1), rate_func=linear, run_time=4)
        self.wait(2)
        self.play(FadeOut(get_v_lines1), FadeOut(lines1))
        self.wait()
        self.play(Create(get_v_lines2), rate_func=linear, run_time=6)
        self.play(Create(lines2), rate_func=linear, run_time=4)
        self.wait()
        self.play(FadeOut(get_v_lines2), FadeOut(lines2))
        self.wait()
        self.play(Create(get_v_lines3), rate_func=linear, run_time=6)
        self.play(Create(lines3), rate_func=linear, run_time=4)
        self.wait(2)