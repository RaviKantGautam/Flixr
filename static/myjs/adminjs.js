function submitadmin() {
    var form = $('#adminRegisteration').valid();
    if (form == true) {
        var controls = document.getElementById("adminRegisteration").elements;
        var formdata = new FormData();
        for (var i = 0; i < controls.length; i++) {
            if (controls[i].type == "file") {
                formdata.append(controls[i].name, controls[i].files[0]);
            } else {
                formdata.append(controls[i].name, controls[i].value);
            }
        }
        var httpreg = new XMLHttpRequest();
        httpreg.onreadystatechange = function () {
            if (this.status == 200 && this.readyState == 4) {
                var output = this.response;
                alert(output);
                if (output == 'success') {
                    window.location.href = 'adminview'
                } else {
                    document.getElementById('erroradminsubmit').innerHTML = `<span class='alert alert-danger'>${output}</span>`;
                }
                // window.location.href = '';
            }

        };
        httpreg.open("POST", "adminRegisteration", true);
        httpreg.send(formdata);
    }

}

function deleteadmin(email) {
    alert(email);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.response);
            window.location.href = 'adminview'
        }
    };
    xml.open('GET', 'adminDelete?email=' + email, true);
    xml.send()
}

function updatemodel(data) {
    // alert(data);
    $('#email').val(data.email);
    $('#fname').val(data.type);
    $('#mobile').val(data.mobile);
    // $('#email').val(data.password);
    $('#updateadminmodel').modal('show');
}


function updateAdmin() {
    var controls = document.getElementById("myform").elements;
    var formdata = new FormData();
    for (var i = 0; i < controls.length; i++) {
        if (controls[i].type == "file") {
            formdata.append(controls[i].name, controls[i].files[0]);
        } else {
            formdata.append(controls[i].name, controls[i].value);
        }
    }
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.responseText);
            $('#updateadminmodel').modal('hide');
            window.location.href = 'adminview';
        }
    };
    xml.open('POST', 'adminUpdate', true);
    xml.send(formdata)
}

function forgetpassword(status) {
    var formdata = new FormData();
    var xml = new XMLHttpRequest();
    var output = '';
    if (status == 'admin') {
        if (document.getElementById('otpemail').value != "" && document.getElementById('otpphone').value != "") {
            formdata.append('status', status);
            formdata.append('email', document.getElementById('otpemail').value);
            formdata.append('phone', document.getElementById('otpphone').value);
            xml.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    output = this.response;
                    if (output == 'None') {
                        document.getElementById('otperror').innerHTML = '<div class="alert alert-danger" role="alert">' + output + '</div>'

                    } else {
                        $('#forgetadminpassword').modal('hide');
                        window.location.href = 'forgetpage'
                    }
                    // $('#mymodalchangepassword').modal('hide');
                    // window.location.href = 'adminview';
                }
            };
            xml.open('POST', 'forgetpassword', true);
            xml.send(formdata)

        } else if (document.getElementById('otpemail').value != "") {
            alert(document.getElementById('otpemail').value);
            formdata.append('status', status);
            formdata.append('email', document.getElementById('otpemail').value);
            xml.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    output = this.response;
                    if (output == 'None') {
                        document.getElementById('otperror').innerHTML = '<div class="alert alert-danger" role="alert">' + output + '</div>'
                    } else {
                        $('#forgetadminpassword').modal('hide');
                        window.location.href = 'forgetpage'
                    }
                    // $('#mymodalchangepassword').modal('hide');
                    // window.location.href = 'adminview';
                }
            };
            xml.open('POST', 'forgetpassword', true);
            xml.send(formdata)

        } else if (document.getElementById('otpphone').value != "") {
            alert(document.getElementById('otpphone').value);
            formdata.append('status', status);
            formdata.append('phone', document.getElementById('otpphone').value);
            xml.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    output = this.response;
                    if (output == 'None') {
                        document.getElementById('otperror').innerHTML = '<div class="alert alert-danger" role="alert">' + output + '</div>'
                    } else {
                        $('#forgetadminpassword').modal('hide');
                        window.location.href = 'forgetpage'
                    }
                    // $('#mymodalchangepassword').modal('hide');
                    // window.location.href = 'adminview';
                }
            };
            xml.open('POST', 'forgetpassword', true);
            xml.send(formdata)
        } else {
            document.getElementById('otperror').innerHTML = '<div class="alert alert-danger">Please Fill any field</div>'
        }
    }
}

function deletemovie(vid, vidname) {
    var output = confirm('Are You Sure U Want To delete?');
    if (output == true) {
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                alert(this.response);
                window.location.href = 'movie'
            }
        };
        xml.open('GET', 'deletemovie?vid=' + vid + "&vidname=" + vidname, true);
        xml.send()
    }
}

function deletetheater(vid, vidname) {
    var output = confirm('Are You Sure U Want To delete?');
    if (output == true) {
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                alert(this.response);
                window.location.href = 'theater'
            }
        };
        xml.open('GET', 'deletetheater?vid=' + vid + "&vidname=" + vidname, true);
        xml.send()
    }
}


