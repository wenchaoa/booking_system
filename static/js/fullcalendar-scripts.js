document.addEventListener('DOMContentLoaded', function() {
    
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        
        initialView: 'timeGridWeek',
        nowIndicator: true,
        selectable: true,
        
        //header
        //'dayGridMonth' is removed
        headerToolbar: {
            start: 'timeGridWeek,timeGridDay',
            center:  'title',
            end: 'today prev,next'
        },
        
        //Indicate opening hours
        businessHours: {
          // days of week. an array of zero-based day of week integers (0=Sunday)
          daysOfWeek: [ 1, 2, 3, 4, 5, 6, 0], // Monday - Sunday

          startTime: '09:00', // a start time (9am)
          endTime:   '18:00', // an end time  (6pm)
        },
        
        
        //Select time and book
        select: function(info) {
            var name;
            var startTime = info.startStr;
            var endTime = info.endStr;
            var r=confirm('Would you like to confirm this booking from '
                          + startTime + ' to ' + endTime + '?');
            if(r){
                name = prompt('Please enter your name:');
                
                //Ajax technique here (data model changed)
//                $.get('/booking_system/add_event/',
//                      {'title': name, 'start': startTime, 'end': endTime},
//                      function(data){
//                          if(data){
//                              //Fullcalendar's addEvent function
//                              calendar.addEvent({
//                                  title: name,
//                                  start: startTime,
//                                  end: endTime
//                              })
//                          }
//                })
                
                calendar.addEvent({
                    title: name,
                    start: startTime,
                    end: endTime
                })
                
            }
        },
        
      
    });
    
    calendar.render();
});
