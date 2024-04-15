$(document).on('change', '#filterInput', function(event) {
    event.preventDefault();  
    var search_input = $('#filterInput').val();
    var url = $(this).data("url");
    alert(url)
    alert(search_input)
    $.ajax({
        url: url,
        type: 'post',
        data: {'search_input':search_input,'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
        dataType: "json",
        success: function(data) {
           console.log("success")
           $('#example tbody').html(data.update);




            }

       
    });
});




