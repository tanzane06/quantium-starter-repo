# Import the necessary libraries
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# 1. LOAD AND PREPARE THE DATA
# Load the data you formatted in the previous task
df = pd.read_csv('formatted_sales.csv')

# Convert the 'date' column to a proper datetime format
df['date'] = pd.to_datetime(df['date'])

# The data is per-region, so we need to sum up the sales for each day
# to get the total daily sales.
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Sort the data by date to ensure the line chart is plotted correctly
daily_sales = daily_sales.sort_values(by='date')

# 2. CREATE THE VISUALIZATION
# Use Plotly Express to create a line chart
fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Pink Morsel Sales Over Time',
    labels={
        'date': 'Date',
        'sales': 'Total Sales ($)'
    }
)

# 3. INITIALIZE THE DASH APP
# Create an instance of the Dash class
app = Dash(__name__)
server = app.server

# 4. DEFINE THE APP LAYOUT
# This describes what the web application will look like
app.layout = html.Div(children=[
    # A main header for the dashboard
    html.H1(
        children='Soul Foods: Pink Morsel Sales Analysis',
        style={'textAlign': 'center'}
    ),

    # A descriptive paragraph
    html.Div(
        children='Visualizing daily sales data to understand the impact of the Jan 15, 2021 price increase.',
        style={'textAlign': 'center'}
    ),

    # The line chart component
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 5. RUN THE APP
# This is the standard code to run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
