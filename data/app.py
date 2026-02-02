from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import os # 1. Bu kütüphaneyi ekledik

app = Dash(__name__)

# 2. Dosya yolunu dinamik hale getirdik
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'formatted_data.csv')

df = pd.read_csv(file_path)
df = df.sort_values(by="date")

app.layout = html.Div(style={'fontFamily': 'sans-serif', 'padding': '20px'}, children=[
    html.H1(
        id='header', # Testin kolay bulması için bir ID ekleyebilirsin (Opsiyonel)
        children='Pink Morsel Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),

    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("Select Region: ", style={'fontWeight': 'bold'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            inline=True,
            style={'marginLeft': '10px'}
        ),
    ]),

    dcc.Graph(id='sales-line-chart')
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.upper()}"
    )

    fig.update_layout(
        transition_duration=500,
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9'
    )

    return fig

if __name__ == '__main__':
    # debug=True kalsın, geliştirme yaparken lazım olur
    app.run(debug=True)