import React, { Component } from 'react';
import { Link } from 'react-router-dom'

import { connect } from 'react-redux';

import { posts } from "../actions";

import 'bootstrap/dist/css/bootstrap.min.css';
import 'jquery/dist/jquery.min.js';
import 'popper.js/dist/umd/popper.min.js';
import 'bootstrap/dist/js/bootstrap.min.js';
import {
  Button, FormGroup, Form, Input, Container,
} from 'reactstrap';

class Aminia extends Component {

  state = {
    content: "",
    updatePostId: null,
  }

  resetForm = () => {
    this.setState({content:"", updatePostId:null});
  }

  selectForEdit = (id) => {
    let post = this.props.posts[id];
    this.setState({content: post.content, updatePostId:id});
  }

  submitPost = (event) => {
    event.preventDefault();
    if (this.state.updatePostId === null){
      this.props.addPost(this.state.content);
    } else {
      this.props.updatePost(this.state.updatePostId, this.state.content)
    }
    this.resetForm();
  }


  render() {
    return (
      <div>
        <h2>Welcome to Aminia</h2>
        <hr/>

        <p>Naskia kuzitoka!!</p>
          <Container>
            <Form onSubmit={this.submitPost}>
              <FormGroup>
                <Input
                  value={this.state.content}
                  placeholder="Enter post here..."
                  onChange = {(event)=> this.setState({content:event.target.value})}
                  required
                />
                <Button outline className="m-1" onClick={this.resetForm} block>Reset</Button>
                <Button outline className="m-1" type="submit" color="success" block>Save Post</Button>
              </FormGroup>
            </Form>
          </Container>


        <p>
          <Link to="/contact">Click Here</Link> to contact us.
        </p>
        <h3>Posts</h3>

        <table>
          <tbody>
            {this.props.posts.map((post, id) => (
              <tr key={`post_${post.id}`}>
                <td>{post.content}</td>
                <td>
                  <Button outline color="prinary" onClick={() => this.selectForEdit(id)}>
                    edit
                  </Button>
                </td>
                <td>
                  <Button outline color="danger" onClick={() => this.props.deletePost(id)}>
                    delete
                  </Button>
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
    addPost: (content) => {
      dispatch(posts.addPost(content))
    },
    updatePost: (id, content) => {
      dispatch(posts.updatePost(id, content))
    },
    deletePost: (id) => {
      dispatch(posts.deletePost(id))
    },
  }
}

export default connect(mapStateToProps,mapDispatchToProps)(Aminia);
