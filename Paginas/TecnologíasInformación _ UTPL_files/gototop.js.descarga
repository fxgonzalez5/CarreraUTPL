/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */




//go to top @ymtorres
(function ($) {

    $(document).ready(function () {
        $("#gototop").click(function () {
            $("html, body").animate({scrollTop: 0}, 1000);
        });

        $("#gototopfoot").click(function () {
            $("html, body").animate({scrollTop: 0}, 1000);
        });

        var navtop = $('.gototopfoot');
        $(window).scroll(function () {
            if ($(this).scrollTop() > 600 && $(this).scrollTop() + 1000 < ($("html").height())) {
                navtop.addClass("top-nav");
            } else {
                navtop.removeClass("top-nav");
            }
        });
    });


})(jQuery);
