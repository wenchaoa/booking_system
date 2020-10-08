$(document).ready(function() {
    var username;
    
    //like building
    $('#like_btn').click(function() {
        var buildingIdVar;
        buildingIdVar = $(this).attr('data-buildingid');

        $.get('/booking_system/like_building/',
            {'building_id': buildingIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn').removeClass('btn-primary').addClass('btn-secondary');
                $('#like_btn').attr({"disabled":"disabled"});
//                $('#like_btn').hide();
            })
    });

    
    //09-11 slot1
    $('#tab1-0911-slot1').click(function() {
        var r = confirm("Would you confirm this book?");
        if (r == true){
            var name = $(this).attr('data-username');
            var time = $(this).attr('data-timeperiod');
            var date = $(this).attr('data-date');
            var room = $(this).attr('data-room');
            alert("You have booked " + room + " on " + date + " from 09:00 to 11:00");
            
            $.get('/booking_system/test/',
                  {'name': name, 'time': time, 'date': date, 'room': room},
                  function(data) {
                $('#tab1-0911-slot1').removeClass('btn-outline-info').addClass('btn-success');
                $('#tab1-0911-slot1').text(data + " booked");
                $('#tab1-0911-slot1').attr({"disabled":"disabled"});
            })
        }
    });
    
    //09-11 slot2
    $('#tab1-0911-slot2').click(function() {
        var r = confirm("Would you confirm this book?");
        if (r == true){
            var name = $(this).attr('data-username');
            var time = $(this).attr('data-timeperiod');
            var date = $(this).attr('data-date');
            var room = $(this).attr('data-room');
            alert("You have booked " + room + " on " + date + " from 09:00 to 11:00");
            
            $.get('/booking_system/test/',
                  {'name': name, 'time': time, 'date': date, 'room': room},
                  function(data) {
                $('#tab1-0911-slot2').removeClass('btn-outline-info').addClass('btn-success');
                $('#tab1-0911-slot2').text(data + " booked");
                $('#tab1-0911-slot2').attr({"disabled":"disabled"});
            })
        }
    });
    
    //11-13 slot1
    $('#tab1-1113-slot1').click(function() {
        var r = confirm("Would you confirm this book?");
        if (r == true){
            var name = $(this).attr('data-username');
            var time = $(this).attr('data-timeperiod');
            var date = $(this).attr('data-date');
            var room = $(this).attr('data-room');
            alert("You have booked " + room + " on " + date + " from 11:00 to 13:00");
            
            $.get('/booking_system/test/',
                  {'name': name, 'time': time, 'date': date, 'room': room},
                  function(data) {
                $('#tab1-1113-slot1').removeClass('btn-outline-info').addClass('btn-success');
                $('#tab1-1113-slot1').text(data + " booked");
                $('#tab1-1113-slot1').attr({"disabled":"disabled"});
            })
        }
    });
    
    //11-13 slot2
    $('#tab1-1113-slot2').click(function() {
        var r = confirm("Would you confirm this book?");
        if (r == true){
            var name = $(this).attr('data-username');
            var time = $(this).attr('data-timeperiod');
            var date = $(this).attr('data-date');
            var room = $(this).attr('data-room');
            alert("You have booked " + room + " on " + date + " from 11:00 to 13:00");
            
            $.get('/booking_system/test/',
                  {'name': name, 'time': time, 'date': date, 'room': room},
                  function(data) {
                $('#tab1-1113-slot2').removeClass('btn-outline-info').addClass('btn-success');
                $('#tab1-1113-slot2').text(data + " booked");
                $('#tab1-1113-slot2').attr({"disabled":"disabled"});
            })
        }
    });
    
    
    //13-15 slot1
    $('#tab1-1315-slot1').click(function() {
        var r = confirm("Would you confirm this book?");
        if (r == true){
            var name = $(this).attr('data-username');
            var time = $(this).attr('data-timeperiod');
            var date = $(this).attr('data-date');
            var room = $(this).attr('data-room');
            alert("You have booked " + room + " on " + date + " from 13:00 to 15:00");
            
            $.get('/booking_system/test/',
                  {'name': name, 'time': time, 'date': date, 'room': room},
                  function(data) {
                $('#tab1-1315-slot1').removeClass('btn-outline-info').addClass('btn-success');
                $('#tab1-1315-slot1').text(data + " booked");
                $('#tab1-1315-slot1').attr({"disabled":"disabled"});
            })
        }
    });
    
    //13-15 slot2
    $('#tab1-1315-slot2').click(function() {
        var r = confirm("Would you confirm this book?");
        if (r == true){
            var name = $(this).attr('data-username');
            var time = $(this).attr('data-timeperiod');
            var date = $(this).attr('data-date');
            var room = $(this).attr('data-room');
            alert("You have booked " + room + " on " + date + " from 13:00 to 15:00");
            
            $.get('/booking_system/test/',
                  {'name': name, 'time': time, 'date': date, 'room': room},
                  function(data) {
                $('#tab1-1315-slot2').removeClass('btn-outline-info').addClass('btn-success');
                $('#tab1-1315-slot2').text(data + " booked");
                $('#tab1-1315-slot2').attr({"disabled":"disabled"});
            })
        }
    });
    
    //15-17 slot1
    $('#tab1-1517-slot1').click(function() {
        var r = confirm("Would you confirm this book?");
        if (r == true){
            var name = $(this).attr('data-username');
            var time = $(this).attr('data-timeperiod');
            var date = $(this).attr('data-date');
            var room = $(this).attr('data-room');
            alert("You have booked " + room + " on " + date + " from 15:00 to 17:00");
            
            $.get('/booking_system/test/',
                  {'name': name, 'time': time, 'date': date, 'room': room},
                  function(data) {
                $('#tab1-1517-slot1').removeClass('btn-outline-info').addClass('btn-success');
                $('#tab1-1517-slot1').text(data + " booked");
                $('#tab1-1517-slot1').attr({"disabled":"disabled"});
            })
        }
    });
    
    //15-17 slot2
    $('#tab1-1517-slot1').click(function() {
        var r = confirm("Would you confirm this book?");
        if (r == true){
            var name = $(this).attr('data-username');
            var time = $(this).attr('data-timeperiod');
            var date = $(this).attr('data-date');
            var room = $(this).attr('data-room');
            alert("You have booked " + room + " on " + date + " from 15:00 to 17:00");
            
            $.get('/booking_system/test/',
                  {'name': name, 'time': time, 'date': date, 'room': room},
                  function(data) {
                $('#tab1-1517-slot2').removeClass('btn-outline-info').addClass('btn-success');
                $('#tab1-1517-slot2').text(data + " booked");
                $('#tab1-1517-slot2').attr({"disabled":"disabled"});
            })
        }
    });

    
});
