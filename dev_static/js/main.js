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

    $('.services').select2({
        placeholder: {
            id: '-1',
            text: 'Выберите услугу из списка или начните вводить название услуги...'
        }
      });
    $('.doctors').select2({
        placeholder: {
            id: '-1',
            text: 'Выберите врача'
        }
      });

    $('.servicebtn').click(function(e){         //ajax 
        e.preventDefault();

        csrf_token = $('#orderform [name="csrfmiddlewaretoken"]').val();
        service_id=$('.services').val();

        data = {
            'csrfmiddlewaretoken' : csrf_token,
            'service_id' : service_id,
        }

        $.ajax ({
            type: 'POST',
            url: $('#orderform').attr('action'),
            data: data,
            success: function(data){
                console.log('data.doctors');
            }
        });
    });
});