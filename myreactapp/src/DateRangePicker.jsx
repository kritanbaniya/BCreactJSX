import React, { useState } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';

function DateRangePicker() {
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [plotData, setPlotData] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/plot', { start_date: startDate, end_date: endDate });
      setPlotData(response.data);
    } catch (error) {
      console.error('Error fetching plot data:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Start Date:
          <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
        </label>
        <label>
          End Date:
          <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
        </label>
        <button type="submit">Generate Plot</button>
      </form>
      {plotData && <Plot data={plotData.data} layout={plotData.layout} />}
    </div>
  );
}

export default DateRangePicker;
