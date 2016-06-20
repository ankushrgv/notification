$(document).on('ready', function(){

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