import React, { Component } from 'react';
import './App.css';
import Landing from './Landing.js';
import MultipleImageUploadComponent from './multiple-image-upload.js';
import PredictionLabel from './PredictionLabel.js';
// import { render } from 'react-dom';
// import Buttons from './components/Buttons'

class App extends Component {
  render() {
    return (
      <div className="App">
        <Landing />
        <PredictionLabel />
        <MultipleImageUploadComponent />
        {/* <Buttons /> */}
      </div>
    );
  }
}

export default App;
