/* ---Form Validation--- */


/* Registration Form Validation */
function validate_registration_form(){

    valid = true;

    validate_name();
    validate_email();
    validate_phone_number();
    validate_password();
    validate_user_type();

    const user_type = user_type_select.options[user_type_select.selectedIndex].value;
    
    if(user_type == "doctor"){
        validate_government_id();
        validate_degrees();
    }

    valid ? registration_form.submit() : false;

}

/* Password Updation Form Validation */
function validate_updatation_form(){
    valid = true;
    validate_password();

    valid ? password_updation_form.submit() : false;
}

/* Validation Functions */
function validate_name(){
    !name_validator.test(first_name_field.value) ? mark_invalid(first_name_helper) : mark_valid(first_name_helper);
    !name_validator.test(last_name_field.value) ? mark_invalid(last_name_helper) : mark_valid(last_name_helper);
}

function validate_email(){
    !email_validator.test(email_field.value) ? mark_invalid(email_helper) : mark_valid(email_helper);
}

function validate_phone_number(){
    !phone_number_validator.test(phone_number_field.value) ? mark_invalid(phone_number_helper) : mark_valid(phone_number_helper);
}

function validate_password(){
    !password_validator.test(password_field.value) ? mark_invalid(password_helper) : mark_valid(password_helper);
    !( confirm_password_field.value == password_field.value ) ? mark_invalid(confirm_password_helper) : mark_valid(confirm_password_helper);
}

function validate_user_type(){
    const user_type = user_type_select.options[user_type_select.selectedIndex].value;
    user_type == "" ? mark_invalid(user_type_helper) : mark_valid(user_type_helper);
}

function validate_government_id(){
    !government_id_validator.test(government_id_field.value) ? mark_invalid(government_id_helper) : mark_valid(government_id_helper);
}

function validate_degrees(){
    let checked = false;

    degree_fields.forEach(degree_field => {
        if(degree_field.checked){
            checked = true;
        }
    });

    !checked ? mark_invalid(degrees_field_helper) : mark_valid(degrees_field_helper);
}