$(document).ready(function(){
    $(".dropdown").hover(function() {
            $(this).children().toggleClass('d-block');  //Отображение при наведении
        }
    );
    
    $.datetimepicker.setLocale('ru');

    $('#datetimepicker').datetimepicker({  
        step:30,
        minDate:0,
        timepicker:true,
        inline:true,
        format:'d.m.Y H:i',   // Календарь
    });

    $('.breadcrumbmodify .doctor').click(function(){
        $('.choosedoctor').addClass('d-block');
        $('.choosedoctor').removeClass('d-none');
        $('.chooseservice').addClass('d-none');
        $('.chooseservice').removeClass('d-block');
    });
});