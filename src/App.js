import React, { Component } from 'react';
import { Route, Switch, BrowserRouter } from 'react-router-dom';
import Aminia from "./components/Aminia";
import NotFound from "./components/NotFound";

// import logo from './logo.svg';
import './App.css';

import { Provider } from "react-redux";
import { createStore } from "redux";
import aminiaApp from "./reducers";

let store = createStore(aminiaApp)

class App extends Component {
  render() {
    return (
    <Provider store={store}>
      <BrowserRouter>
        <Switch>
        <Route exact path="/" component ={Aminia} />
        <Route component={NotFound} />
        </Switch>
      </BrowserRouter>
    </Provider>
    );
  }
}

export default App;
