# Import the necessary libraries
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# --- 1. PREPARE THE DATA ---
# Load the data you formatted in the previous task
df = pd.read_csv('formatted_sales.csv')

# Convert the 'date' column to a proper datetime format for plotting
df['date'] = pd.to_datetime(df['date'])
# Sort the DataFrame by date initially
df = df.sort_values(by='date')

# --- 2. INITIALIZE THE DASH APP ---
# Use a modern, dark theme for the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# --- 3. DEFINE THE APP LAYOUT ---
# This describes what the web application will look like
app.layout = html.Div(style={'backgroundColor': '#111111', 'color': '#7FDBFF', 'fontFamily': 'sans-serif'}, children=[
    
    # Main header for the dashboard
    html.H1(
        children='Soul Foods: Pink Morsel Sales Analysis',
        style={'textAlign': 'center', 'padding': '20px'}
    ),

    # Container for the radio buttons
    html.Div([
        html.Label('Select a Region:', style={'paddingRight': '10px'}),
        dcc.RadioItems(
            id='region-radio-buttons',
            options=[
                {'label': 'All Regions', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',  # Default value
            labelStyle={'display': 'inline-block', 'marginRight': '15px'},
            inputStyle={"margin-right": "5px"}
        )
    ], style={'textAlign': 'center', 'padding': '10px'}),

    # The line chart component will be updated by the callback
    dcc.Graph(id='sales-line-chart')
])

# --- 4. DEFINE THE CALLBACK ---
# This connects the radio buttons to the line chart
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio-buttons', 'value')
)
def update_chart(selected_region):
    # Filter the DataFrame based on the selected region
    if selected_region == 'all':
        filtered_df = df
        title = 'Total Pink Morsel Sales Over Time (All Regions)'
    else:
        filtered_df = df[df['region'] == selected_region]
        title = f'Pink Morsel Sales Over Time ({selected_region.capitalize()})'

    # The data is per-region, so we need to sum up the sales for each day
    # to get the total daily sales for the selected region(s).
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()

    # Create the line chart with the filtered data
    fig = px.line(
        daily_sales,
        x='date',
        y='sales',
        title=title,
        labels={
            'date': 'Date',
            'sales': 'Total Sales ($)'
        }
    )

    # Update the layout of the figure for the dark theme
    fig.update_layout(
        plot_bgcolor='#111111',
        paper_bgcolor='#111111',
        font_color='#7FDBFF'
    )

    return fig

# --- 5. RUN THE APP ---
if __name__ == '__main__':
    app.run(debug=True)