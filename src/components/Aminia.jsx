import React, { Component } from 'react';
import { Link } from 'react-router-dom'

export default class Aminia extends Component {
  render() {
    return (
      <div>
        <h2>Welcome to Aminia</h2>
        <p>Tell us what you like. Naskia kuzitoka!!</p>
        <p>
          <Link to="/contact">Click Here</Link> to contact us.
        </p>
      </div>
    )
  }
}
