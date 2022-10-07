window.onload = function() {
    var newProjectName = document.getElementById("newProjectName");
    var goBtn = document.getElementById('goBtn');
    newProjectName.onfocus = function(){
        if(newProjectName.value == "New Project Name"){
            newProjectName.value = '';
            newProjectName.style.color = "black";
        }
    }
    newProjectName.onblur = function() {
        if(newProjectName.value == '') {
            newProjectName.value = "New Project Name";
            newProjectName.style.color = "darkgray";
        }
    }
}