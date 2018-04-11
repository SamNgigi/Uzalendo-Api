const initialState = [
  // {content: "Initial Post!"}
]

export default function posts(state=initialState, action) {
  let postsList = state.slice();

  switch (action.type) {
    case 'FETCH_POSTS':
      return [...state, action.posts]

    case 'ADD_POST':
      return [...state, action.post]

    case 'UPDATE_POST':

    // Here we do not update a state directly but we return a new state to replace the current state.

      let postToUpdate = postsList[action.index]
      postToUpdate.content = action.post.content
      postsList.splice(action.index, 1, postToUpdate)
      return postsList;

    case 'DELETE_POST':
      postsList.splice(action.id, 1)
      return postsList

    default:
      return state;
  }
}

// These cases in the reducers will be only invoked when an action is dispatched of the respective type.
// In actions/posts.js we will declare these actions.
