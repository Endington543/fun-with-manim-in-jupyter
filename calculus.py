from manim import *


class IntegralBases(Scene):
    def construct(self):
        sp = self.play
        sw = self.wait

        # Construct starting axes
        ax = Axes(
            x_range=[-4 * PI, 4 * PI, PI],
            y_range=[-5,5,1],
            tips=False,
            y_axis_config={"include_numbers": True, "unit_size": 1},
            x_axis_config={"unit_size": 1}
        )

        x_labels = [MathTex("-4 \pi"), MathTex("-3 \pi"),
                    MathTex("-2 \pi"), MathTex("- \pi"),
                    MathTex("\pi"), MathTex("2 \pi"),
                    MathTex("3 \pi"), MathTex("4 \pi")]
        
        multiple = -4
        x_labels_group = VGroup()
        for i in range(len(x_labels)):
            if multiple == 0:
                multiple += 1
            
            x_labels[i].next_to(ax.x_axis.n2p(multiple * PI), DOWN)
            x_labels_group.add(x_labels[i])
            multiple += 1

        sp([Create(ax), Write(x_labels_group)], run_time=3)

        sw()
        
        sin_func = ax.plot(
            lambda x: 4 * np.sin(1 / 2 * x + PI / 2),
            color=RED_A
        )
        
        sp(Create(sin_func))
        
        sw()
        
        area = ax.get_riemann_rectangles(sin_func, dx=0.5, stroke_color=GREY)
        
        sp(DrawBorderThenFill(area), run_time=3)
        
        sw()
        
        
        
        self.interactive_embed()