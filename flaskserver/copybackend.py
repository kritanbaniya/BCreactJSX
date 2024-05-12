from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import pandas as pd
import plotly.express as px
import worldnewsapi
#import plotly.graph_objs as go


app = Flask(__name__)
CORS(app) ###, origins=['http://localhost:5173'])
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


def generate_plot(start_date, end_date, stockfile, stockname):
    # Read data from CSV file
    df = pd.read_csv(f'FlaskBknd/{stockfile}.csv')
    
    # Data preprocessing
    df = df.drop_duplicates()
    df = df.dropna()
    df['Date'] = pd.to_datetime(df['Date'])
    ##start_date = '2023-01-01'  # You can adjust this dynamically if needed
    ##end_date = '2023-01-30'    # You can adjust this dynamically if needed
    df_range = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    df_range['Date'] = df_range['Date'].dt.strftime('%Y-%m-%d')
    df_range['Average'] = (df_range['Open'] + df_range['High'] + df_range['Low']) / 3
    
    # Generate Plotly graph
    fig = px.line(df_range, x='Date', y='Average', title=f'{stockname} Average of Open, High, and Low for {start_date} to {end_date}')
    fig.update_xaxes(title_text='Date', tickangle=45, tickformat="%Y-%m-%d")
    fig.update_yaxes(title_text='Average in $')
    
    return fig

@app.route('/plot', methods=['POST'])
def plot():    # This is Nvidia
    # Handle POST request to generate plot
    # Retrieve start_date and end_date from request data
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    # Generate plot based on start_date and end_date
    # Return plot data as JSON response
    
    # Generate the Plotly graph
    fig = generate_plot(start_date, end_date, stockfile = 'NVDA99', stockname = 'NVDA')
    
    # Convert NumPy arrays to lists in the entire figure data
    fig_data_converted = convert_np_arrays_to_lists(fig.to_dict())

    # Return the Plotly graph data as JSON
    return jsonify(fig_data_converted)


@app.route('/plotA', methods=['POST'])
def plotA():   ####### this is Amazon
    # Handle POST request to generate plot
    # Retrieve start_date and end_date from request data
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    # Generate plot based on start_date and end_date
    # Return plot data as JSON response
    
    # Generate the Plotly graph
    fig = generate_plot(start_date, end_date, stockfile = 'AMZN2', stockname = 'AMZN')
    
    # Convert NumPy arrays to lists in the entire figure data
    fig_data_converted = convert_np_arrays_to_lists(fig.to_dict())

    # Return the Plotly graph data as JSON
    return jsonify(fig_data_converted)

@app.route('/plotB', methods=['POST'])
def plotB():           # This is Apple 
    # Handle POST request to generate plot
    # Retrieve start_date and end_date from request data
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    # Generate plot based on start_date and end_date
    # Return plot data as JSON response
    
    # Generate the Plotly graph
    fig = generate_plot(start_date, end_date, stockfile = 'AAPL', stockname = 'AAPL')
    
    # Convert NumPy arrays to lists in the entire figure data
    fig_data_converted = convert_np_arrays_to_lists(fig.to_dict())

    # Return the Plotly graph data as JSON
    return jsonify(fig_data_converted)

@app.route('/plotC', methods=['POST'])
def plotC():           # This is META
    # Handle POST request to generate plot
    # Retrieve start_date and end_date from request data
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    # Generate plot based on start_date and end_date
    # Return plot data as JSON response
    
    # Generate the Plotly graph
    fig = generate_plot(start_date, end_date, stockfile = 'META', stockname = 'META')
    
    # Convert NumPy arrays to lists in the entire figure data
    fig_data_converted = convert_np_arrays_to_lists(fig.to_dict())

    # Return the Plotly graph data as JSON
    return jsonify(fig_data_converted)

@app.route('/plotD', methods=['POST'])
def plotD():           # This is Netflix
    # Handle POST request to generate plot
    # Retrieve start_date and end_date from request data
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    # Generate plot based on start_date and end_date
    # Return plot data as JSON response
    
    # Generate the Plotly graph
    fig = generate_plot(start_date, end_date, stockfile = 'NFLX', stockname = 'NFLX')
    
    # Convert NumPy arrays to lists in the entire figure data
    fig_data_converted = convert_np_arrays_to_lists(fig.to_dict())

    # Return the Plotly graph data as JSON
    return jsonify(fig_data_converted)


