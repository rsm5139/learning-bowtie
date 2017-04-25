from bowtie.visual import Plotly
from bowtie.control import Slider
import numpy as np
import plotlywrapper as pw

sine_plot = Plotly()
freq_slider = Slider(caption='frequency', minimum=1, maximum=10, start=5)

def listener(freq):
    if isinstance(freq, list):
        freq = float(freq[0])
    else:
        freq = float(freq)
    t = np.linspace(0, 10, 100)
    sine_plot.do_all(pw.line(t, np.sin(freq * t)).to_json())

from bowtie import command
@command
def construct(path):
    from bowtie import Layout
    description = """
First Bowtie app
===========

Learning Bowtie is fun!
"""
    layout = Layout(description=description,background_color='PaleTurquoise',directory=path)
    layout.add_controller(freq_slider)
    layout.add_visual(sine_plot)
    layout.subscribe(listener, freq_slider.on_change)
    layout.build()