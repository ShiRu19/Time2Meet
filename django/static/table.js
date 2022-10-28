window.onload = function() {
    information.init();
    formTable.init();
    login.init();
    formTable.reloadAvailableTime_project();
}

mouseDown = false;
fillInColor = "white";
isGreen = 0;
userTime = [];
projectTime = [];
projectId = -1;
userId = -1;
countOfUser = -1;

var information = {
    init() {
        this.getProjectId();
        this.getUserCount();
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
        })
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
                    var myCell = document.getElementById("user" + (row*7 + cell));
                    if(myCell.style.backgroundColor == "white") {
                        fillInColor = "green";
                        isGreen = 1;
                    } else {
                        fillInColor = "white";
                        isGreen = 0;
                    }
                    myCell.style.backgroundColor = fillInColor;
                    userTime[row*7 + cell] = isGreen;
                    mouseDown = true;
                })

                div_cell.addEventListener('mouseup', function mouseupHandle() {
                    mouseDown = false;
                    availableTime = "";
                    userTime.forEach(function(value) {
                        availableTime += "," + value;
                    })
                    // Update user available time.
                    $.ajax({
                        url: "updateUserAvailableTime/",
                        data: {
                            'projectId': projectId,
                            'userId': userId,
                            'availableTime': availableTime.substring(1)
                        },
                        success: function(return_data){
                            if(return_data == "Update success"){
                                formTable.reloadAvailableTime_project();
                            }
                        }
                    })
                })

                div_cell.addEventListener('mousemove', function mousemoveHandle() {
                    if(mouseDown) {
                        var myCell = document.getElementById("user" + (row*7 + cell));
                        myCell.style.backgroundColor = fillInColor;
                        userTime[row*7 + cell] = isGreen;
                    }
                })

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
                div_row.appendChild(div_cell);
            }
            table.appendChild(div_row);
        }
    },
    reloadAvailableTime_user() {
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
        })
    },
    reloadAvailableTime_project() {
        // Get project available time.
        $.ajax({
            url: "getAllAvailableTime_project/",
            data: {
                'projectId': projectId
            },
            success: function(return_data){
                return_data = JSON.parse(return_data);
                for(let i = 0; i < return_data.length; i++) {
                    projectTime[i] = return_data[i];
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
                    information.getUserCount();
                    login.switchScreen(return_data, userName_enter);
                }
            })
        })

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
                    result_login = true;
                    login.switchScreen(return_data, userName_enter);
                }
            })
        })
    },
    switchScreen(return_data, userName_enter) {
        return_data = JSON.parse(return_data);
        if(return_data.result == "Login success" || return_data.result == "Sign up success") {
            userId = return_data.userId;
            formTable.reloadAvailableTime_user();
            $("#userLogin").hide();
            $("#userTable").show();
            $("#userName").text(userName_enter);
        }
        else {
            alert(return_data.result);
        }
    }
}