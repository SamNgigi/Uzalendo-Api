$(document).ready(function() {
  console.log("Working");
  $.ajax({
    url:"/posts/api/",
    method:"GET",
    success: function(data) {
        console.log(data);
    },
    error: function(data){
      console.log("error");
      console.log(data);
    }
  })
  // Note:
  // "{% url 'posts_api:post_list_api' %}" would work if we working with a block script. i.e in base.html
  // However with an external script file we have to write out the url the old fashion way
});
