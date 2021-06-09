$(document).ready(function(){
   $("#car").submit(function(e){
      if ($("#car")[0].checkValidity()) {
        //prevent Default functionality
        e.preventDefault();
        $("#overlay").show();
        //get the action-url of the form
        var actionurl = e.currentTarget.action;

        //do your own request an handle the results
        $.ajax({
           url: actionurl,
           type: 'post',
           dataType: 'json',
           data: $("#car").serialize(),
                success: function(data) {
                    document.getElementById('result').innerHTML = data.carPrice;
                },
                error: function (xhr, ajaxOptions, thrownError) {
                    document.getElementById('result').innerHTML = "<p class='text-danger'> Error in predicting selling price </p>";
                    console.log(thrownError);
                },
                complete: function() {
                 $("#overlay").hide();
                }
        });
      }
      else {
          e.preventDefault()
          e.stopPropagation()
       }
      $("#car")[0].classList.add('was-validated')
   });
});