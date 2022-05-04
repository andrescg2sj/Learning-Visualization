#
# Andrés González SJ
# https://github.com/andrescg2sj
#

import plotly.graph_objects as go


fig = go.Figure()


#These are the data that will be displayed
categories=["Coffee", "Tea", "Cereals", "Fruit", "Toasts", "Eggs"]
values =  [1, 2, 3, 4, 5, 6]
plus = [0.1, 0.2, 0.3,0.5, 1, 2]
minus = [0.4, 0.3, 0.2, 0.1, 0.2, 0.3]

#Create the graph
fig.add_trace(go.Scatter(
    name='Control',
    mode='markers', 
    x=categories, y=values,
    error_y=dict(type='data',
        symmetric=False,
        array=plus,
        arrayminus=minus)
        
    ))

#Configure main title and titles for axes
fig.update_layout(
    title="Breakfast preferences",
    title_font_size=20,
    xaxis_title="Type of breakfast",
    yaxis_title="Odds Ratio",
)

#Change axes' titles font size
fig.update_xaxes(title_font_size=16)
fig.update_yaxes(title_font_size=16)

# Reference dashed line over y=1
fig.add_hline(y=1, line_width=2, line_dash="dash", line_color="red")

#Draw black lines on axes
fig.update_xaxes(showline=True, linewidth=1, linecolor='black')
fig.update_yaxes(showline=True, linewidth=1, linecolor='black')


#background color
#fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')

#This should launch a browser and show the graph.
#(sometimes it doesn't work if the browser is not well configured...).
fig.show()

#This saves the graph to disk.
fig.write_html("example1_errorbars.htm")




