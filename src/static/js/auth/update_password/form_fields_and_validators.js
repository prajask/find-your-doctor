/* ---Initializing Fields and Validators--- */

/* Password Fields and Validators */
const password_field = document.querySelector("#password");
const password_helper = document.querySelector("#password-helper");
const confirm_password_field = document.querySelector("#confirm_password");
const confirm_password_helper = document.querySelector("#confirm-password-helper");
const password_validator = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.* )(?=.*[^a-zA-Z0-9]).{8,30}$/;

/* Form Element */
const password_updation_form = document.querySelector("#password-update-form");