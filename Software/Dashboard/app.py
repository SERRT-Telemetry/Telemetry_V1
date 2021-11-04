# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash_bootstrap_components import themes
from matplotlib.pyplot import margins, title
from numpy import random
import plotly.express as px
import pandas as pd
import numpy as np
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

app = dash.Dash(
    __name__,
    external_stylesheets = [dbc.themes.YETI]
)

logo = 'assets/solarcarlogo.png'

N = 30
# df1 = pd.DataFrame(dict(
#     x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     y = [0, np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N)]
# ))
# df2 = pd.DataFrame(dict(
#     x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     y = [0, np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N)]
# ))
# df3 = pd.DataFrame(dict(
#     x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     y = [0, np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N)]
# ))
# fig1 = px.line(df1, x="x", y="y", title="Input Power", width=500, height=400)
# fig1.update_layout(xaxis_title="Time (s)",
#                     yaxis_title="Power (Watts)",
#                     title_x=0.5)
# fig2 = px.line(df2, x="x", y="y", title="Output Power", width=500, height=400)
# fig2.update_layout(xaxis_title="Time (s)",
#                     yaxis_title="Power (Watts)",
#                     title_x=0.5)
# fig3 = px.line(df3, x="x", y="y", title="Battery Voltage", width=500, height=400)
# fig3.update_layout(xaxis_title="Time (s)",
#                     yaxis_title="Voltage (Volts)",
#                     title_x=0.5)

Total_power_display = html.Div(
    children=[
        html.Div(
            "Total Power [KiloWatts]",
            style={
                "text-align": "center"
            },
        ),
        html.Div(
            daq.Gauge(
                min=0,
                max=2,
                value=0.57,
                units="kW",
                size=240,
                showCurrentValue=True,
                style={
                    "align": "center",
                    "marginTop": "2%",
                    "display": "flex",
                    "paddingRight": "-25px"
                }
            )
        )     
    ]
)

Auxiliary_battery_display = html.Div(
    children=[
        html.Div(
            "Auxiliary Battery [Volts]",
            style={
                "text-align": "center"
            }
        ),    
        html.Div(
            daq.Gauge(
                min=0,
                max=15,
                value=6.8,
                units="Volts",
                size=240,
                showCurrentValue=True,
                style={
                    "align": "center",
                    "marginTop": "2%",
                    "display": "flex",
                    "paddingRight": "-25px"
                }
            )
        )
    ]
)

Velocity_display = html.Div(
    children=[
        html.Div(
            "Velocity [km/h]",
            style={
                "text-align": "center"
            },
        ),
        html.Div(
            daq.Gauge(
                min=0,
                max=60,
                value=43,
                units="km/h",
                scale={'start': 0, 'interval': 15, 'labelInterval': 1},
                size=240,
                showCurrentValue=True,
                color={"gradient":True,"ranges":{"green":[0,20],"yellow":[20,40],"red":[40,60]}},
                style={
                    "align": "center",
                    "marginTop": "2%",
                    "display": "flex",
                    "paddingRight": "-25px"
                }
            )
        )
    ]
)

Low_voltage_display = html.Div(
    children=[
        html.Div(
            "Low Voltage [Volts]",
            style={
                "text-align": "center"
            }
        ),
        html.Div(
            daq.Gauge(
                min=0,
                max=15,
                value=5.89,
                units="Volts",
                size=240,
                showCurrentValue=True,
                style={
                    "align": "center",
                    "display": "flex",
                    "marginTop": "2%",
                    "paddingRight": "-25px"
                }
            )
        )
    ]
)

Net_power_display = html.Div(
    children=[
        html.Div(
            "Net Power [KiloWatts]",
            style={
                "text-align": "center"
            }
        ),

        html.Div(
            daq.Gauge(
                max=2,
                min=-2,
                value=0,
                units="kW",
                size=240,
                showCurrentValue=True,
                color="whitesmoke",
                style={
                    "align": "center",
                    "display": "flex",
                    "marginTop": "2%",
                    "paddingRight": "-25px"
                }
            )
        )
    ]
)

app.layout = html.Div(
    children=[
    
    html.Center(
            children='Solar Car Dashboard',
            style= {
                'paddingTop': '25px',
                'fontSize': '50px'
            }
    ),
    
    html.Img(
        src=logo,
        alt="Logo", 
        width=250,
        height=225,
        className=logo, 
        style= {
            'marginLeft': '25px',
            'marginTop': '-140px'
        }     
    ),

    html.Div(className="grid-container",
    children=[

        html.Div(className="row1",
        children=[
            dbc.Col([
                dbc.Row(Total_power_display),
                dbc.Row(Auxiliary_battery_display)
            ], className="gauge")
        ]),

        html.Div(className="row2",
        children=[
            dbc.Col(
                dbc.Row(Velocity_display), align='center', className="gauge"
            )
        ]),

        html.Div(className="row1",
        children=[
            dbc.Col([
                dbc.Row(Total_power_display),
                dbc.Row(Auxiliary_battery_display)
            ], className="gauge")
        ]),

        html.Div(className="row1",
        children=[
            dbc.Col([
            dbc.Row([
                daq.LEDDisplay(
                    label = 'BMS Fault Codes',
                    value = '00',
                    size = 80
                )
            ], className="BMScodes"),
            dbc.Row([
            html.Div([
                dcc.Dropdown(
                    id="dropdown",
                    options=[
                        {"label": "Input Power", "value": 1},
                        {"label": "Output Power", "value": 2},
                        {"label": "Battery Voltage", "value": 3}],
                        value=1),
                dcc.Graph(id='graph-court')
            ],
            style={
                "width": "100%",
            })
        ])
        ])
        ])
    ])
])

def create_graph(value):
    if value == 1:
        df = pd.DataFrame(dict(
            x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            y = [0, 17, 25, 4, 29, 2, 16, 12, 14, 10, 15]))
    elif value == 2:
        df = pd.DataFrame(dict(
            x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            y = [0, 22, 19, 18, 8, 22, 16, 19, 29, 24, 13]))
    else:
        df = pd.DataFrame(dict(
            x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            y = [0, 7, 19, 11, 25, 13, 10, 4, 1, 14, 20]))
   
    fig = px.line(df, x="x", y="y", height=500)

    return fig

@app.callback(Output('graph-court', 'figure'), 
              [Input('dropdown', 'value')])

def update_figure(selected_value):
    if selected_value == 1:
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        y = [0, 17, 25, 4, 29, 2, 16, 12, 14, 10]
    elif selected_value == 2:
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        y = [0, 22, 19, 18, 8, 22, 16, 19, 29, 24]
    else:
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        y = [0, 7, 19, 11, 25, 13, 10, 4, 1, 14]

    fig = create_graph(selected_value)

    if selected_value == 1:
        fig.update_layout(xaxis_title="Time (s)",
                    yaxis_title="Power (Watts)",
                    title="Input Power",
                    title_x=0.5)
    elif selected_value == 2:
        fig.update_layout(xaxis_title="Time (s)",
                    yaxis_title="Power (Watts)",
                    title="Output Power",
                    title_x=0.5)
    else:
        fig.update_layout(xaxis_title="Time (s)",
                    yaxis_title="Voltage (Volts)",
                    title="Battery Voltage",
                    title_x=0.5)

    return fig
        

if __name__ == '__main__':
    app.run_server(debug=True)
