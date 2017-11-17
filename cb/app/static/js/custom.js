$(document).ready(function(){

	// $('.table').paging({limit:10});
	$('[data-toggle="tooltip"]').tooltip();

	 $(window).scroll(function(){
      if ($(this).scrollTop() > 300) {
        $('.scrollToTop').fadeIn();
      } else {
        $('.scrollToTop').fadeOut();
      }
    });


   NProgress.start();
   NProgress.done();

	 $('.scrollToTop').click(function(){
      $('html, body').animate({scrollTop : 0},800);
      return false;
    });

   $('ul.nav li.dropdown').hover(function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(300).slideDown(300);
      }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(300).slideUp(300);
      });

   $('#pannel').accordion({collapsible: true},{heightStyle: "content"}, {active: false});

   // $(function() { $("#id_leave_periods").daterangepicker(); });

   // Pagination Script
    $('.table').paging({limit:15});
    // END Pagination Script

});

