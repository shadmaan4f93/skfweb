$(document).ready(function(){
    $(".fa-microphone").click(function(){
        $("#search").hide();
        $('#listener').html("listening....");
        var base_url = window.location.origin;
        action = base_url + '/api/recognizer/';
        $.ajax({
            type: "GET",
            url: action,
            success: function(msg) {
                $("#search").show();
                $('#listener').hide();
                if (msg) {
                    var idselector = '#'+msg.response
                    $([document.documentElement, document.body]).animate({
                        scrollTop: $(idselector).offset().top
                    }, 2000);
                
            }
            }
        });
    });
    $(".fa-search").click(function(){
        var idselector = $("#search").val()

    });

  });