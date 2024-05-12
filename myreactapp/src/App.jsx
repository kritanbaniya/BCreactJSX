import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';
import Home from './Home';
import VerticalNav from './VerticalNav'; // Importing VerticalNav component
import AmazonComponent from './AmazonComponent';
import NvidiaComponent from './NvidiaComponent';
import MetaComponent from './MetaComponent';
import NetflixComponent from './NetflixComponent';
import AppleComponent from './AppleComponent';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedCompany: null
    };
  }

  handleCompanyChange = (company) => {
    this.setState({ selectedCompany: company });
  };

  render() {
    const { selectedCompany } = this.state;
    return (
      <div>
        <VerticalNav /> {/* Rendering VerticalNav component */}
        <Home />
        <div>
          <h2>Companies Stock</h2>
          <select onChange={(e) => this.handleCompanyChange(e.target.value)}>
            <option value="">Select a company</option>
            <option value="Amazon">Amazon</option>
            <option value="Nvidia">Nvidia</option>
            <option value="Meta">Meta</option>
            <option value="Netflix">Netflix</option>
            <option value="Apple">Apple</option>
          </select>
          {selectedCompany && (
            <>
              {selectedCompany === 'Amazon' && <AmazonComponent />}
              {selectedCompany === 'Nvidia' && <NvidiaComponent />}
              {selectedCompany === 'Meta' && <MetaComponent />}
              {selectedCompany === 'Netflix' && <NetflixComponent />}
              {selectedCompany === 'Apple' && <AppleComponent />}
            </>
          )}
        </div>
      </div>
    );
  }
}

export default App;

