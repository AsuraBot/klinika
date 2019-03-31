$(document).ready(function(){
    $(".dropdown").hover(function() {
            $(this).children().toggleClass('d-block');
        }
    );
    
    $.datetimepicker.setLocale('ru');

    $('#datetimepicker').datetimepicker({
        step:30,
        minDate:0,
        timepicker:true,
        inline:true,
        format:'d.m.Y H:i',
    });
});

