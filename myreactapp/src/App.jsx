import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';
import DateRangePicker from './DateRangePicker'; // Import the DateRangePicker component

function App() {
  const [plotData, setPlotData] = useState(null);
  const [error, setError] = useState(null);

  // useEffect hook to fetch plot data initially
  useEffect(() => {
    fetchData();
  }, []); // Empty dependency array to run only once on component mount

  // Function to fetch plot data from the Flask backend
  const fetchData = async (startDate, endDate) => {
    try {
      // Adjust the Axios request URL to point to the Flask backend
      const response = await axios.post('http://localhost:5000/plot', { start_date: startDate, end_date: endDate });
      setPlotData(response.data);
    } catch (error) {
      setError(error.message);
    }
  };

  // Render the DateRangePicker and Plot components
  return (
    <div className="App">
      <DateRangePicker fetchData={fetchData} /> {/* Pass fetchData function as prop */}
      {error && <div>Error: {error}</div>}
      {plotData && <Plot data={plotData.data} layout={plotData.layout} />}
    </div>
  );
}

export default App;
