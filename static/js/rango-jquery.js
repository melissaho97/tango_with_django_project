$(document).ready(function() {
    alert('Hello, world!');
    $('#about-btn').click(function() {
        alert('You clicked the button using JQuery!');
    });

    $('.ouch').click(function() {
        alert('You clicked me! Ouch!');
    });

    $('p').hover(function() {
        $(this).css('color', 'red');
    }, function() {
        $(this).css('color', 'black');
    });

    $('#about-btn').click(function() {
        msgStr = $('#msg').html();
        msgStr = msgStr + ' ooo, fancy!';
        $('#msg').html(msgStr);
    });
});