@app.route('/api/nflx', methods=['POST'])
def get_newsnflx():
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')

    configuration = worldnewsapi.Configuration()    
    configuration.api_key['apiKey'] = 'd7c4014147b44248a1141e12a296a11f' 
    api_instance = worldnewsapi.NewsApi(worldnewsapi.ApiClient(configuration))

    try:
        sn_response = api_instance.search_news(text="Netflix Stock", 
                                                number=3,  # Increased number of news items
                                                source_countries="us", 
                                                earliest_publish_date=start_date, 
                                                latest_publish_date=end_date,
                                                sort="publish-time", 
                                                sort_direction="desc")
        news_data = [{'title': article.title, 'url': article.url} for article in sn_response.news]
        return jsonify(news_data)

    except worldnewsapi.ApiException as e:
        return jsonify({'error': str(e)}), 500

    
@app.route('/api/meta', methods=['POST'])
def get_newsmeta():
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')

    configuration = worldnewsapi.Configuration()    
    configuration.api_key['apiKey'] = 'd7c4014147b44248a1141e12a296a11f' 
    api_instance = worldnewsapi.NewsApi(worldnewsapi.ApiClient(configuration))

    try:
        sn_response = api_instance.search_news(text="Facebook META", 
                                                number=3,  # Increased number of news items
                                                source_countries="us", 
                                                earliest_publish_date=start_date, 
                                                latest_publish_date=end_date,
                                                sort="publish-time", 
                                                sort_direction="desc")
        news_data = [{'title': article.title, 'url': article.url} for article in sn_response.news]
        return jsonify(news_data)

    except worldnewsapi.ApiException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/nvda', methods=['POST'])
def get_newsnvda():
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')

    configuration = worldnewsapi.Configuration()    
    configuration.api_key['apiKey'] = 'd7c4014147b44248a1141e12a296a11f' 
    api_instance = worldnewsapi.NewsApi(worldnewsapi.ApiClient(configuration))

    try:
        sn_response = api_instance.search_news(text="Nvidia", 
                                                number=3,  # Increased number of news items
                                                source_countries="us", 
                                                earliest_publish_date=start_date, 
                                                latest_publish_date=end_date,
                                                sort="publish-time", 
                                                sort_direction="desc")
        news_data = [{'title': article.title, 'url': article.url} for article in sn_response.news]
        return jsonify(news_data)

    except worldnewsapi.ApiException as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/amzn', methods=['POST'])
def get_newsamzn():
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')

    configuration = worldnewsapi.Configuration()    
    configuration.api_key['apiKey'] = 'd7c4014147b44248a1141e12a296a11f' 
    api_instance = worldnewsapi.NewsApi(worldnewsapi.ApiClient(configuration))

    try:
        sn_response = api_instance.search_news(text="Amazon Stock", 
                                                number=3,  # Increased number of news items
                                                source_countries="us", 
                                                earliest_publish_date=start_date, 
                                                latest_publish_date=end_date,
                                                sort="publish-time", 
                                                sort_direction="desc")
        news_data = [{'title': article.title, 'url': article.url} for article in sn_response.news]
        return jsonify(news_data)

    except worldnewsapi.ApiException as e:
        return jsonify({'error': str(e)}), 500
    
    
@app.route('/api/aapl', methods=['POST'])
def get_newsaapl():
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')

    configuration = worldnewsapi.Configuration()    
    configuration.api_key['apiKey'] = 'd7c4014147b44248a1141e12a296a11f' 
    api_instance = worldnewsapi.NewsApi(worldnewsapi.ApiClient(configuration))

    try:
        sn_response = api_instance.search_news(text="Apple Stock", 
                                                number=3,  # Increased number of news items
                                                source_countries="us", 
                                                earliest_publish_date=start_date, 
                                                latest_publish_date=end_date,
                                                sort="publish-time", 
                                                sort_direction="desc")
        news_data = [{'title': article.title, 'url': article.url} for article in sn_response.news]
        return jsonify(news_data)

    except worldnewsapi.ApiException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)