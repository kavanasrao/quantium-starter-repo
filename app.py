from dash import Dash, html, dcc
import plotly.express  as px
import pandas as pd


df = pd.read_csv('output_data.csv')
df=df.sort_values(by='date')

fig = px.line(df, x='date', y='sales', color='region')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)