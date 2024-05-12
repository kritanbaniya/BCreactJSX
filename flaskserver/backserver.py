from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import pandas as pd
import plotly.express as px
#import plotly.graph_objs as go


app = Flask(__name__)
CORS(app) ##, origins=['http://localhost:5173'])
  # Add this line to enable CORS for all routes

def convert_np_arrays_to_lists(data):
    if isinstance(data, dict):
        return {key: convert_np_arrays_to_lists(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_np_arrays_to_lists(item) for item in data]
    elif isinstance(data, np.ndarray):
        return data.tolist()
    else:
        return data


def generate_plot(start_date, end_date, stockfile):
    # Read data from CSV file
    df = pd.read_csv(f'flaskserver/{stockfile}.csv')
    
    # Data preprocessing
    df = df.drop_duplicates()
    df = df.dropna()
    df['Date'] = pd.to_datetime(df['Date'])
    ##start_date = '2020-01-01'  # You can adjust this dynamically if needed
    ##end_date = '2021-01-01'    # You can adjust this dynamically if needed
    df_range = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_range['Date'] = df_range['Date'].dt.strftime('%Y-%m-%d')
    df_range['Average'] = (df_range['Open'] + df_range['High'] + df_range['Low']) / 3
    
    # Generate Plotly graph
    fig = px.line(df_range, x='Date', y='Average', title=f'NVDA Average of Open, High, and Low for {start_date} to {end_date}')
    fig.update_xaxes(title_text='Date', tickangle=45, tickformat="%Y-%m-%d")
    fig.update_yaxes(title_text='Average in $')
    
    return fig

@app.route('/plot', methods=['POST'])
def plot():
    # Handle POST request to generate plot
    # Retrieve start_date and end_date from request data
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    # Generate plot based on start_date and end_date
    # Return plot data as JSON response
    
    # Generate the Plotly graph
    fig = generate_plot(start_date, end_date, stockfile = 'NVDA99')
    
    # Convert NumPy arrays to lists in the entire figure data
    fig_data_converted = convert_np_arrays_to_lists(fig.to_dict())

    # Return the Plotly graph data as JSON
    return jsonify(fig_data_converted)





if __name__ == '__main__':
    app.run(debug=True)



