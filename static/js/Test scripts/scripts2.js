
window.onload=function(){

    
//document.addEventListener('DOMContentLoaded', function() {
    
    
     var calendarEl = document.getElementById('calendar');
     var calendar = new FullCalendar.Calendar(calendarEl, {
         
         nowIndicator: true,
         editable: true,
         selectable: true,
         selectHelper: true,
         
         //themeSystem: 'bootstrap',
         
         
         headerToolbar: {
             start: 'dayGridMonth,timeGridWeek1',
             center:  'title',
             end: 'today prev,next'
         },
         
         views: {
           timeGridWeek1: {
             type: 'timeGrid',
             duration: { days: 7 },
             buttonText: 'Week'
           }
         },
         
         
         events: [
           { // this object will be "parsed" into an Event Object
             title: 'Joshua', // a property!
             start: '2020-09-08 09:00:00', // a property!
             end: '2020-09-08 11:00:00' // a property! ** see important note below about 'end' **
           },
           {
             title: 'Leon',
             start: '2020-09-09 11:00:00',
             end: '2020-09-09 12:00:00'
           },
           {
             title: 'Simon',
             start: '2020-09-10 14:00:00',
             end: '2020-09-10 15:00:00'
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
          
         
         //event drop message
         eventDrop: function(info) {
           alert(info.event.title + " was dropped on " + info.event.start.toISOString());

           if (!confirm("Are you sure about this change?")) {
             info.revert();
           }
         }
         
         //day click
         dateClick: function() {
           alert('a day has been clicked!');
         },
         
     });
     calendar.render();
 }
