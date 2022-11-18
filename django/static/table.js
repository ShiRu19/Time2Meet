window.onload = function() {
    projectData.init();
    formTable.init();
    login.init();
    formTable.loadAvailableTime_project();
    $('#flexSwitchCheck_uncertain').click(function() {
        if($('#flexSwitchCheck_uncertain').prop("checked")) {
            alert("clicked");
        }
    });
    
}

mouseDown = false;
fillInColor = "white";
isGreen = 0;
userTime = [];
projectTime = [];
allUserTime = {};
projectId = -1;
userId = -1;
countOfUser = -1;
userLogin = false;

var projectData = {
    init() {
        this.getProjectId();
        this.getUserCount();
        this.getAvailableTime_allUser();
    },
    getProjectId() {
        // reload project id
        projectId = window.location.pathname;
        projectId = projectId.substring(1);
    },
    getUserCount() {
        // reload count of user
        $.ajax({
            url: "getUserCount/",
            data: {
                'projectId': projectId
            },
            success: function(return_data){
                countOfUser = return_data;
            }
        });
    },
    getAvailableTime_allUser() {
        // Get all user available time.
        $.ajax({
            url: "getAvailableTime_allUser/",
            data: {
                'projectId': projectId
            },
            success: function(return_data){
                allUserTime = JSON.parse(return_data);
            }
        });
    }
}

var formTable = {
    createRow: 10,
    currCell: null,
    init() {
        var userTable = document.getElementById('userTable');
        var projectTable = document.getElementById('projectTable');

        // Create week of table.
        this.createTable_title(userTable);
        this.createTable_title(projectTable);

        // Create content row of table
        this.createTable_user(userTable);
        this.createTable_project(projectTable);
    },
    createTable_title(table) {
        var div_title = document.createElement('div');
        div_title.className = "titleOfTable";
        let week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        for(let cell = 0; cell < 7; cell++) {
            var div_title_cell = document.createElement('div');
            div_title_cell.innerHTML = week[cell];
            div_title.appendChild(div_title_cell);
        }
        table.appendChild(div_title);
    },
    createTable_user(table) {
        // Create user table.
        for(let row = 0; row < this.createRow; row++) {
            var div_row = document.createElement('div');
            div_row.className = "timeOfTable";
            for(let cell = 0; cell < 7; cell++) {
                var div_cell = document.createElement('div');
                div_cell.style.backgroundColor = "white";
                userTime.push(0)
                div_cell.ondragstart = () => {
                    return false;
                };
                div_cell.id = "user" + (row*7 + cell);

                div_cell.addEventListener("mousedown", function mousedownHandle() {
                    // user table
                    var myCell = document.getElementById("user" + (row*7 + cell));
                    if(myCell.style.backgroundColor == "white") {
                        fillInColor = "green";
                        isGreen = 1;
                    } else {
                        fillInColor = "white";
                        isGreen = 0;
                    }
                    myCell.style.backgroundColor = fillInColor;

                    // project table
                    var myCell_project = document.getElementById("project" + (row*7 + cell));
                    projectTime[row*7 + cell] = projectTime[row*7 + cell] - userTime[row*7 + cell] + isGreen;
                    if(projectTime[row*7 + cell] == 0) {
                        myCell_project.style.backgroundColor = "white";
                        myCell_project.style.opacity = 1;
                    }
                    else {
                        myCell_project.style.backgroundColor = "green";
                        myCell_project.style.opacity = projectTime[row*7 + cell] / countOfUser;
                    }
                    userTime[row*7 + cell] = isGreen;
                    mouseDown = true;
                });

                div_cell.addEventListener('mouseup', function mouseupHandle() {
                    mouseDown = false;
                    // Update user available time.
                    availableTime_user = "";
                    userTime.forEach(function(value) {
                        availableTime_user += "," + value;
                    });
                    $.ajax({
                        url: "updateAvailableTime_user/",
                        data: {
                            'projectId': projectId,
                            'userId': userId,
                            'availableTime': availableTime_user.substring(1)
                        },
                        success: function(return_data){
                            if(return_data != "Update success") alert(return_data);
                        }
                    });

                    // Update project available time.
                    availableTime_project = "";
                    projectTime.forEach(function(value) {
                        availableTime_project += "," + value;
                    })
                    $.ajax({
                        url: "updateAvailableTime_project/",
                        data: {
                            'projectId': projectId,
                            'availableTime': availableTime_project.substring(1)
                        },
                        success: function(return_data){
                            if(return_data != "Update success") alert(return_data);
                        }
                    });

                    // Update all user available time.
                    allUserTime["user" + userId] = userTime;
                });

                div_cell.addEventListener('mousemove', function mousemoveHandle() {
                    if(mouseDown) {
                        // user table
                        var myCell = document.getElementById("user" + (row*7 + cell));
                        myCell.style.backgroundColor = fillInColor;

                        // project table
                        var myCell_project = document.getElementById("project" + (row*7 + cell));
                        projectTime[row*7 + cell] = projectTime[row*7 + cell] - userTime[row*7 + cell] + isGreen;
                        if(projectTime[row*7 + cell] == 0) {
                            myCell_project.style.backgroundColor = "white";
                            myCell_project.style.opacity = 1;
                        }
                        else {
                            myCell_project.style.backgroundColor = "green";
                            myCell_project.style.opacity = projectTime[row*7 + cell] / countOfUser;
                        }

                        userTime[row*7 + cell] = isGreen;
                    }
                });

                div_row.appendChild(div_cell);
            }
            table.appendChild(div_row);
        }
    },
    createTable_project(table) {
        for(let row = 0; row < this.createRow; row++) {
            var div_row = document.createElement('div');
            div_row.className = "timeOfTable";
            for(let cell = 0; cell < 7; cell++) {
                var div_cell = document.createElement('div');
                div_cell.style.backgroundColor = "white";
                div_cell.id = "project" + (row*7 + cell);
                projectTime.push(0);

                div_cell.addEventListener('mouseenter', function mouseenterHandle() {
                    var availableUser = [];
                    var unavailableUser = [];
                    Object.keys(allUserTime).forEach(function(key) {
                        if(allUserTime[key][row*7 + cell] == 1) {
                            availableUser.push(key);
                        }
                        else if(allUserTime[key][row*7 + cell] == 0) {
                            unavailableUser.push(key);
                        }
                    });

                    availableUser.forEach(function(user) {
                        const div_available = document.createElement('div');
                        div_available.className = "userList";
                        const newContent = document.createTextNode(user);
                        div_available.appendChild(newContent);
                        $('#availableList').append(div_available);
                    });
                    unavailableUser.forEach(function(user) {
                        const div_unavailable = document.createElement('div');
                        div_unavailable.className = "userList";
                        const newContent = document.createTextNode(user);
                        div_unavailable.appendChild(newContent);
                        $('#unavailableList').append(div_unavailable);
                    });

                    $("#availableCount").text(availableUser.length + "/" + countOfUser);
                    $('#userLogin').hide();
                    $('#userTable').hide();
                    $("#availableListTable").show();
                });

                div_cell.addEventListener('mouseleave', function mouseleaveHandle() {
                    // Clear the list.
                    $('#availableListTable').hide();
                    $('.userList').remove();
                    if(userLogin) {
                        $("#userLogin").hide();
                        $("#userTable").show();
                    }
                    else {
                        $("#userLogin").show();
                        $("#userTable").hide();
                    }
                })

                div_row.appendChild(div_cell);
            }
            table.appendChild(div_row);
        }
    },
    loadAvailableTime_project() {
        // Get project available time.
        $.ajax({
            url: "getAllAvailableTime_project/",
            data: {
                'projectId': projectId
            },
            success: function(return_data){
                projectTime = JSON.parse(return_data);
                for(let i = 0; i < projectTime.length; i++) {
                    var myCell = document.getElementById("project" + i);
                    if(projectTime[i] == 0) {
                        myCell.style.backgroundColor = "white";
                        myCell.style.opacity = 1;
                    }
                    else {
                        myCell.style.backgroundColor = "green";
                        myCell.style.opacity = projectTime[i] / countOfUser;
                    }
                }
            }
        })
    },
    loadAvailableTime_user() {
        // Get user available time.
        $.ajax({
            url: "getAllAvailableTime_user/",
            data: {
                'userId': userId
            },
            success: function(return_data){
                return_data = JSON.parse(return_data);
                for(let i = 0; i < return_data.length; i++) {
                    userTime[i] = return_data[i];
                    var myCell = document.getElementById("user" + i);
                    if(userTime[i] == 1) {
                        myCell.style.backgroundColor = "green";
                    }
                }
            }
        });
    },
    reloadAvailableTime_project() {
        for(let i = 0; i < projectTime.length; i++) {
            var myCell = document.getElementById("project" + i);
            if(projectTime[i] == 0) {
                myCell.style.backgroundColor = "white";
                myCell.style.opacity = 1;
            }
            else {
                myCell.style.backgroundColor = "green";
                myCell.style.opacity = projectTime[i] / countOfUser;
            }
        }
    }
}

