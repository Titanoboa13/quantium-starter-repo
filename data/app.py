from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Veriyi oku ve tarihe göre sırala
df = pd.read_csv('formatted_data.csv')
df = df.sort_values(by="date")

# Sayfa Düzeni (Layout)
app.layout = html.Div(style={'fontFamily': 'sans-serif', 'padding': '20px'}, children=[
    html.H1(
        children='Pink Morsel Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),

    # Radyo Butonları (Bölge Seçimi)
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
            value='all',  # Başlangıç değeri
            inline=True,
            style={'marginLeft': '10px'}
        ),
    ]),

    # Grafik Alanı
    dcc.Graph(id='sales-line-chart')
])


# Etkileşim (Callback) Mekanizması
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # Veriyi filtrele
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Grafiği oluştur
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.upper()}"
    )

    # Grafik tasarımı (estetik dokunuş)
    fig.update_layout(
        transition_duration=500,
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9'
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)

