jQuery(window).on('load',function() {
    setTimeout(function() {
        $("#airports circle").each(function() {
            if ($(this).attr('r') < 12) {
                $(this).addClass('red');
            }
            if (($(this).attr('r') >= 12 ) && ($(this).attr('r') < 18.5 )) {
                $(this).addClass('orange');
            }
            if (($(this).attr('r') >= 18.5 ) && ($(this).attr('r') < 24 )) {
                $(this).addClass('yellow');
            }
            if (($(this).attr('r') >= 24 ) && ($(this).attr('r') < 27 )) {
                $(this).addClass('lightgreen');
            }
            if ($(this).attr('r') >= 27) {
                $(this).addClass('darkgreen');
            }
        });
    }, 200);
});

/*
jQuery(document).delay(2000).ready(function ($) {
    $(window).on('load',function() {
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
*/
