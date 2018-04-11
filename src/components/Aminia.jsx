import React, { Component } from 'react';
import { Link } from 'react-router-dom'

import { connect } from 'react-redux';

import { posts } from "../actions";

class Aminia extends Component {

  state = {
    text: "",
    updatePostId: null,
  }

  resetForm = () => {
    this.setState({text:"", updatePostId:null});
  }

  selectForEdit = (id) => {
    let post = this.props.posts[id];
    this.setState({text: post.text, updatePostId:id});
  }

  submitPost = (event) => {
    event.preventDefault();
    if (this.state.updatePostId === null){
      this.props.addPosts(this.state.text);
    } else {
      this.props.updatePost(this.state.updatePostId, this.state.text)
    }
    this.resetForm();
  }


  render() {
    return (
      <div>
        <h2>Welcome to Aminia</h2>
        <hr/>

        <p>Naskia kuzitoka!!</p>
          <form onSubmit={this.submitPost}>
            <input
              value={this.state.text}
              placeholder="Enter post here..."
              onChange = {(event)=> this.setState({text:event.target.value})}
              required
            />
            <button onClick={this.resetForm}>Reset</button>
            <input type="submit" value="Save Post"/>
          </form>


        <p>
          <Link to="/contact">Click Here</Link> to contact us.
        </p>
        <h3>Posts</h3>
        <table>
          <tbody>
            {this.props.posts.map((post, id) => (
              <tr key={`post_${post.id}`}>
                <td>{post.text}</td>
                <td>
                  <button onClick={() => this.props.selectForEdit(id)}>
                    edit
                  </button>
                </td>
                <td>
                  <button onClick={() => this.props.deletePost(id)}>
                    delete
                  </button>
                </td>
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
/*
We use the actions we defined in actions/posts.js in our
Aminia component by its properties in mapDispatchToProp
function.

We update the mapDispatchToProp function to use all the actions.
*/

const mapDispatchToProps = dispatch => {
  return {
    addPosts: (text) => {
      dispatch(posts.addPosts(text))
    },
    updatePost: (id, text) => {
      dispatch(posts.addPosts(id, text))
    },
    deletePost: (id) => {
      dispatch(posts.deletePost(id))
    },
  }
}

export default connect(mapStateToProps,mapDispatchToProps)(Aminia);
