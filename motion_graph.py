from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from motion_detector import df



df['Start_time'] = df['Start'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['End_time'] = df['End'].dt.strftime('%Y-%m-%d %H:%M:%S')

cds = ColumnDataSource(df)

p = figure(x_axis_type = 'datetime', height=100, width=500, sizing_mode='scale_width', title='Motion Graph')

hover=HoverTool(tooltips=[('Start','@Start_time'),('End','@End_time')])
p.add_tools(hover)

p.title.text_font_size='20pt'
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

q=p.quad(left='Start', right='End', bottom=0, top=1, color='green', source=cds)

output_file('Motion_Graph.html')
show(p)