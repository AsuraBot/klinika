$(document).ready(function(){
    
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
      
    $('#cityheaderinfo').change(function(){
        $("#phoneheaderinfo option[value=" + $(this).val() + "]").prop('selected', true);
    });

    $('.formsearch span').click(function(){
        $('.mainsearch').toggleClass('d-none');
        $('.formsearch .fa').toggleClass('fa-search');
        $('.formsearch .fa').toggleClass('fa-times');
    });

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

    $('.services').on('change', function(){
        $(this).siblings('.btn').removeClass('d-none')
    }); 

    $('.orderdoctors').on('change', function(){
        $(this).siblings('.btn').removeClass('d-none')
    });

    $('.ordercities').on('change', function(){
        $(this).siblings('.btn').removeClass('d-none')
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
        $('.doctorbtn').addClass('d-none');
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
        $('.citybtn').addClass('d-none');
    });

    $('.doctordoctorbtn').click(function(e){         //doctorbooknow doctor button 
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
                servicechoice = $('.services');
                servicechoice.find('option').remove();
                servicechoice.append('<option value="-1"></option>');
                for(i=0; i < data.services_id.length; i++){
                    servicechoice.append('<option value="'+ data.services_id[i] + '">' + data.services_name[i] + ' (' + data.services_price[i] + ' руб.)</option>');
                }              
            }
        });
        $('#service-tab').removeClass('disabled');
        $('#service-tab').tab('show');
        $('#city-tab').addClass('disabled');
        $('#datetime-tab').addClass('disabled');
        $('#enterinfo-tab').addClass('disabled');
        $('.doctorservicebtn').addClass('d-none');
    });

    $('.doctorservicebtn').click(function(e){         //doctorbooknow service button
        e.preventDefault();

        csrf_token = $('#orderform [name="csrfmiddlewaretoken"]').val();
        doctor_id = $('.orderdoctors').val();

        data = {
            'csrfmiddlewaretoken' : csrf_token,
            'doctor_id' : doctor_id,
        }
        
        $.ajax ({
            type: 'POST',
            url: $('#orderform').attr('action'),
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
        $('.citybtn').addClass('d-none');
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
        service = $('.services').find('option:selected').text();
        doctor = $('.orderdoctors').find('option:selected').text();
        city = $('.ordercities').find('option:selected').text();
        datetime = $('#datetimepicker').val().split(' ');
        date = datetime[0];
        time = datetime[1];

        $('#suminfo').html('<div>Услуга: ' + service + '</div> <div> Врач: ' + 
            doctor + '</div> <div> Город: ' + city + '</div> <div> Дата: ' + 
            date + '</div> <div> Время: ' + time + '</div>')

        $('#enterinfo-tab').removeClass('disabled');
        $('#enterinfo-tab').tab('show');
    });

    $('.enterinfobtn').click(function(e){         //enterinfo button
        e.preventDefault();

        csrf_token = $('#enterinfoform [name="csrfmiddlewaretoken"]').val();
        service_id = $('.services').val();
        doctor_id = $('.orderdoctors').val();
        city_id = $('.ordercities').val();
        datetime = $('#datetimepicker').val().split(' ');
        date = datetime[0];
        time = datetime[1];
        client_name = $('#client_lastname').val() + ' ' + $('#client_firstname').val() + ' ' + $('#client_surname').val();
        client_address = $('#client_address').val()
        client_phone = $('#client_phone').val()
        client_dob = $('#client_dob').val()
        client_mail = $('#client_mail').val()

        data = {
            'csrfmiddlewaretoken' : csrf_token,
            'service_id' : service_id,
            'doctor_id' : doctor_id,
            'city_id' : city_id,
            'date' : date,
            'time' : time,
            'client_name' : client_name,
            'client_address' : client_address,
            'client_phone' : client_phone,
            'client_dob' : client_dob,
            'client_mail' : client_mail,
        }
        
        $.ajax ({
            type: 'POST',
            url: $('#enterinfoform').attr('action'),
            data: data,
            success: function(data){
                
            }
        });
    });

    $(function(){
        //2. Получить элемент, к которому необходимо добавить маску
        $("#client_phone").mask("8(999) 999-9999");
      });

    $('#doctorschedulebooknow .worktime').click(function(e){         //service button
        e.preventDefault();

        csrf_token = $('#doctorschedulebooknow [name="csrfmiddlewaretoken"]').val();
        doctor_id = $('#doctorschedulebooknow').data('doctorid');
        worktime = $(this).val();
        workdate = $(this).parent().siblings().children().val();

        data = {
            'csrfmiddlewaretoken' : csrf_token,
            'doctor_id' : doctor_id,
            'worktime' : worktime,
            'workdate' : workdate,
        }

        $.ajax ({
            type: 'POST',
            url: $('#doctorschedulebooknow').attr('action'),
            data: data,
            // success: function(data){
                // doctorchoice = $('.orderdoctors');
                // doctorchoice.find('option').remove();
                // doctorchoice.append('<option value="-1"></option>');
                // for(i=0; i < data.doctors_id.length; i++){
                //     doctorchoice.append('<option value="'+ data.doctors_id[i] + '">' + data.doctors_name[i] + '</option>');
                // }              
            // }
        });
    });
});

