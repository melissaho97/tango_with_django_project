$(document).ready(function() {
    $('#like_btn').click(function() {
        var catecategoryIdVar;
        catecategoryIdVar = $(this).attr('data-categoryid');

        $.get('/rango/like_category/',
            {'category_id': catecategoryIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').hide();
            })
    });

    // Chapter 17: page 309
    $('#search-input').keyup(function() {
        var query;
        query = $(this).val();
        console.log(query);
        $.get('/rango/suggest/', {'suggestion': query},
            function(data) {
                $('#categories-listing').html(data);
            })
    });
});
