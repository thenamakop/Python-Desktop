# celebration.py
from manim import *
import sys


class VictoryAnimation(Scene):
    def construct(self):
        winner = sys.argv[1]
        text = Text(f"{winner} Wins!", font_size=72, color=YELLOW)
        self.play(Write(text))
        self.play(text.animate.scale(1.5).rotate(PI / 4))
        self.play(text.animate.shift(UP * 2).rotate(-PI / 2))
        self.wait(2)


if __name__ == "__main__":
    config.quality = "low_quality"
    VictoryAnimation().render()
