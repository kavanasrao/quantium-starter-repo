from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv("output_data.csv")
df = df.sort_values(by="date")

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    
    html.H1(
        "Pink Morsel Sales Analysis",
        style={"textAlign": "center"}
    ),

    html.Div([
        html.Label("Select Region:"),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True
        ),
    ], style={"textAlign": "center", "marginBottom": "20px"}),

    dcc.Graph(id="sales-chart")
])

# Callback to update chart
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        labels={"date": "Date", "sales": "Sales"},
        title="Pink Morsel Sales Over Time"
    )

    return fig


# Run server
if __name__ == "__main__":
    app.run(debug=True)