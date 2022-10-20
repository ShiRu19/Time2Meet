window.onload = function() {
    table.init();
    login.init();
}

mouseDown = false;
fillInColor = "white";
isGreen = 0;
userTime = [];

var table = {
    createRow: 10,
    currCell: null,
    init() {
        var userTable = document.getElementById('userTable');
        var integrateTable = document.getElementById('integrateTable');

        // Create week of table.
        this.createTable_title(userTable);
        this.createTable_title(integrateTable);

        // Create content row of table
        this.createTable_user(userTable);
        this.createTable_integrate(integrateTable);
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
        for(let row = 0; row < this.createRow; row++) {
            var div_row = document.createElement('div');
            div_row.className = "timeOfTable";
            for(let cell = 0; cell < 7; cell++) {
                var div_cell = document.createElement('div');
                userTime.push(0);
                div_cell.style.backgroundColor = "white";
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
                    printStr = "";
                    userTime.forEach(function(value) {
                        printStr += "," + value;
                    })
                    /*
                    $.ajax({
                        type: "POST",
                        url: "~/insertSQL.py",
                        data: {
                            param: "Hello world",
                        }
                    }).done((o) => {
                        console.log(o)
                    });*/
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
    createTable_integrate(table) {
        for(let row = 0; row < this.createRow; row++) {
            var div_row = document.createElement('div');
            div_row.className = "timeOfTable";
            for(let cell = 0; cell < 7; cell++) {
                var div_cell = document.createElement('div');
                div_cell.style.backgroundColor = "white";
                div_cell.id = "integrate" + (row*7 + cell);
                div_row.appendChild(div_cell);
            }
            table.appendChild(div_row);
        }
    }
}

var login = {
    init() {
        $("#loginBtn").click(function(e) {
            var userName_enter = $("#userName_enter").val();
            var userPassword_enter = $("#userPassword_enter").val();

            if(userName_enter == ""){
                alert("Please enter your name.");
            }
            else {
                $("#userName").text(userName_enter);
                
                // Create new user.
                $.ajax({
                    url: "createUser/",
                    data: {
                        'userName': userName_enter,
                        'userPassword': userPassword_enter
                    },
                    success: function(return_data){
                        if(return_data == "Create success") {
                            $("#userLogin").hide();
                            $("#userTable").show();
                        }
                        else {
                            alert(return_data);
                        }
                    }
                })
            }
        })
    }
}