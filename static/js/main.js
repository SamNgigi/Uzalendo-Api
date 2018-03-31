// This function allows us to pass in a query on to our url
function getParameterByName(name, url) {
  if (!url) {
    url = window.location.href;
  }
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
    results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}


// Note:
// "{% url 'posts_api:post_list_api' %}" would work if we working with a block script. i.e in base.html
// However with an external script file we have to write out the url the old fashion way >> url:"/posts/api/"

$(document).ready(function() {

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      }
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
      }
    }
  });


  // console.log("Working");

  // Stores the query url in query
  var query = getParameterByName('q')
  // console.log(query);

  var postList = []

  function prependPost(postData, prepend) {
    // Storing data from ajax call.
    var postUser = postData.user;
    var postContent = postData.content;
    var dateDisplay = postData.date_display;
    var postContent = postData.content;
    var postFormattedHtml = "<p>" + "-" + postContent + "<br/>" + postUser.username + "  |  " + dateDisplay + "  |  " + "<a href='#'>View</a>" + "</p>" + "<br/>" + "<hr>"

    if (prepend == true){
      $("#post-container").prepend(postFormattedHtml)
    }else{
      // Ajax rendering of the call. Long and messy html definition
      $("#post-container").append(postFormattedHtml)
    }
  }

  function parsePosts() {
    // Loging data in key value pair and storing the data to postList
    if (postList === 0) {
      $('#post-container').text("No posts currently found")
    } else {
      // Posts exist therefore parse and display them
      $.each(postList, function(key, value) {
        // console.log(key);
        // console.log(value.user);
        // console.log(value.content);
        var postKey = key;
        prependPost(value)
      })
    }
  }

  // Having the ajax call in a function gives us the abilitu to be able to call it anywhere.
  function fetchPosts() {
    console.log('fetching..');
    $.ajax({
      url: "/posts/api/",
      // Our search term is passed in as data. This basically does "/posts/api/?q= + query" which we can also do.
      data: {
        "q": query
      },
      method: "GET",
      success: function(data) {
        // Loging if call is successful
        // console.log(data);
        // Storing our data in our empty postList
        postList = data
        // Parsing the data from postList
        parsePosts()

      },
      error: function(data) {
        console.log("error");
        console.log(data);
      }
    })
  }
  // Calling the fetchPost everytime the page loads.
  fetchPosts()

  var charsStart = 30;
  var charsCounter = 0;
  // Appending characters left counter to our create post form
  $("#post-form").append(
    "<span id='postCharsLeft' class='badge  badge-pill'>" + charsStart +"</span>"
  )
  // Just incase input[type=text]. Our input is not a textarea.
  $("#post-form input[type=text]").keyup(function(event) {
    // Would return the key number and the time i typed the specific character.
    // console.log(event.key, event.timeStamp);

    var keyValue = $(this).val()
    console.log(keyValue);
    charsCounter = charsStart - keyValue.length
    charDisplay = $("#postCharsLeft")
    charDisplay.text(charsCounter)

    if(charsCounter > 0){
      // Do something
      charDisplay.removeClass("badge-secondary")
      charDisplay.removeClass("badge-danger")
      charDisplay.addClass("badge-success")
    } else if(charsCounter == 0) {
      charDisplay.removeClass("badge-success")
      charDisplay.addClass("badge-secondary")
      charDisplay.removeClass("badge-success")
    } else if (charsCounter < 0){
      charDisplay.removeClass("badge-success")
      charDisplay.addClass("badge-danger")
      charDisplay.removeClass("badge-secondary")
    }
  })


  $("#post-form").submit(function(event) {
    // Prevents default submition
    event.preventDefault()
    var submited = $(this)
    console.log(event);
    console.log(submited.serialize());
    var formData = submited.serialize()

    $.ajax({
      url: "/posts/api/create/",
      // data is now our serialized form data.
      data: formData,
      method: "POST",
      success: function(data) {
        submited.find("input[type=text], textarea").val("")
        // Loging if call is successful
        console.log(data);
        // fetching updated list
        // fetchPosts()
        prependPost(data, true)


      },
      error: function(data) {
        console.log("error");
        console.log(data.statusText);
        console.log(data.status);
      }
    })

  });

});
