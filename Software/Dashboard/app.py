#http://127.0.0.1:8050/

import dash
import dash_html_components as html
import dash_core_components as dcc



app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        options=[
            {'label': 'Home', 'value': 'HOME'},
            {'label': 'Battery', 'value': 'BAT'},
            {'label': 'Motor', 'value': 'MOT'},
            {'label': 'Array', 'value': 'ARR'},
        ],
        value='HOME'
    ),
    html.Div(id='temetryMenu')
])



@app.callback(
    dash.dependencies.Output(component_id= 'telemetryMenu', component_property = 'children'),
    [dash.dependencies.Input('telemetryMenu', 'value')])
def update_output(value):
    return 0

if __name__ == '__main__':
    app.run_server(debug=True)

