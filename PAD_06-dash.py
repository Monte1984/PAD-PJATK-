from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('winequelity.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__)

app.layout = html.Div([
    html.H3(children='WINE QUALITY'),
    generate_table(df),

    html.Div(children=[
        html.Br(),
        html.Label('Wybierz model:'),
        dcc.RadioItems(['Model regresji', 'Model klasyfikacji'], 'Model regresji'),
    ], style={'padding': 10, 'flex': 1}),
], style={'padding': 10, 'flex': 1})


if __name__ == '__main__':
    app.run_server(debug=True)