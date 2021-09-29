# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from numpy import random
import plotly.express as px
import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import plotly.graph_objs as go

app = dash.Dash(__name__)

colors = {
    'text': '#7FDBFF'
}
logo = 'assets/logo.png'
gauge_size = "auto"

# see https://plotly.com/python/px-arguments/ for more options

N = 30
df = pd.DataFrame(dict(
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y = [0, np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N)]
))
fig1 = px.line(df, x="x", y="y", title="Input Power")
fig1.update_layout(xaxis_title="Time (s)",
                    yaxis_title="Power (Watts)")

Velocity_display = dbc.Card(
    children=[
        dbc.CardHeader(
            "Velocity [MPH]",
            style={
                "display": "flex",
                "text-align": "center",
                "color": "black",
                "border-radius": "1px",
                "border-width": "5px",
                "border-top": "1px solid rgb(121, 121, 121)",
            },
        ),
        dbc.CardBody(
            [
                html.Div(
                    daq.Gauge(
                        min=0,
                        max=120,
                        value=57,
                        units="MPH",
                        scale={'start': 0, 'interval': 15, 'labelInterval': 2},
                        size=300,
                        showCurrentValue=True,
                        color={"gradient":True,"ranges":{"green":[0,40],"yellow":[40,80],"red":[80,120]}},
                        style={
                            "align": "center",
                            "display": "inline-block",
                            "marginTop": "2%",
                            "marginBottom": "2%",
                        },
                    ),
                    style={
                        "display": "inline-block",
                        "border-radius": "1px",
                        "border-width": "5px",
                    },
                )
            ],
            style={
                "border-radius": "1px",
                "border-width": "5px",
                "border-top": "1px solid rgb(216, 216, 216)",
            },
        ),
    ],
    style={"height": "95%"},
)

Total_power_display = dbc.Card(
    children=[
        dbc.CardHeader(
            "Total Power [Watts]",
            style={
                "display": "flex",
                "text-align": "center",
                "color": "black",
                "border-radius": "1px",
                "border-width": "5px",
                "border-top": "1px solid rgb(121, 121, 121)",
            },
        ),
        dbc.CardBody(
            [
                html.Div(
                    daq.Gauge(
                        min=0,
                        max=60,
                        value=28,
                        units="Watts",
                        showCurrentValue=True,
                        color="#fead36",
                        style={
                            "align": "center",
                            "display": "flex",
                            "marginTop": "2%",
                            "marginBottom": "2%",
                        },
                    ),
                    style={
                        "display": "flex",
                        "border-radius": "1px",
                        "border-width": "5px",
                    },
                )
            ],
            style={
                "border-radius": "1px",
                "border-width": "5px",
                "border-top": "1px solid rgb(216, 216, 216)",
            },
        ),
    ],
    style={"height": "95%"},
)

Auxiliary_battery_display = dbc.Card(
    children=[
        dbc.CardHeader(
            "Auxiliary Battery []",
            style={
                "display": "flex",
                "text-align": "center",
                "color": "black",
                "border-radius": "1px",
                "border-width": "5px",
                "border-top": "1px solid rgb(121, 121, 121)",
            },
        ),
        dbc.CardBody(
            [
                html.Div(
                    daq.Gauge(
                        min=0,
                        max=60,
                        value=28,
                        units="Watts",
                        showCurrentValue=True,
                        color="#fead36",
                        style={
                            "align": "center",
                            "display": "flex",
                            "marginTop": "2%",
                            "marginBottom": "2%",
                        },
                    ),
                    style={
                        "display": "flex",
                        "border-radius": "1px",
                        "border-width": "5px",
                    },
                )
            ],
            style={
                "border-radius": "1px",
                "border-width": "5px",
                "border-top": "1px solid rgb(216, 216, 216)",
            },
        ),
    ],
    style={"height": "95%"},
)

Low_voltage_display = dbc.Card(
    children=[
        dbc.CardHeader(
            "Low Voltage [Volts]",
            style={
                "display": "flex",
                "text-align": "center",
                "color": "black",
                "border-radius": "1px",
                "border-width": "5px",
                "border-top": "1px solid rgb(121, 121, 121)",
            },
        ),
        dbc.CardBody(
            [
                html.Div(
                    daq.Gauge(
                        min=0,
                        max=60,
                        value=28,
                        units="Watts",
                        showCurrentValue=True,
                        color="#fead36",
                        style={
                            "align": "center",
                            "display": "flex",
                            "marginTop": "2%",
                            "marginBottom": "2%",
                        },
                    ),
                    style={
                        "display": "flex",
                        "border-radius": "1px",
                        "border-width": "5px",
                    },
                )
            ],
            style={
                "border-radius": "1px",
                "border-width": "5px",
                "border-top": "1px solid rgb(216, 216, 216)",
            },
        ),
    ],
    style={"height": "95%"},
)

Net_power_display = dbc.Card(
    children=[
        dbc.CardHeader(
            "Net Power [Watts]",
            style={
                "display": "flex",
                "text-align": "center",
                "color": "black",
                "border-radius": "1px",
                "border-width": "5px",
                "border-top": "1px solid rgb(121, 121, 121)",
            },
        ),
        dbc.CardBody(
            [
                html.Div(
                    daq.Gauge(
                        min=0,
                        max=60,
                        value=28,
                        units="Watts",
                        showCurrentValue=True,
                        color="#fead36",
                        style={
                            "align": "center",
                            "display": "flex",
                            "marginTop": "2%",
                            "marginBottom": "2%",
                        },
                    ),
                    style={
                        "display": "flex",
                        "border-radius": "1px",
                        "border-width": "5px",
                    },
                )
            ],
            style={
                "border-radius": "1px",
                "border-width": "5px",
                "border-top": "1px solid rgb(216, 216, 216)",
            },
        ),
    ],
    style={"height": "95%"},
)

app.layout = html.Div(children=[
    html.Img(
        src=logo
    ),
    html.H1(
        children='Solar Car Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(
        figure=fig1
    ),
    # dcc.Graph(
    #     figure=Output_power
    # ),
    # dcc.Graph(
    #     figure=Battery_voltage
    # ),
    dbc.Row([
        dbc.Col(Total_power_display,
            xs=gauge_size,
            md=gauge_size,
            lg=gauge_size,
            width=gauge_size),
        dbc.Col(Auxiliary_battery_display,
            xs=gauge_size,
            md=gauge_size,
            lg=gauge_size,
            width=gauge_size),
        dbc.Col(Velocity_display,
            xs=gauge_size,
            md=gauge_size,
            lg=gauge_size,
            width=gauge_size),
        dbc.Col(Low_voltage_display,
            xs=gauge_size,
            md=gauge_size,
            lg=gauge_size,
            width=gauge_size),
        dbc.Col(Net_power_display,
            xs=gauge_size,
            md=gauge_size,
            lg=gauge_size,
            width=gauge_size)
    ])
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
