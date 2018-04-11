import React, { Component } from 'react';
import { Link } from 'react-router-dom'

import { connect } from 'react-redux';

class Aminia extends Component {
  render() {
    return (
      <div>
        <h2>Welcome to Aminia</h2>
        <p>Tell us what you like. Naskia kuzitoka!!</p>
        <p>
          <Link to="/contact">Click Here</Link> to contact us.
        </p>
        <h3>Posts</h3>
        <table>
          <tbody>
            {this.props.posts.map(post => (
              <tr>
                <td>{post.text}</td>
                <td><button>edit</button></td>
                <td><button>delete</button></td>
              </tr>
            ))}
          </tbody>
          </table>
      </div>
    )
  }
}

const mapStateToProps = state => {
  return {
    posts:state.posts,
  }
}
const mapDispatchToProps = dispatch => {
  return {

  }
}

export default connect(mapStateToProps,mapDispatchToProps)(Aminia);
