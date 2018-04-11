export const addPosts = content => {
  return {
    type: 'ADD_NOTE',
    content
  }
}

export const addPosts = (id, content) => {
  return {
    type: 'UPDATE_NOTE',
    id,
    content
  }
}

export const addPosts = (id, content) => {
  return {
    type: 'DELETE_NOTE',
    id,
    content
  }
}
