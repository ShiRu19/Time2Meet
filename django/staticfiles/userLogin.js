window.onload = function() {
    login.init();
}

var login = {
    init() {
        $("#loginBtn").click(function(e) {
            if($("#userName_enter").val() == ""){
                alert("Please enter your name.");
            }
            else {
                $("#userName").text($("#userName_enter").val());
                $("#userLogin").hide();
                $("#userTable").show();
            }
        })
    }
}