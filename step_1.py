from bowtie.visual import Plotly
from bowtie.control import Slider, Number
from bowtie import cache
import numpy as np
import plotlywrapper as pw
import plotly.plotly as py
import plotly.graph_objs as go

#
# Initialize our values
#
# This prevents an empty page from loading
#
def initialize():
    cache.save('scheduled',30)
    top_left(5)
    top_right(0.5)
    middle_left(3)
    middle_right(30)

#
# Scheduled function
#
def timed_event():
    ticker = cache.load('scheduled')
    ticker -= 1
    if ticker < 0:
        ticker = 0
    middle_right(ticker)
    cache.save('scheduled',ticker)

#
# Top Row
#
sine_plot1 = Plotly()
freq_slider1 = Slider(caption='Left Plot', minimum=1, maximum=10, start=5, step=1)
sine_plot2 = Plotly()
freq_slider2 = Slider(caption='Right Plot', minimum=0.1, maximum=1, start=0.5, step=0.1)

def top_left(freq):
    freq = float(freq)
    t = np.linspace(0, 10, 100)
    sine_plot1.do_all(pw.line(t, np.sin(freq * t)).to_json())
    
def top_right(freq):
    freq = float(freq)
    t = np.linspace(0, 10, 100)
    sine_plot2.do_all(pw.line(t, np.sin(freq * t)).to_json())

#
# Middle Row
#
sine_plot3 = Plotly()
freq_number1 = Number(caption='Left Plot', minimum=1, maximum=10, start=3, step=1)
sine_plot4 = Plotly()
#freq_number2 = Slider(caption='Right Plot', minimum=0.1, maximum=1, start=0.5, step=0.1)

def middle_left(freq):
    freq = float(freq)
    t = np.linspace(0, 10, 100)
    sine_plot3.do_all(pw.line(t, np.sin(freq * t)).to_json())
    
def middle_right(n):
    #freq = float(freq)
    #t = np.linspace(0, 10, 100)
    #sine_plot4.do_all(pw.line(t, np.sin(freq * t)).to_json())
    #sine_plot4.progress.do_visible(True)
    #sine_plot4.progress.do_percent(n)
    
    fig = {
      "data": [
        {
          "values": [30-n, n],
          "marker": {"colors": ["white", "green"]},
          "textposition":"inside",
          "name": "Timer",
          "hoverinfo":"none",
          "hole": .9,
          "showlegend": False,
          "textinfo": "none",
          "sort": False,
          "direction": "clockwise",
          "type": "pie"
        }],
      "layout": {
            "title":"Remaining Time",
            "annotations": [
                {
                    "font": {
                        "size": 100
                    },
                    "showarrow": False,
                    "text": str(n)
                }
            ]
        }
    }
    sine_plot4.do_all(fig)
    #py.iplot(fig)

#
# Bowtie section
#
from bowtie import command
@command
def construct(path):
    from bowtie import Layout
    description = """
First Bowtie app
===========

Learning Bowtie is fun!

"""
    layout = Layout(rows=3,columns=12,description=description,background_color='PaleTurquoise',directory=path,debug=True)
    # Schedule a task
    # You must edit server.py manually after build for this to work
    layout.schedule(1,timed_event) # Edit server.py ->socketio.run(app, host=host, port=port, use_reloader=False)
    # Add controllers to the sidebar
    layout.add_sidebar(freq_slider1)
    layout.add_sidebar(freq_slider2)
    layout.add_sidebar(freq_number1)
    # Add the visuals
    layout.add(sine_plot1,row_start=0,column_start=0,row_end=0,column_end=5)
    layout.add(sine_plot2,row_start=0,column_start=6,row_end=0,column_end=11)
    layout.add(sine_plot3,row_start=1,column_start=0,row_end=1,column_end=5)
    layout.add(sine_plot4,row_start=1,column_start=6,row_end=1,column_end=11)
    # Reaction tasks
    layout.subscribe(top_left, freq_slider1.on_change) # Continuously changes while adjusting
    layout.subscribe(top_right, freq_slider2.on_after_change) # Only changes after adjustment
    layout.subscribe(middle_left, freq_number1.on_change)
    # Initialize the app on page load
    layout.load(initialize)
    # Build the app
    layout.build()