$(document).ready(function(){
    $(".dropdown").hover(function() {
            $(this).children().toggleClass('d-block');  //Отображение при наведении
        }
    );

    
    (function() {
        'use strict';
        window.addEventListener('load', function() {
          // Fetch all the forms we want to apply custom Bootstrap validation styles to
          var forms = document.getElementsByClassName('needs-validation');
          // Loop over them and prevent submission
          var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
              if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
              }
              form.classList.add('was-validated');
            }, false);
          });
        }, false);
      })();


    $('.services').select2({
        placeholder: {
            id: '-1',
            text: 'Выберите услугу из списка или начните вводить название услуги...'
        }
      });

    $('.orderdoctors').select2({
        placeholder: {
            id: '-1',
            text: 'Выберите врача'
        }
      });
    
    $('.ordercities').select2({
    placeholder: {
        id: '-1',
        text: 'Выберите город из списка'
    }
    });

    $('.servicebtn').click(function(e){         //service button 
        e.preventDefault();

        csrf_token = $('#orderform [name="csrfmiddlewaretoken"]').val();
        service_id = $('.services').val();

        data = {
            'csrfmiddlewaretoken' : csrf_token,
            'service_id' : service_id,
        }

        $.ajax ({
            type: 'POST',
            url: $('#orderform').attr('action'),
            data: data,
            success: function(data){
                doctorchoice = $('.orderdoctors');
                doctorchoice.find('option').remove();
                doctorchoice.append('<option value="-1"></option>');
                for(i=0; i < data.doctors_id.length; i++){
                    doctorchoice.append('<option value="'+ data.doctors_id[i] + '">' + data.doctors_name[i] + '</option>');
                }              
            }
        });
        $('#doctor-tab').removeClass('disabled');
        $('#doctor-tab').tab('show');
        $('#city-tab').addClass('disabled');
        $('#datetime-tab').addClass('disabled');
        $('#enterinfo-tab').addClass('disabled');
    });

    $('.doctorbtn').click(function(e){         //doctor button
        e.preventDefault();

        csrf_token = $('#doctorform [name="csrfmiddlewaretoken"]').val();
        doctor_id = $('.orderdoctors').val();

        data = {
            'csrfmiddlewaretoken' : csrf_token,
            'doctor_id' : doctor_id,
        }
        
        $.ajax ({
            type: 'POST',
            url: $('#doctorform').attr('action'),
            data: data,
            success: function(data){
                citychoice = $('.ordercities');
                citychoice.find('option').remove();
                citychoice.append('<option value="-1"></option>');
                for(i=0; i < data.cities_id.length; i++){
                    citychoice.append('<option value="'+ data.cities_id[i] + '">' + data.cities_name[i] + '</option>');
                }
            }
        });
        $('#city-tab').removeClass('disabled');
        $('#city-tab').tab('show');
        $('#datetime-tab').addClass('disabled');
        $('#enterinfo-tab').addClass('disabled');
    });

    $('.citybtn').click(function(e){         //city button
        e.preventDefault();

        csrf_token = $('#cityform [name="csrfmiddlewaretoken"]').val();
        doctor_id = $('.orderdoctors').val();
        city_id = $('.ordercities').val();

        data = {
            'csrfmiddlewaretoken' : csrf_token,
            'doctor_id' : doctor_id,
            'city_id' : city_id,
        }
        
        $.ajax ({
            type: 'POST',
            url: $('#cityform').attr('action'),
            data: data,
            success: function(data){
                $.datetimepicker.setLocale('ru');
                $('#datetimepicker').datetimepicker({
                    minDate:0,
                    dayOfWeekStart:1,
                    timepicker:true,
                    inline:true,
                    todayButton:false,
                    startDate: Object.keys(data.schedule)[0],
                    allowTimes: data.schedule[Object.keys(data.schedule)[0]],
                    format:'d.m.Y H:i',   
                    allowDates: Object.keys(data.schedule), formatDate:'d.m.Y',
                    onSelectDate: function(){
                        $('.datetimebtn').addClass('d-none');
                        this.setOptions({
                            allowTimes: [],
                        })
                        datevalue = $('#datetimepicker').val();
                        datevalue = datevalue.slice(0,10);
                        console.log(datevalue);
                        this.setOptions({
                            allowTimes: data.schedule[datevalue],
                        })
                    },
                    onSelectTime: function(){
                        $('.datetimebtn').removeClass('d-none');
                    },
                });
            }
        });
        $('#datetime-tab').removeClass('disabled');
        $('#datetime-tab').tab('show');
        $('#enterinfo-tab').addClass('disabled');
    });

    $('.datetimebtn').click(function(){         //datetime button

        $('#enterinfo-tab').removeClass('disabled');
        $('#enterinfo-tab').tab('show');
    });

    $('.enterinfobtn').click(function(e){         //enterinfo button
        e.preventDefault();

        csrf_token = $('#doctorform [name="csrfmiddlewaretoken"]').val();
        doctor_id = $('.orderdoctors').val();

        data = {
            'csrfmiddlewaretoken' : csrf_token,
            'doctor_id' : doctor_id,
        }
        
        $.ajax ({
            type: 'POST',
            url: $('#doctorform').attr('action'),
            data: data,
            success: function(data){
                citychoice = $('.ordercities');
                citychoice.find('option').remove();
                citychoice.append('<option value="-1"></option>');
                for(i=0; i < data.cities_id.length; i++){
                    citychoice.append('<option value="'+ data.cities_id[i] + '">' + data.cities_name[i] + '</option>');
                }
            }
        });
    });
});