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

    var socket = io.connect("localhost", {port: 8002});

    socket.on('message', function(message) {
        var message_json = jQuery.parseJSON(message);

        $("#unread_count").text(message_json.unread_count);

        // if ("mark_as_read" in message_json) {
        //     $("#notifications-table tbody").empty();
        // } else {
            var $tr = $("<tr>");
            // $tr.append($("<td>").text(message_json.timestamp));
            $tr.append($("<td>").text(message_json.recipient));
            $tr.append($("<td>").text(message_json.actor));
            $tr.append($("<td>").text(message_json.verb));
            $tr.append($("<td>").text(message_json.action_object));
            // $tr.append($("<td>").text(message_json.target));
            // $tr.append($("<td>").text(message_json.description));

            $("#notifications-table tbody").prepend($tr);
        // }
    });

 	$('#arrow').hide();
	$(document).on('click','.notify', function(event){
        // alert("clicked");
        event.stopPropagation();
        $this = $(this);
        $this.addClass('active-bell');
        openNav();
    });

    $(document).on('click','.active-bell', function(event){
        $this = $(this);
        $this.removeClass('active-bell');
        closeNav();
    });

	$(document).not(document.querySelectorAll(".notification-container, .notify")).on('click', function(event){
        console.log("outside notification container clicked");
        $(document).find('.active-bell').removeClass('active-bell');
        closeNav();
    });

    $('.notification-container').click(function(event){
    	event.stopPropagation();
    });

});

function openNav() {
	$('#count').hide();
	$('#arrow').show();
    document.getElementById("myNav").style.height = "50%";
    
}

function closeNav() {
	document.getElementById("myNav").style.height = "0%";
	setTimeout(
		function(){
    		$('#arrow').hide();
		}, 350);
}