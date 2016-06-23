function getCookie(name) {
    var cookieValue = null;

    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}

$(document).on('ready', function(){

    $('.count').hide();

    $('.count').each(function() {
        $this = $(this);
        // $this.html("");
        // var count_value = $this.data("count");
        if ($this.data("count") > 0){
            $('.count').show();
        }
    });

    var socket = io.connect("localhost", {port: 8002});

    socket.on('message', function(message) {
        var message_json = jQuery.parseJSON(message);

        $('.count').each(function() {
            $this = $(this);
            $this.html("");
            var count_value = $this.data("count");
            
            // console.log("cv", count_value);

            count_value = count_value + 1;
            $this.append($("<strong>").text(count_value));
            $this.data("count", count_value);
            // console.log("updated cv", count_value);
        });

        $('.count').show();

        var f = document.createDocumentFragment();

        var l = document.createElement('li');
        $(l).attr('class', 'unread');

        $(l).append($("<h3>").text(message_json.actor));
        $(l).append($("<h4>").text(message_json.verb));
        $(l).append($("<h4>").text("your"));
        $(l).append($("<h4>").text(message_json.action_object));
        $(l).append($("<p>").text(message_json.timestamp));

        f.appendChild(l);
        $('.notifications-items').prepend(f);


        var f2 = document.createDocumentFragment();

        var i = document.createElement('input');
        $(i).attr('type', 'hidden');
        $(i).attr('name', 'notific_id');
        $(i).attr('value', message_json.notification_id);

        f.appendChild(i);
        $('.notification-form').prepend(f);

    });

 	$('#arrow').hide();

    $(document).on('click','.notify', function(event){
        // alert("clicked");
        event.stopPropagation();
        $this = $(this);
        $this.addClass('active-bell');
        $('#notif-box-status').val('open');
        $this.removeClass('notify');

        // $('.active-bell').each(function() {
        //     $this = $(this);
        //     status = $this.data('status');
        //     $this.data("status", "open");
        // });

        openNav();
    });

    $(document).on('click','.active-bell', function(event){
        $this = $(this);
        $this.addClass('notify');
        $('#notif-box-status').val('close');
        $this.removeClass('active-bell');

        // $('.notify').each(function() {
        //     $this = $(this);
        //     status = $this.data('status');
        //     $this.data("status", "close");
        // });

        closeNav();
        // box_status_form_submit();
    });

	$(document).not(document.querySelectorAll(".notification-container, .bell")).on('click', function(event){

        console.log("clicked outside anywhere");

        var status = "close";

        $('#notif-box-status').each(function() {
            $this = $(this);
            status = $this.val();
        });

        console.log("status = ", status);

        if (status == "open"){ 
            $('#notif-box-status').val('close');
            closeNav();
            $(document).find('.bell').removeClass('active-bell');
            $(document).find('.bell').addClass('notify');
        }
    });

    $('.notification-container').click(function(event){
    	event.stopPropagation();
    });

    $('.logout-link').click(function(){

        var status = "close";

        $('#notif-box-status').each(function() {
            $this = $(this);
            status = $this.val();
        });

        console.log("status = ", status);

        if (status == "open"){
            $('#notif-box-status').val('close');
            notification_form_submit();
        }
    });

});

function openNav() {
	$('#count').hide();
	$('#arrow').show();
    
    document.getElementById("myNav").style.height = "50%";

    $('.count').each(function() {
        $this = $(this);
        $this.html("");
        
        var count_value = $this.data("count");
        
        count_value = 0;
        $this.append($("<strong>").text(count_value));
        $this.data("count", count_value);
    });

    // $('.bell').each(function() {
    //     $this = $(this);
    //     status = $this.data('status');
    //     $this.data("status", "open");
    // });

    notification_form_submit();
}

function closeNav() {
    $('#count').hide();
    $('.count').each(function() {
        $this = $(this);
        $this.html("");
        
        var count_value = $this.data("count");
        
        count_value = 0;
        $this.append($("<strong>").text(count_value));
        $this.data("count", count_value);
    });

	document.getElementById("myNav").style.height = "0%";
	setTimeout(
		function(){
    		$('#arrow').hide();
            $('.unread').each(function() {
                $this = $(this);
                $this.removeClass('unread').addClass('read');
            });
		}, 350);

    // $('.bell').each(function() {
    //     $this = $(this);
    //     status = $this.data('status');
    //     $this.data("status", "close");
    // });
    notification_form_submit();
}


function notification_form_submit() {
    // console.log("notification form submit is working!") // sanity check

    $.ajax({
           type: "POST",
           url: "/notification_form_submit/",
           data: $("#notification-form").serialize(), // serializes the form's elements.
           // dataType: 'json',

           success: function(data){ 
                console.log("success!!");
           }
    });
}

// function box_status_form_submit() {

//     $.ajax({
//            type: "POST",
//            url: "/box_status_form_submit/",
//            data: $("#box-status-form").serialize(), // serializes the form's elements.
//            // dataType: 'json',

//            success: function(data){ 
//                 console.log("success!!");
//            }
//     });

// }