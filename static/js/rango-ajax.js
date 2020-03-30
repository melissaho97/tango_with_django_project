$(document).ready(function() {
    // Chapter 17: page 301
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

    // Chapter 17: page 312
    $('.rango-page-add').click(function() {
        var categoryid = $(this).attr('data-categoryid');
        var title = $(this).attr('data-title');
        var url = $(this).attr('data-url');
        var clickedButton = $(this);

        $.get('/rango/search_add_page/',
            {'category_id': categoryid, 'title': title, 'url': url},
            function(data) {
                $('#page-listing').html(data);
                clickedButton.hide();
            })
    });
});
