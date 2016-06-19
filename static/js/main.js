$(document).on('ready', function(){

	// $(document).on('click','.body-container', function(event){
 //       	// $(document).find('.active-bell').removeClass('active-bell');
 //        // $this.removeClass('active-bell');
 //        closeNav();
 //    });
 	$('#arrow').hide();
	$(document).on('click','.notify', function(event){
        // alert("clicked");
        $this = $(this);
        $this.addClass('active-bell');
        openNav();
    });

    $(document).on('click','.active-bell', function(event){
        $this = $(this);
        $this.removeClass('active-bell');
        closeNav();
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