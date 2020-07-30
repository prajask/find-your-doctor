/* ---Input Fields Visual Effects--- */

/* Highlight Input Fields with Light Blue Border on Focus */
const input_fields = document.querySelectorAll("input");
const select_fields = document.querySelectorAll("select");

input_fields.forEach(input_field => {
    input_field.onfocus = function(){
        if(input_field.type != "checkbox" && input_field.type != "radio") input_field.parentElement.style.border = "2px solid #90caf9";
    }

    input_field.onblur = function(){
        if(input_field.type != "checkbox" && input_field.type != "radio") input_field.parentElement.style.border = "1px solid #35424a";
    }   
});

select_fields.forEach(select_field => {
    select_field.onfocus = function(){
        select_field.parentElement.style.border = "2px solid #90caf9";
    }

    select_field.onblur = function(){
        select_field.parentElement.style.border = "1px solid #35424a";
    }   
});

/* Show Helper Text for an Invalid Input Field  */
function mark_invalid(helper_field){
    helper_field.style.display = "flex";
    valid = false;
}

/* Hide Helper Text for a Valid Input Field */
function mark_valid(helper_field){
    helper_field.style.display = "none";
}