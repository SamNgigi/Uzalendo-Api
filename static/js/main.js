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

  // Stores the query url in query
  var query = getParameterByName('q')
  // console.log(query);
  var postList = []
  // Pagination allows us to have the .next property that is responsible for navigating between pages.
  // .next gives us a url that we will store in our nextPostUrl
  //  "next": "http://127.0.0.1:8000/posts/api/?page=2",
  // So simply nextPostUrl = "http://127.0.0.1:8000/posts/api/?page=2" or 3 or 1
  var nextPostUrl;


  function updateHashLinks(){
    $(".post-content").each(function(data) {
      // We are creating a regex to recoginize a #
      var hashtagRegex = /(^|\s)#([\w\d-]+)/g
      // we want the word after the word after the hash tag to be a clickable link
      var newText = $(this).html().replace(hashtagRegex, "$1<a href='/hashtag/$2/'>#$2</a>")
      $(this).html(newText)
    })
  }

// For solving ajax csrf error.
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


  // Function that displays posts
  function prependPost(postData, prepend, repost) {
    // Storing data from ajax call.
    var postId = postData.id;
    var postUser = postData.user;
    var postContent = postData.content;
    var dateDisplay = postData.date_display;
    var postContent = postData.content;
    var postFormattedHtml;
    // Returns formated with a repost tag if it isn't an original post
    if (repost && postData.parent){
      // Repost
      var rePost = postData.parent
      postFormattedHtml = "<span style='color:grey'>Repost by "+postUser.username+" on "+dateDisplay+"</span><br/><br/>"+"<p class='post-content'>" + postId + " -" + rePost.content + "<br/> <a href='" + rePost.user.url + "'>" + rePost.user.username + "</a> |  " + dateDisplay + "  |  " + "<a href='/posts/"+ rePost.id +"/'>View</a>" + "  |  "  + "<a href='/posts/"+ rePost.id +"/repost/'>Repost</a>" + "</p><br/><hr>"

    }else{
      // Original Post
      postFormattedHtml = "<p class='post-content'>"+ postId  + " -" + postContent + "<br/> <a href='" + postUser.url + "'>" + postUser.username + "</a> |  " + dateDisplay + "  |  " + "<a href='/posts/"+ postId +"/'>View</a>" +"  |  " + "<a href='/posts/"+ postId +"/repost/'>Repost</a>" + "</p>" + "<br/>" + "<hr>"

    }

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
        if (value.parent){
          prependPost(value, false, true)
        }else{
          prependPost(value)
        }

      })
    }
  }

  // Having the ajax call in a function gives us the abilitu to be able to call it anywhere.
  function fetchPosts(url) {
    console.log('fetching..');
    var fetchUrl;
    if(!url){
      fetchUrl = "/posts/api/"
    } else {
      fetchUrl = url
    }
    $.ajax({
      url: fetchUrl,
      // Our search term is passed in as data. This basically does "/posts/api/?q= + query" which we can also do.
      data: {
        "q": query
      },
      method: "GET",
      success: function(data) {
        // Loging if call is successful
        // console.log(data);
        // Storing our data in our empty postList
        postList = data.results
        if (data.next){
          // Getting next page from pagination
          nextPostUrl = data.next
        } else {
          // We hide load more link if .next propery is null.
          $('#loadMore').css("display", "none")
        }
        // Parsing the data from postList
        parsePosts()
        // hashtag links
        updateHashLinks()

      },
      error: function(data) {
        console.log("error");
        console.log(data);
      }
    })
  }
  // Calling the fetchPosts everytime the page loads.
  fetchPosts()

  // Load more
  $('#loadMore').click(function(event) {
    event.preventDefault()
    if(nextPostUrl){
      // We pass in our next url through the fetchPosts(url)
      fetchPosts(nextPostUrl)
    }
  })

  // Char counting
  var charsStart = 155;
  var charsCounter = 0;
  // Appending characters left counter to our create post form
  $("#post-form").append(
    "<span id='postCharsLeft' class='badge  badge-pill'>" + charsStart +"</span>"
  )
  // Just incase input[type=text]. Our input is not a textarea.
  $("#post-form input[type=text]").keyup(function(event) {
// Would return the key number and the time i typed the specific character.
// console.log(event.key, event.timeStamp);
  // Storing our values
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
    } else if(charsCounter === 0) {
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
    // Submit if charsCounter is more the 0
    if(charsCounter >= 0){
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
          // hash tag links
          updateHashLinks()


        },
        error: function(data) {
          console.log("error");
          console.log(data.statusText);
          console.log(data.status);
        }
      })
    } else {
      console.log("Cannot submit post. Too long.");
    }


  });


  // Search on key up
  var typingTimer;
  var doneInterval = 1000; //ms
  var searchQuery = $('#searchForm input[type=text]')
  var searchQuery;

  searchQuery.keyup(function(event) {
    // console.log(event.key);
    searchQuery = $(this).val()
    // console.log(searchQuery)
    // clearTimeout seems like an inbuilt function.
    // Start searching after someone stops typing. I.e on key up.
    clearTimeout(typingTimer)
    typingTimer = setTimeout(doneSearchTyping, doneInterval)
  })
  searchQuery.keydown(function(event) {
    // console.log(event.key);
    // While typing.
    clearTimeout(typingTimer)

  })
  function doneSearchTyping() {
    if(searchQuery){
      // do search
      var url = '/posts/search/?q=' + searchQuery
      document.location.href = url;
    }
  }

});
