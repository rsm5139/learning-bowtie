#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bowtie.visual import Plotly, SmartGrid
from bowtie.control import Slider, Number, Button
from bowtie import cache, command, Pager
import numpy as np
import plotlywrapper as pw
import plotly.graph_objs as go

pager = Pager()

#
# Initialize our values
#
# This prevents an empty page from loading
#
def initialize():
    cache.save('scheduled',30)
    r1v1_listener(5)
    r1v2_listener(0.5)
    r2v1_listener(500)
    r2v2_listener(30)

#
# Scheduled function
#
def timed_event():
    ticker = cache.load('scheduled')
    ticker -= 1
    if ticker < 0:
        ticker = 0
    r2v2_listener(ticker)
    cache.save('scheduled',ticker)

def page_event():
    pager.notify()

#
# Reset Button
#
reset_button = Button(label='RESET')

#
# Row 1
#
r1v1 = Plotly()
r1v2 = Plotly()
r1v1_controller = Slider(caption='Row 1 - Left', minimum=1, maximum=10, start=5, step=1)
r1v2_controller = Slider(caption='Row 1 - Right', minimum=0.1, maximum=1, start=0.5, step=0.1)
def r1v1_listener(freq):
    freq = float(freq)
    t = np.linspace(0, 10, 100)
    r1v1.do_all(pw.line(t, np.sin(freq * t)).to_json())
def r1v2_listener(freq):
    freq = float(freq)
    t = np.linspace(0, 10, 100)
    r1v2.do_all(pw.line(t, np.sin(freq * t)).to_json())

#
# Row 2
#
r2v1 = Plotly()
r2v2 = Plotly()
r2v1_controller = Number(caption='Row 2 - Left', minimum=100, maximum=1000, start=500, step=100)
def r2v1_listener(n):
    random_x = np.random.randn(n)
    random_y = np.random.randn(n)
    trace = go.Scatter(
        x = random_x,
        y = random_y,
        mode = 'markers'
    )
    fig = { "data": [trace] }
    r2v1.do_all(fig)
def r2v2_listener(n):
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
    r2v2.do_all(fig)

#
# Row 3
#
r3v1 = SmartGrid()
r3v2 = SmartGrid()
def r3v1_listener(a,b,c):
    table_data = r3v1.get()
    table_data.append({"Control 1": a, "Control 2": b, "Control 3": c})
    r3v1.do_update(table_data)
def r3v2_listener(selected_data):
    r3v2.do_update(selected_data['points'])

#
# Bowtie section
#
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
    layout.schedule(1,page_event) # Edit server.py ->socketio.run(app, host=host, port=port, use_reloader=False)
    layout.respond(pager,timed_event)
    # Add controllers to the sidebar
    layout.add_sidebar(reset_button)
    layout.add_sidebar(r1v1_controller)
    layout.add_sidebar(r1v2_controller)
    layout.add_sidebar(r2v1_controller)
    # Add the visuals
    layout.add(r1v1,row_start=0,row_end=0,column_start=0,column_end=5)
    layout.add(r1v2,row_start=0,row_end=0,column_start=6,column_end=11)
    layout.add(r2v1,row_start=1,row_end=1,column_start=0,column_end=5)
    layout.add(r2v2,row_start=1,row_end=1,column_start=6,column_end=11)
    layout.add(r3v1,row_start=2,row_end=2,column_start=0,column_end=5)
    layout.add(r3v2,row_start=2,row_end=2,column_start=6,column_end=11)
    # Reaction tasks
    layout.subscribe(initialize, reset_button.on_click)
    layout.subscribe(r1v1_listener, r1v1_controller.on_change) # Continuously changes while adjusting
    layout.subscribe(r1v2_listener, r1v2_controller.on_after_change) # Only changes after adjustment
    layout.subscribe(r2v1_listener, r2v1_controller.on_change)
    layout.subscribe(r3v1_listener, r1v1_controller.on_after_change, r1v2_controller.on_after_change, r2v1_controller.on_change)
    layout.subscribe(r3v2_listener, r2v1.on_select)
    # Initialize the app on page load
    layout.load(initialize)
    # Build the app
    layout.build()