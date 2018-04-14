import React, { Component } from 'react';
import { Route, Switch, BrowserRouter } from 'react-router-dom';
import Aminia from "./components/Aminia";
import NotFound from "./components/NotFound";

// import logo from './logo.svg';
import './App.css';

import { Provider } from "react-redux";

import { createStore, applyMiddleware } from "redux";

/*
Redux Thunk middleware allows us to write action creators that return a function instead of an action.

The thunk can be used to delay the dispatch of an action, or to dispatch only if a certain condition is met.

The inner function recieves the store methods dispatch and getState as parameters.
*/
import thunk from "redux-thunk";

import aminiaApp from "./reducers";

let store = createStore(aminiaApp, applyMiddleware(thunk));

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
