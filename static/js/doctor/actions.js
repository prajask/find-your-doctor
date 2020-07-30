/* ---DOM Actions for Doctor Users--- */

/* Navigate to Selected Appointment's Information Page */
const appointment_cards = document.querySelectorAll(".appointment-card");
appointment_cards.forEach(appointment_card => {
    appointment_card.onclick = function(){
        window.open(`/doctor/appointment/${appointment_card.id}`, "_blank");
    }
});

/* Completion and Updation of Report for Selected Appointment */
const report_actions = document.querySelectorAll(".report-option");
const report = document.querySelector("#report-form");

if(report){
    base_action = report.action;
    report.action = `${base_action}/complete_now`;

    report_actions.forEach(report_action => {
        report_action.onclick = function(){
            if(report_action.value == "complete_later" || report_action.value == "no_report") report.style.display = "none";
            else report.style.display = "block";

            report.action = `${base_action}/${report_action.value}`;
        }
    });
}

const complete_appointment_button = document.querySelector("#complete-appointment");

if(complete_appointment_button){
    complete_appointment_button.onclick = function(){
        if(report.style.display != "none"){
            validate_report() ? report.submit() : false;
        }

        else report.submit();
    }
}

const update_appointment_button = document.querySelector("#update-appointment");

if(update_appointment_button){
    report.action = `${base_action}/update`;
    update_appointment_button.onclick = () => validate_report() ? report.submit() : false;
}

/* Validate Report Fields */
function validate_report(){
    const rbc_field = document.querySelector("#red_blood_cell_count");
    const rbc_helper_field = document.querySelector("#red-blood-cell-count-helper");

    const wbc_field = document.querySelector("#white_blood_cell_count");
    const wbc_helper_field = document.querySelector("#white-blood-cell-count-helper");

    const sugar_level = document.querySelector("#sugar_level");
    const sugar_level_helper_field = document.querySelector("#sugar-level-helper");
    
    const validator = /^[0-9]{2,3}$/;
    valid = true;

    !validator.test(rbc_field.value) ? mark_invalid(rbc_helper_field) : mark_valid(rbc_helper_field);
    !validator.test(wbc_field.value) ? mark_invalid(wbc_helper_field) : mark_valid(wbc_helper_field);
    !validator.test(sugar_level.value) ? mark_invalid(sugar_level_helper_field) : mark_valid(sugar_level_helper_field);

    return valid ? true : false;
}
