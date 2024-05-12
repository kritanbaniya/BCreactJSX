import React, { useState } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';

function DateRangePicker() {
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [plotData, setPlotData] = useState(null);
  const [newsData, setNewsData] = useState([]); // Added newsData state

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // Fetch plot data
      const plotResponse = await axios.post('http://localhost:5000/plot', { start_date: startDate, end_date: endDate });
      setPlotData(plotResponse.data);

      // Fetch news data
      const newsResponse = await axios.post('http://localhost:5000/api/nvda', { start_date: startDate, end_date: endDate });
      setNewsData(newsResponse.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };


  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Start Date:
          <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)}min="2000-01-01" max="2023-12-31" />
        </label>
        <label>
          End Date:
          <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} min="2000-01-01" max="2023-12-31" />
        </label>
        <button type="submit">Generate Plot</button>
      </form>
      {plotData && <Plot data={plotData.data} layout={plotData.layout} />}
      {newsData && (
        <div>
          <h2>News Data</h2>
          <ul>
            {newsData.map((item, index) => (
              <li key={index}>
                <a href={item.url} target="_blank" rel="noopener noreferrer">{item.title}</a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default DateRangePicker;