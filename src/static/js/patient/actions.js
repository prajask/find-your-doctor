/* ---DOM Actions for Patient Users--- */

/* Navigate to Selected Appointment's Information Page */
const appointment_cards = document.querySelectorAll(".appointment-card");
appointment_cards.forEach(appointment_card => {
    appointment_card.onclick = function(){
        window.location = (`/patient/appointment/${appointment_card.id}`);
    }
});

/* Appointment Booking Form Actions */
const date_field = document.querySelector("#date");

if(date_field){
    const today = new Date();

    var date = today.getDate() + 1;
    if(date < 10) date = `0${date}`;

    var month = today.getMonth() + 1;
    if(month < 10) month = `0${month}`;
    
    const year = today.getFullYear();
    date_field.value = `${year}-${month}-${date}`;
    date_field.min = `${year}-${month}-${date}`;
}

/* Appointment Booking Form Modal Triggers */
const modal_triggers = document.querySelectorAll(".modal-trigger");
const modal = document.querySelector(".datetime-modal");

modal_triggers.forEach(modal_trigger => {
    modal_trigger.onclick = function(){
        const datetime_form = document.querySelector("#appointment-datetime"); 
        datetime_form.action = `/patient/book_appointment/${modal_trigger.parentElement.id}`;
        modal.style.display = "block";
    }
});

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}