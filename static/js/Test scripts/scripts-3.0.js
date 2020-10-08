document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        
//        initialView: 'timeGridWeek',
        initialView: 'dayGridMonth',
        nowIndicator: true,
        selectable: true,
        editable: true,
        
        //header
        headerToolbar: {
            start: 'timeGridWeek,timeGridDay',
            center:  'title',
            end: 'today prev,next'
        },
        
//        views: {
//          timeGridWeek1: {
//            type: 'timeGrid',
//            duration: { days: 7 },
//            buttonText: 'Week'
//          }
//        },
        
        businessHours: {
          // days of week. an array of zero-based day of week integers (0=Sunday)
          daysOfWeek: [ 1, 2, 3, 4, 5, 6, 0], // Monday - Sunday

          startTime: '09:00', // a start time (9am)
          endTime:   '18:00', // an end time  (6pm)
        },
        
        events: [
          { // this object will be "parsed" into an Event Object
            title: 'Joshua', // a property!
            start: '2020-09-20 09:00:00', // a property!
            end: '2020-09-20 11:00:00' // a property! ** see important note below about 'end' **
          },
          {
            title: 'Leon',
            start: '2020-09-21 11:00:00',
            end: '2020-09-21 12:00:00'
          },
          {
            title: 'Simon',
            start: '2020-09-22 14:00:00',
            end: '2020-09-22 15:00:00'
          },
          {
            title: 'Joshua',
            start: '2020-09-23 10:00:00',
            end: '2020-09-23 11:00:00',
            //backgroundColor: '#ff0000'
            //backgroundColor: 'rgb(255,0,0)'
            //backgroundColor: 'red'
            backgroundColor: 'grey'
            
          }
        ],
        
        eventDrop: function(info) {
            console.log(info.event.start)
          alert(info.event.title + " was dropped on " + info.event.start.toISOString());

          if (!confirm("Are you sure about this change?")) {
            info.revert();
          }
        },
        
        select: function(info) {
            alert('Start on: ' + info.start.toString());
            
            s = info.startStr
            e = info.endStr
//            alert('111 ' + info.jsEvent.toStrin);
            calendar.addEvent({
                title: 'aaa',
                start: s,
                end: e
//                allDay: true
            });
        },
        
        
        dateClick: function(info) {
            //alert('Clicked on: ' + info.dateStr);
            var x;
            var r=confirm("Would you confirm to book?");
            if (r==true){
                
                var thisYear = info.date.getFullYear();
                var thisMonth = info.date.getMonth() + 1;
                var thisDay = info.date.getDate();
                var thisHour = info.date.getHours();
                var thisMinute = info.date.getMinutes();
                var endMinute = thisMinute + 30;

                if (thisMonth < 10){
                    thisMonth = '0' + thisMonth;
                }
                
                if (thisDay < 10){
                    thisDay = '0' + thisDay;
                }
                
                
                if (thisMinute == 0){
                    thisMinute = '00';
                }else{
                    endMinute = '00';
                }
                
                if (thisHour < 10){
                    thisHour = '0' + thisHour;
                }
                

                
                var startTime = thisYear + '-' + thisMonth + '-' + thisDay  + ' ' +
                thisHour + ':' + thisMinute + ':00';
                var endTime = thisYear + '-' + thisMonth + '-' + thisDay  + ' ' +
                thisHour + ':' + endMinute + ':00';
                
//                alert(startTime);
//                alert(endTime);
                
//                alert('h:' + h + ', m:' + m);
//                var dateStr = prompt('Enter a date YYYY-MM-DD');
                var date = new Date(startTime);
                
//                var startTime = new Date(dateStr);
//
                if(!isNaN(date.valueOf())){  //validation check
//                    alert(startTime);
                    calendar.addEvent({
                        
//                        title: 'bbb',
//                        start: '2020-09-24 12:00:00',
//                        end: '2020-09-24 15:00:00',
                    title: 'aaa',
                    start: startTime,
                    end: endTime
//                    allDay: true
                    });
                    alert(startTime);
                }
                
//                var dateStr = prompt('Enter a date in YYYY-MM-DD format');
//                var date = new Date(dateStr + 'T00:00:00'); // will be in local time

//                if (!isNaN(date.valueOf())) { // valid?
//                  calendar.addEvent({
//                    title: 'dynamic event',
//                    start: date,
//                    end:
//                    allDay: true
//                  });
//                  alert('Great. Now, update your database...');
//                } else {
//                  alert('Invalid date.');
//                }
                
                
                
//                events: function(info) {
//
//                },
//                color: 'yellow',   // an option!
//                textColor: 'black', // an option!
                
                //$.get('/booking_system/test/',{'': h, '': m}
                    
                /*
                $('#like_btn').click(function() {
                    var categoryIdVar;
                    categoryIdVar = $(this).attr('data-categoryid');
                    
                    $.get('/booking_system/like_category/',
                          {'category_id': categoryIdVar},
                          function(data) {
                              $('#like_count').html(data);
                              $('#like_btn').hide();
                          })
                        
                });
                 
                */
            }
            
            
            
        },
        
    });
    
    calendar.render();
});
