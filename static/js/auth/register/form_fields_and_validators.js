/* ---Initializing Fields and Validators--- */

/* Name Fields and Validators */
const first_name_field = document.querySelector("#first_name");
const first_name_helper = document.querySelector("#first-name-helper");
const last_name_field = document.querySelector("#last_name");
const last_name_helper = document.querySelector("#last-name-helper");
const name_validator = /^[a-zA-Z(\s)*]{2,}$/;

/* Email Field and Validator */
const email_field = document.querySelector("#email");
const email_helper = document.querySelector("#email-helper");
const email_validator = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

/* Phone Number Field and Validator */
const phone_number_field = document.querySelector("#phone_number");
const phone_number_helper = document.querySelector("#phone-number-helper");
const phone_number_validator = /^[0-9]{10}/;

/* Password Fields and Validators */
const password_field = document.querySelector("#password");
const password_helper = document.querySelector("#password-helper");
const confirm_password_field = document.querySelector("#confirm_password");
const confirm_password_helper = document.querySelector("#confirm-password-helper");
const password_validator = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.* )(?=.*[^a-zA-Z0-9]).{8,30}$/;

/* User Type Field and Validator */
const user_type_select = document.querySelector("#user_type");
const user_type_helper = document.querySelector("#user-type-helper");

/* Government ID Field and Validator */
const government_id_field = document.querySelector("#government_id");
const government_id_helper = document.querySelector("#government-id-helper");
const government_id_validator = /^[a-zA-Z0-9]{15}$/;

/* Degree Field and Validator */
const degree_fields = document.querySelectorAll("input[name = 'degree']");
const degrees_field_helper = document.querySelector("#degree-helper");

/* Form Element */
const registration_form = document.querySelector("#registration-form");