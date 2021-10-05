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

app = dash.Dash(
    __name__,
    external_stylesheets = [dbc.themes.BOOTSTRAP]
)

colors = {
    'text': '#000'
}
logo = 'assets/logo.png'
gauge_size = "auto"

# see https://plotly.com/python/px-arguments/ for more options

N = 30
df1 = pd.DataFrame(dict(
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y = [0, np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N)]
))
df2 = pd.DataFrame(dict(
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y = [0, np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N)]
))
df3 = pd.DataFrame(dict(
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    y = [0, np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N), np.random.randint(0, N)]
))
fig1 = px.line(df1, x="x", y="y", title="Input Power", width=500, height=400)
fig1.update_layout(xaxis_title="Time (s)",
                    yaxis_title="Power (Watts)",
                    title_x=0.5)
fig2 = px.line(df2, x="x", y="y", title="Output Power", width=500, height=400)
fig2.update_layout(xaxis_title="Time (s)",
                    yaxis_title="Power (Watts)",
                    title_x=0.5)
fig3 = px.line(df3, x="x", y="y", title="Battery Voltage", width=500, height=400)
fig3.update_layout(xaxis_title="Time (s)",
                    yaxis_title="Voltage (Volts)",
                    title_x=0.5)

Total_power_display = html.Div(
    children=[
        html.Div(
            "Total Power [Watts]",
            style={
                "text-align": "center",
                "color": "black"
            },
        ),
        html.Div(
            daq.Gauge(
                min=0,
                max=60,
                value=28,
                units="Watts",
                size=200,
                showCurrentValue=True,
                color="#fead36",
                style={
                    "align": "center",
                    "marginTop": "2%",
                    "display": "flex"
                }
            )
        )     
    ]
)

Auxiliary_battery_display = html.Div(
    children=[
        html.Div(
            "Auxiliary Battery [Watts]",
            style={
                "text-align": "center",
                "color": "black"
            }
        ),
        
                html.Div(
                    daq.Gauge(
                        min=0,
                        max=60,
                        value=28,
                        units="Watts",
                        size=200,
                        showCurrentValue=True,
                        color="#fead36",
                        style={
                            "align": "center",
                            "marginTop": "2%",
                            "display": "flex"
                        }
                    )
               
        )
    ], style={
        "color": "black"
    }
)

Velocity_display = html.Div(
    children=[
        html.Div(
            "Velocity [MPH]",
            style={
                "text-align": "center",
                "color": "black"
            },
        ),
                html.Div(
                    daq.Gauge(
                        min=0,
                        max=120,
                        value=57,
                        units="MPH",
                        scale={'start': 0, 'interval': 15, 'labelInterval': 2},
                        size=200,
                        showCurrentValue=True,
                        color={"gradient":True,"ranges":{"green":[0,40],"yellow":[40,80],"red":[80,120]}},
                        style={
                            "align": "center",
                            "marginTop": "2%",
                            "display": "flex"
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
                "text-align": "center",
                "color": "black"
            }
        ),
                html.Div(
                    daq.Gauge(
                        min=0,
                        max=60,
                        value=28,
                        units="Volts",
                        size=200,
                        showCurrentValue=True,
                        color="#fead36",
                        style={
                            "align": "center",
                            "display": "flex",
                            "marginTop": "2%"
                        }
                    )
                )
    ]
)

Net_power_display = html.Div(
    children=[
        html.Div(
            "Net Power [Watts]",
            style={
                "text-align": "center",
                "color": "black"
            }
        ),

                html.Div(
                    daq.Gauge(
                        min=-100,
                        max=100,
                        value=0,
                        units="Watts",
                        size=200,
                        showCurrentValue=True,
                        color="#fead36",
                        style={
                            "align": "center",
                            "display": "flex",
                            "marginTop": "2%"
                        }
                    )
                )
    ]
)

app.layout = html.Div(
    className="background",
    children=[
    dbc.Row([
        html.Img(
            src=logo,
            alt="Logo",
            width=250,
            height=100
        ),
        html.H1(
            children='Solar Car Dashboard',
            style={
                'color': colors['text'],
                'marginLeft': '300px',
                'marginTop': '25px'
            }
        )
    ]),
    
    # dbc.Row([
    #     dcc.Graph(
    #     figure=fig1,
    #     ),
    #     dcc.Graph(
    #         figure=fig2
    #     ),
    #     dcc.Graph(
    #         figure=fig3
    #     )
    # ]),

    dbc.Row([
        dbc.Col([
            dbc.Row(Total_power_display),
            dbc.Row(Auxiliary_battery_display)
        ]),
        dbc.Col(
            dbc.Row(Velocity_display), align='center'
        ),
        dbc.Col([
            dbc.Row(Low_voltage_display),
            dbc.Row(Net_power_display)
        ]),
        dbc.Col([
            dbc.Row([
                daq.LEDDisplay(
                    label = 'Codes',
                    value = '00',
                    size = 80,
                    color="red"
                )
            ])
        ], align='center')
    ], style={
        'margin': 50
    },no_gutters=True)

])

if __name__ == '__main__':
    app.run_server(debug=True)
