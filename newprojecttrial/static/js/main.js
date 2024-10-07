function openeye(){
    var valueofpassword = document.getElementById("password");
    if(valueofpassword.type === "password"){
        valueofpassword.type= "text";
        $("#eye-icon-status").removeClass("fa-solid fa-eye");
        $("#eye-icon-status").addClass("fa-solid fa-eye-slash");
    }
    else{
        valueofpassword.type= "password";
        $("#eye-icon-status").addClass("fa-solid fa-eye");
        $("#eye-icon-status").removeClass("fa-solid fa-eye-slash");
    }
}

$(window).scroll(function(e){
    if ($(window).scrollTop()>=100 && $(window).scrollTop() !=0){
       $("button.button.is-link.modal-button").removeClass("hidden");}
    else{
       $("button.button.is-link.modal-button").addClass("hidden");}
  });
