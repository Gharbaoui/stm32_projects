from manim import *

class AdcInterrupts(Scene):
    def construct(self):
        cpu = Square(side_length=1.5, color=WHITE, fill_color=GREY, fill_opacity=1).to_edge(UL, buff=1)
        dma = Square(side_length=1.5, color=WHITE, fill_color=GREEN, fill_opacity=1).to_edge(DL, buff=1)
        isr = Square(side_length=2, color=WHITE, fill_color=ORANGE, fill_opacity=1).to_edge(DR, buff=1)
        main_work = Rectangle(height=.5, width=3, color=GREEN).to_edge(UR, buff=1)
        
        main_work_in_prograss_tracker = ValueTracker(0)
        main_work_in_prograss = always_redraw(
            lambda:
            Rectangle(height=.5,
                             width=main_work_in_prograss_tracker.get_value() * main_work.get_width(),
                             stroke_width=0, fill_color=PINK, fill_opacity=1).
                            move_to(main_work.get_corner(LEFT), aligned_edge=LEFT)
        )

        cpu_title = Text("cpu").move_to(cpu.get_center())
        dma_title = Text("adc").move_to(dma.get_center())
        isr_title = Text("isr").move_to(isr.get_center())
        real_work = Text('"real work"').next_to(main_work, UP, buff=.2).scale(.75)
        cpu_center_pos = cpu.get_center()
        dma_center_pos = dma.get_center()
        
        cpu_dma_line = Line(
            start=[cpu_center_pos[0], cpu_center_pos[1] - cpu.get_width()/2, 0],
            end=[dma_center_pos[0], dma_center_pos[1] + dma.get_width()/2, 0],
            color=RED, stroke_width=5
        )

        cpu_isr_line = Line(
            start=cpu.get_center() + [cpu.get_width()/2, -cpu.get_width()/2, 0],
            end=isr.get_center() + [-isr.get_width()/2, isr.get_width()/2, 0],
            color=ORANGE, stroke_width=4
        )

        cpu_main_work_line = Line(
            start=cpu.get_center() + [cpu.get_width()/2, 0, 0],
            end=main_work.get_center() + [-main_work.get_width()/2, 0, 0],
            color=GREEN, stroke_width=4            
        )
        low_pos = [dma_center_pos[0], dma_center_pos[1] + dma.get_width()/2, 0]
        up_pos = [cpu_center_pos[0], cpu_center_pos[1] - cpu.get_width()/2, 0],
        isr_cpu_s_dot_pos = cpu_isr_line.get_start()
        isr_cpu_s_dot = Dot(color=ORANGE).scale(2).move_to(isr_cpu_s_dot_pos)
        isr_cpu_e_dot_pos = cpu_isr_line.get_end()
        dlow = Dot(color=RED).scale(2).move_to(low_pos)

        mw_s_pos = cpu_main_work_line.get_start()
        mw_e_pos = cpu_main_work_line.get_end()
        mw_dot = Dot(color=GREEN).scale(1.5).move_to(mw_s_pos)

        
        def dma_request_animation(t, ft, work_time, work_rate):
            # work rate 0 to 100% represnting how how much work will be done before the next
            # interrupt
            dstart_dma_cpu = dlow.copy()
            cpu_isr_dstart = isr_cpu_s_dot.copy()
            dstart_mw_dot = mw_dot.copy()
            self.play(dstart_dma_cpu.animate.move_to(up_pos), rate_func=linear, run_time=t)
            self.play(FadeOut(dstart_dma_cpu), run_time=ft)
            self.play(cpu_isr_dstart.animate.move_to(isr_cpu_e_dot_pos),run_time=t)
            self.play(FadeOut(cpu_isr_dstart), run_time=ft)
            self.play(dstart_mw_dot.animate.move_to(mw_e_pos),run_time=t)
            self.play(main_work_in_prograss_tracker.animate.set_value(main_work_in_prograss_tracker.get_value() + work_rate/100), run_time=work_time, rate_func=linear)
            self.play(FadeOut(dstart_mw_dot), run_time=ft)

        self.add(cpu, dma, cpu_dma_line,
                 cpu_title, dma_title, isr, cpu_isr_line, isr_title,
                 main_work, real_work, cpu_main_work_line, main_work_in_prograss
                 )
        

        work_rate = 2
        num_of_interrupts = 8
        for _ in range(num_of_interrupts):
            dma_request_animation(.2, .1, work_rate, 10)
        
        self.wait()