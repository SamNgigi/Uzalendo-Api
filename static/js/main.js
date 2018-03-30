// This function allows us to pass in a query on to our url
function getParameterByName(name, url) {
  if(!url){
    url = window.location.href;
  }
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
    results = regex.exec(url);
  if(!results) return null;
  if(!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}


// Note:
// "{% url 'posts_api:post_list_api' %}" would work if we working with a block script. i.e in base.html
// However with an external script file we have to write out the url the old fashion way

$(document).ready(function() {
  console.log("Working");

  var query = getParameterByName('q')

  console.log(query);

  $.ajax({
    url:"/posts/api/",
    // Our search term is passed in as data. This basically does "/posts/api/?q= + query" which we can also do.
    data:{
      "q": query
    },
    method:"GET",
    success: function(data) {
      // Loging if call is successful
        console.log(data);
        // Loging data in key value pair
        $.each(data, function(key, value){
          console.log(key);
          console.log(value.user);
          console.log(value.content);
          // Storing data from ajax call.
          var postKey = value.key;
          var postUser = value.user;
          var postContent = value.content;
          // Ajax rendering of the call. Long and messy html definition
          $("#post-container").append(
            "<p>"+ "-" + postContent + "<br/>" + postUser.username + " | " + "<a href='#'>View</a>" +"</p>" + "<br/>" + "<hr>"
          )
        })
    },
    error: function(data){
      console.log("error");
      console.log(data);
    }
  })
});
