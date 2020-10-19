import React, {Component} from 'react';

import './App.css';
import Landing from './components/Landing';
import Appa from './components/image-upload/Appa'
// import { render } from 'react-dom';




class App extends Component {
  render() {
    return (
      // <Router>
        <div className="App">
          <Landing />
          <Appa />
        </div>
      // </Router>
    );
  }
}

export default App;