var login = {
    init() {
        $("#signUpBtn").click(function(e) {
            var userName_enter = $("#userName_enter").val();
            var userPassword_enter = $("#userPassword_enter").val();

            if(userName_enter == ""){
                alert("Please enter your name.");
                return;
            }

            // Create new user.
            $.ajax({
                url: "createUser/",
                data: {
                    'userName': userName_enter,
                    'userPassword': userPassword_enter,
                    'projectId': projectId
                },
                success: function(return_data){
                    projectData.getUserCount();
                    login.switchScreen(return_data, userName_enter);
                }
            });
        });

        $("#loginBtn").click(function(e) {
            var userName_enter = $("#userName_enter").val();
            var userPassword_enter = $("#userPassword_enter").val();

            if(userName_enter == ""){
                alert("Please enter your name.");
                return;
            }

            // User Login.
            $.ajax({
                url: "userLogin/",
                data: {
                    'userName': userName_enter,
                    'userPassword': userPassword_enter,
                    'projectId': projectId
                },
                success: function(return_data){
                    return_data_login = return_data;
                    userLogin = true;
                    login.switchScreen(return_data, userName_enter);
                }
            });
        });
    },
    switchScreen(return_data, userName_enter) {
        return_data = JSON.parse(return_data);
        if(return_data.result == "Login success" || return_data.result == "Sign up success") {
            userId = return_data.userId;
            formTable.loadAvailableTime_user();
            $("#userLogin").hide();
            $('#availableListTable').hide();
            $("#userTable").show();
            $("#userName").text(userName_enter);
        }
        else {
            alert(return_data.result);
        }
    }
}