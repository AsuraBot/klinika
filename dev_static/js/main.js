$(document).ready(function(){
    $(".dropdown").hover(function() {
            $(this).children().toggleClass('d-block');         //я отойду
        }
    );
});