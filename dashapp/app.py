import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Ronaldo vs Messi - who is better'),

    html.Div(children='''
        Goals scored vs season
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ['2016/2017','2017/2018', '2018/2019'], 'y': [42, 44, 28], 'type': 'bar', 'name': 'Ronaldo'},
                {'x': ['2016/2017','2017/2018', '2018/2019'], 'y': [59, 45, 51], 'type': 'bar', 'name': u'Messi'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)