/*
 Each of the below functions returns an object with a type property by which the reducer determines how the state is to be updated.

 Besides type these payloads can have any property as values which can later be used inside the reducer function while modifying the state.

 We update the actions/index.js file so that we can access all actions in one place.
*/

export const fetchPosts = () => {
  /*
  This function will perform an API call to the django
  application at api/posts/ and dispatch the FETCH_POSTS
  action. when the response is recieved.
  */
  return dispatch => {
    let headers = {"Content-Type": "application/json"};
    return fetch("http://127.0.0.1:8000/api/posts/", {headers, })
      .then(res => res.json())
      .then(posts => {
        console.log(posts.results);
        return dispatch({
          type: 'FETCH_POSTS',
          posts
        })
      })
  }
}

export const addPost = content => {
  return {
    type: 'ADD_POST',
    content
  }
}

export const updatePost = (id, content) => {
  return {
    type: 'UPDATE_POST',
    id,
    content
  }
}

export const deletePost = id=> {
  return {
    type: 'DELETE_POST',
    id
  }
}
