jQuery(document).delay(2000).ready(function ($) {
    $(window).load(function() {
        $("#airports circle").each(function() {
            if ($(this).attr('r') < 10) {
                $(this).addClass('red');
            }
            if (($(this).attr('r') >= 10 ) && ($(this).attr('r') < 15 )) {
                $(this).addClass('orange');
            }
            if (($(this).attr('r') >= 15 ) && ($(this).attr('r') < 20 )) {
                $(this).addClass('yellow');
            }
            if (($(this).attr('r') >= 20 ) && ($(this).attr('r') < 25 )) {
                $(this).addClass('lightgreen');
            }
            if ($(this).attr('r') > 25) {
                $(this).addClass('darkgreen');
            }
        });
    });
});