function deleteMerchandise(vid, vidname) {
    var output = confirm('Are You Sure U Want To delete?');
    if (output == true) {
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                alert(this.response);
                window.location.href = 'merchandise'
            }
        };
        xml.open('GET', 'deleteMerchandise?vid=' + vid + "&vidname=" + vidname, true);
        xml.send()
    }
}


function updatemoviemodel(data) {
    $('#umoviename').val(data.moviename);
    $('#udescription').val(data.description);
    $('#udirection').val(data.direction);
    $('#uphouse').val(data.productionhouse);
    $('#ugenre').val(data.genre);
    $('#ureleaseDate').val(data.dateofrelease);
    $("#uphoto").attr({"src": "static/media/" + data.coverphoto});
    $('#umovieid').val(data.movieid);
    $('#updatemoviemodel').modal('show');

}

function updatevideos() {
    var controls = document.getElementById("myformeditmodal").elements;
    var formdata = new FormData();
    for (var i = 0; i < controls.length; i++) {
        if (controls[i].type == "file") {
            formdata.append(controls[i].name, controls[i].files[0]);
        } else {
            formdata.append(controls[i].name, controls[i].value);
        }
    }
    var httpreg = new XMLHttpRequest();
    httpreg.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var output = this.response;
            alert(output);
            if (output == 'success') {
                $("#myModaleditvideo").modal('hide');
                window.location.href = 'viewMovies'
            } else {
                document.getElementById('error').innerHTML = 'Something is wrong. Try After sometimes!!'
            }
            // window.location.href = '';
        }

    };
    httpreg.open("POST", "updatevideos", true);
    httpreg.send(formdata);

}

function deleteshow(showid, moviename) {
    var output = confirm('Are You Sure U Want To delete?');
    if (output == true) {
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                alert(this.response);
                window.location.href = 'show'
            }
        };
        xml.open('GET', 'deleteshow?showid=' + showid + "&moviename=" + moviename, true);
        xml.send()
    }
}

function showtimingsmodel(showid) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var outptut = JSON.parse(this.response)
            $('#showid').val(showid);
            if (outptut == '') {
                document.getElementById('tdata').innerHTML = '<tr><td colspan="6" class="text-dark font-weight-bolder h1 text-center">No Show</td></tr>'
            } else {
                table(outptut)
            }
            $('#myModal').modal('show');
        }
    };
    xml.open('GET', 'showtimingsview?showid=' + showid, true)
    xml.send()
}

function deleteshowtime(showtimeid,showid) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var outptut = JSON.parse(this.response)
            table(outptut);
        }
    };
    xml.open('GET', 'deleteshowtime?showtimeid=' + showtimeid+"&showid="+showid, true)
    xml.send()
}

function table(outptut) {
    var t = ''
    for (var i = 0; i < outptut.length; i++) {
        // console.log(i)
        t += `<tr>`
        t += `<td>${outptut[i]['id']}</td>`
        t += `<td>${outptut[i]['audi']}</td>`
        t += `<td>${outptut[i]['price']}</td>`
        t += `<td>${outptut[i]['showdate']}</td>`
        t += `<td>${outptut[i]['showtime']}</td>`
        t += `<td class="text-center"><button class="btn btn-danger" onclick="deleteshowtime(JSON.stringify(${outptut[i]['id']}),JSON.stringify(${outptut[i]['showid']}))"><i class="fa fa-trash"></i></button></td>`
        t += `</tr>`
    }
    document.getElementById('tdata').innerHTML = t
}


function addshowtimingsubmit() {
    var form = $('#addshowtiming').valid();
    if (form == true) {
        var controls = document.getElementById("addshowtiming").elements;
        var formdata = new FormData();
        for (var i = 0; i < controls.length; i++) {
            if (controls[i].type == "file") {
                formdata.append(controls[i].name, controls[i].files[0]);
            } else {
                formdata.append(controls[i].name, controls[i].value);
            }
        }
        var httpreg = new XMLHttpRequest();
        httpreg.onreadystatechange = function () {
            if (this.status == 200 && this.readyState == 4) {
                var output = JSON.parse(this.response);
                $("#price").val('');
                $("#time").val('');
                table(output)
            }
        };
        httpreg.open("POST", "addshowtimingsubmit", true);
        httpreg.send(formdata);
    }
}


function changeadminpassword() {
    var controls = document.getElementById("adminChangePassword").elements;
    var formdata = new FormData();
    for (var i = 0; i < controls.length; i++) {
        if (controls[i].type == "file") {
            formdata.append(controls[i].name, controls[i].files[0]);
        } else {
            formdata.append(controls[i].name, controls[i].value);
        }
    }
    var httpreg = new XMLHttpRequest();
    httpreg.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var output = this.response;
            // alert(output);
            if (output == 'success') {
                $("#mymodalchangepassword").modal('hide');
            } else {
                document.getElementById('error').innerHTML = output;
                document.getElementById('adminChangePassword').reset()
            }
        }

    };
    httpreg.open("POST", "adminChangePassword", true);
    httpreg.send(formdata);
}

