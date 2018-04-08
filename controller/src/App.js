import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

class App extends Component {

  constructor(props) {
    super(props);
  }

  direction = (number) => {
    axios.post('api/direction', { number });
  }

  spotlight = () => {
    axios.post('api/spotlight', { });
  }
  render() {
    return (
      <div className="App">
        <div className="container">
          <div className="row">
            <a className="waves-effect waves-light grey lighten-1 btn" onClick={() => this.direction(1)}>Left</a>
            <a className="waves-effect waves-light grey lighten-1 btn" onClick={() => this.direction(2)}>Forward</a>
            <a className="waves-effect waves-light grey lighten-1 btn" onClick={() => this.direction(3)}>Right</a>
            <a className="waves-effect waves-light grey lighten-1 btn" onClick={() => this.direction(4)}>Back</a>
          </div>
          <div className="divider"></div>
          <div className="row">
            <a className="waves-effect waves-light green lighten-1 btn" onClick={this.spotlight}>Spotlight</a>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
