window.addEventListener("load" , function (){

    let today   = new Date();

    let year    = String(today.getFullYear());
    let month   = ("0" + String(today.getMonth() + 1) ).slice(-2);
    let day     = ("0" + String(today.getDate()) ).slice(-2);
    let hour    = ("0" + String(today.getHours()) ).slice(-2);
    let minute  = ("0" + String(today.getMinutes()) ).slice(-2);

    let date    = year + "-" + month + "-" + day + " " + hour + ":" + minute;

    let config_date = { 
        locale: "ja",
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        defaultDate: date,
    }

    flatpickr("[name='end_dt']", config_date);
    flatpickr("[name='start_dt']", config_date);

    console.log(events);

    const calendar_elem = document.getElementById('calendar');
    const calendar      = new FullCalendar.Calendar(calendar_elem, {
                                initialView: 'dayGridMonth',
                                events: events,
                                
                                // イベントをクリックしたとき、その箇所へ移動する。
                                // https://fullcalendar.io/docs/eventClick
                                eventClick: function(info) {
                                    console.log('Event: ' + info.event.id);
                                    const target = document.getElementById("schedule_" + info.event.id );
                                    target.scrollIntoView({  
                                        behavior: 'smooth',
                                    });
                                }
                        });

    calendar.render();


});


