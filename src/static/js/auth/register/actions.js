/* ---Toggle Government Id Field and Degrees Field Based Upon User Type--- */
function toggle_user_type(){
    const user_type = user_type_select.options[user_type_select.selectedIndex].value;
    
    if(user_type == "patient"){
        government_id_field.parentElement.style.display = "none";
        degree_fields[0].parentElement.style.display = "none";
    }

    else{
        government_id_field.parentElement.style.display = "flex";
        degree_fields[0].parentElement.style.display = "grid";
    }
}