from manim import *
from random import randint

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

class DMAContinuousRequests(Scene):
    def construct(self):
        # constants
        dma_buffer_size = 6
        # sensor
        sensor_shape = Square(side_length=1.5, color=WHITE, fill_color=[GREY,WHITE], fill_opacity=.8)
        sensor_title = Text('sensor').scale(.5)
        sensor = VGroup(sensor_shape, sensor_title).to_edge(LEFT, buff=.5)

        # adc
        adc_color=[BLUE, PURPLE]
        adc_shape = Square(side_length=1.5, color=BLUE, fill_color=adc_color, fill_opacity=.8)
        adc_title = Text('ADC').scale(.5)
        adc = VGroup(adc_shape, adc_title).to_edge(LEFT, buff=1).shift(3.5*RIGHT)

        # dma
        dma_shape = Square(side_length=1.5, color=BLUE, fill_color=[PINK,GREEN], fill_opacity=.8)
        dma_title = Text('DMA').scale(.5)
        dma = VGroup(dma_shape, dma_title).to_edge(LEFT, buff=1).shift(6.5*RIGHT)

        # cpu
        cpu_shape = Square(side_length=1.5, color=BLUE, fill_color=[PURPLE,RED], fill_opacity=.8)
        cpu_title = Text('CPU').scale(.5)
        cpu = VGroup(cpu_shape, cpu_title).to_edge(DR, buff=1)

        #sensor adc connection
        sensor_to_adc_line = Line(
            start = sensor_shape.get_center() + [sensor_shape.get_width()/2, 0, 0],
            end=adc_shape.get_center() + [-adc_shape.get_width()/2, 0, 0], color=GREEN
        )

        #sensor signal
        analog_signal_graph = ParametricFunction(
            lambda t: [t, 0.5*np.sin(2*t), 0], t_range=[0, 2*np.pi], color=RED
        ).scale([sensor_to_adc_line.get_length()/(2*np.pi), 1, 1])
        analog_signal_graph.shift(sensor_to_adc_line.get_start()-analog_signal_graph.get_start())

        # adc dma connection
        adc_to_dma_line = Line(
              start = adc_shape.get_center() + [adc_shape.get_width()/2, 0, 0],
            end=dma_shape.get_center() + [-dma_shape.get_width()/2, 0, 0], color=BLUE_B
        ).add_tip()

        # cpu dma connection
        dma_to_cpu_line = Line(
              start = dma_shape.get_corner(RIGHT+DOWN),
            end=cpu_shape.get_corner(LEFT+UP), color=GREEN
        ).add_tip()

        # animation related
        def flash_line(line, speed, original_color=None, next_color=RED):
            if original_color == None:
                original_color = line.get_color()
            self.play(line.animate.set_color(next_color), run_time=speed)
            self.play(line.animate.set_color(original_color), run_time=speed)

        def flash_adc():
            self.play(adc_shape.animate.set_color(RED_B), run_time=.3)
            self.play(adc_shape.animate.set_color(adc_color), run_time=.3)
        
        next_memory_location_to_write = 0
        t = Text("cpu got interrupt").scale(.5).next_to(dma_to_cpu_line, UP, buff=.2).rotate(dma_to_cpu_line.get_angle())
        def adc_to_dma_to_memory_animation(adc_dma_line, dma_mem_line,
                                 speed=.1, original_color=None, next_color=RED):
            flash_adc()
            flash_line(line=adc_dma_line, speed=speed, original_color=original_color, next_color=next_color)
            flash_line(line=dma_mem_line, speed=speed*1.5, original_color=original_color, next_color=next_color)
            nonlocal next_memory_location_to_write
            update_memory_location(next_memory_location_to_write, randint(0, 99))
            next_memory_location_to_write += 1
            if next_memory_location_to_write == dma_buffer_size:
                flash_line(line=dma_to_cpu_line, speed=speed, original_color=original_color, next_color=next_color)
                self.play(Write(t), run_time=.5)
                self.play(FadeOut(t))
            next_memory_location_to_write = next_memory_location_to_write % dma_buffer_size

        def update_memory_location(index, value):
            new_text = Text(str(value)).scale(.5).move_to(array_of_10[0][index][1].get_center())
            self.play(Transform(array_of_10[0][index][1],new_text))

        # array creation
        def get_array(num_of_elements, length=10, color=GREEN, surrounding_color=BLUE):
            width=length/(num_of_elements + num_of_elements/4)
            squares_shape = VGroup(*[VGroup(Square(side_length=width, color=color), Text("xx", color=WHITE).scale(.5))
                                     for _ in range(num_of_elements)]).arrange(RIGHT)
            return VGroup(squares_shape, SurroundingRectangle(squares_shape, color=surrounding_color)).to_edge(UR)

        array_of_10 = get_array(dma_buffer_size)

        # dma memory connection
        dma_to_memory_location_line = Line(
            start = dma.get_center() + [0, dma.get_width()/2, 0],
            end=array_of_10.get_center() + [0, -array_of_10.get_height()/2, 0],color=YELLOW
        ).add_tip()

        self.add(sensor, adc, sensor_to_adc_line, dma, adc_to_dma_line, array_of_10, dma_to_memory_location_line, cpu, dma_to_cpu_line, analog_signal_graph)
        # self.play(Create(analog_signal_graph), rate_func=linear)
        # self.wait()
        # flash_line(adc_to_dma_line, .2)
        for _ in range(dma_buffer_size*2):
            adc_to_dma_to_memory_animation(adc_to_dma_line, dma_to_memory_location_line)

        self.wait(2)