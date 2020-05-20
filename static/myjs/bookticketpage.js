function clickme(i) {
    var totalprice;
    var img1 = document.getElementById(i).src;
    if (img1 == 'http://127.0.0.1:8000/static/media/icon/unbooked.svg') {
        document.getElementById(i).src = 'http://127.0.0.1:8000/static/media/icon/selectseat.svg';
        document.getElementById(i).classList.add("selected")
    } else {
        document.getElementById(i).src = 'http://127.0.0.1:8000/static/media/icon/unbooked.svg';
        document.getElementById(i).classList.remove("selected")
    }
    var selected = document.getElementsByClassName("selected")
    document.getElementById('noofseats').innerHTML = selected.length
    totalprice = parseInt(document.getElementById('price').value) * selected.length;
    document.getElementById('grandtotaldiv').innerHTML = '&#8377; ' + totalprice;
    $('#grandtotal').val(totalprice);
}

function submitseat() {
    var selected = document.getElementsByClassName("selected");
    if (selected.length < 1) {
        alert('Please Select Ur Seats')
    } else {
        var arr = [];
        for (var i = 0; i < selected.length; i++) {
            arr.push(selected[i].id)
        }
        var formdata = new FormData()
        formdata.append('seat', arr)
        formdata.append('numberofseat', arr.length)
        formdata.append('showtimeid', $('#showtimeid').val());
        formdata.append('grandtotal', $('#grandtotal').html());
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                if (output == 'success') {
                    alert('good')
                } else {
                    alert('not good')
                }
            }
        };
        xml.open('POST', 'seatselected', true);
        xml.send(formdata)
    }
}

function audi1(showtimeid) {
    // alert(showtimeid)
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var outputs = JSON.parse(this.response);
            // console.log(outputs)
            var t = ''
            var totalseat = 300;
            var upperseat = (totalseat / 4) * 3;
            var groundhall = totalseat / 4;
            var isDisable = false;
            for (var i = 1; i <= upperseat; i++) {
                isDisable = false;
                for (var a = 0; a < outputs.length; a++) {
                    // console.log(outputs[a])
                    if (i == outputs[a]) {
                        t += `<div class="seat"><img src="http://127.0.0.1:8000/static/media/icon/bookedseat.svg" id="${i}" class="img-fluid"><p>${i}</p></div>`;
                        isDisable = true
                        break;
                    }
                }
                if (isDisable == false) {
                    t += `<div class="seat" onclick="clickme(${i})"><img src="http://127.0.0.1:8000/static/media/icon/unbooked.svg" id="${i}" class="img-fluid"><p>${i}</p></div>`;
                }

            }

            t += `<br><br>`;
            for (var j = upperseat + 1; j <= totalseat; j++) {
                isDisable = false;
                for (var a = 0; a < outputs.length; a++) {
                    console.log(outputs[a])
                    if (i == outputs[a]) {
                        t += `<div class="seat"><img src="http://127.0.0.1:8000/static/media/icon/bookedseat.svg" id="${i}" class="img-fluid"><p>${i}</p></div>`;
                        isDisable = true
                        break;
                    }
                }
                if (isDisable == false) {

                    t += `<div class="seat" onclick="clickme(${i})"><img src="http://127.0.0.1:8000/static/media/icon/unbooked.svg" id="${i}" class="img-fluid"><p>${i}</p></div>`;
                }
            }
            document.getElementById('seatchair').innerHTML = t;
        }
    };
    xml.open('GET', 'selectedseat?showtimeid=' + showtimeid, true)
    xml.send()
}

function seatchair(showtimeid) {
    alert(showtimeid)
    var totalseat = 26;
    var cout = 4
    var t = ''
    var seatid = 0
    while (true) {
        if (cout >= totalseat) {
            break
        }
        console.log(cout);
        var daft = 1
        t += `<div class="row"><div class="col-sm-12 text-center">`
        for (var i = cout; i >= daft; i--) {
            if (i > totalseat) {
                break
            }
            seatid = seatid + 1
            t += `<div class="seat"><img src="http://127.0.0.1:8000/static/media/icon/unbooked.svg"  style="width: 40px!important;height: 30px!important;" class="img-fluid"><p>${seatid}</p></div>`;
        }
        t += `</div></div>`
        cout = cout + 4
    }
    document.getElementById('seatchair').innerHTML = t;
}


function audi2(showtimeid) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var outputs = JSON.parse(this.response);
            var totalseat = 210;
            var t = ''
            var isDisable = false;
            // var half = totalseat / 2
            var count = 0;
            t = '';
            console.log(outputs)
            for (var i = 1; i <= totalseat; i = i + 14) {
                count = i
                t += `<div class="row">`
                t += `<div class="col-sm-4 text-center">`
                for (var j = count; j < count + 4; j++) {
                    isDisable = false;
                    if (j > totalseat) {
                        break
                    } else {
                        for (var a = 0; a < outputs.length; a++) {
                            // console.log(outputs[a])
                            if (outputs[a] == j) {
                                t += `<div class="seat"><img src="http://127.0.0.1:8000/static/media/icon/bookedseat.svg" id="${j}" style="width: 50px!important;height: 50px!important;" class="img-fluid"><p>${j}</p></div>`;
                                isDisable = true
                                break;
                            }
                        }
                        if (isDisable == false) {
                            t += `<div class="seat" onclick="clickme(${j})"><img src="http://127.0.0.1:8000/static/media/icon/unbooked.svg" id="${j}" style="width: 50px!important;height: 50px!important;" class="img-fluid"><p>${j}</p></div>`;
                        }
                    }
                }
                t += `</div>`
                t += `<div class="col-sm-4 text-center">`
                for (var r = count + 4; r < count + 10; r++) {
                    isDisable = false;
                    if (r > totalseat) {
                        break
                    } else {
                        for (var a = 0; a < outputs.length; a++) {
                            console.log(outputs[a])
                            if (outputs[a] == r) {
                                t += `<div class="seat"><img src="http://127.0.0.1:8000/static/media/icon/bookedseat.svg" id="${r}" style="width: 50px!important;height: 50px!important;" class="img-fluid"><p>${r}</p></div>`;
                                isDisable = true
                                break;
                            }
                        }
                        if (isDisable == false) {
                            t += `<div class="seat" onclick="clickme(${r})"><img src="http://127.0.0.1:8000/static/media/icon/unbooked.svg" id="${r}" style="width: 50px!important;height: 50px!important;" class="img-fluid"><p>${r}</p></div>`;
                        }
                    }
                }
                t += `</div>`
                t += `<div class="col-sm-4 text-center">`
                for (var k = count + 10; k < count + 14; k++) {
                    isDisable = false;
                    if (k > totalseat) {
                        break
                    } else {
                        for (var a = 0; a < outputs.length; a++) {
                            // console.log(a)
                            if (outputs[a] == k) {
                                t += `<div class="seat"><img src="http://127.0.0.1:8000/static/media/icon/bookedseat.svg" id="${k}" style="width: 50px!important;height: 50px!important;" class="img-fluid"><p>${k}</p></div>`;
                                isDisable = true
                                break;
                            }
                        }
                        if (isDisable == false) {
                            t += `<div class="seat" onclick="clickme(${k})"><img src="http://127.0.0.1:8000/static/media/icon/unbooked.svg" id="${k}" style="width: 50px!important;height: 50px!important;" class="img-fluid"><p>${k}</p></div>`;
                        }
                    }
                }
                t += `</div>`
                t += `</div>`
            }
            document.getElementById('seatchair').innerHTML = t;
        }
    };
    xml.open('GET', 'selectedseat?showtimeid=' + showtimeid, true)
    xml.send()
}


function audi3(showtimeid) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var outputs = JSON.parse(this.response);
            var totalseat = 204;
            var t = ''
            var half = totalseat / 2
            var count = 0;
            var isDisable = false;
            t = '';
            for (var i = 1; i <= totalseat; i = i + 12) {
                count = i
                t += `<div class="row">`
                t += `<div class="col-sm-6 text-center">`
                for (var j = count; j < count + 6; j++) {
                    isDisable = false;
                    if (j > totalseat) {
                        break
                    } else {
                        for (var a = 0; a < outputs.length; a++) {
                            if (outputs[a] == j) {
                                t += `<div class="seat"><img src="http://127.0.0.1:8000/static/media/icon/bookedseat.svg" id="${j}" style="width: 73px!important;height: 73px!important;" class="img-fluid"><p>${j}</p></div>`;
                                isDisable = true
                                break;
                            }
                        }
                        if (isDisable == false) {
                            t += `<div class="seat" onclick="clickme(${j})"><img src="http://127.0.0.1:8000/static/media/icon/unbooked.svg" id="${j}" style="width: 73px!important;height: 73px!important;" class="img-fluid"><p>${j}</p></div>`;
                        }
                    }
                }
                t += `</div>`
                t += `<div class="col-sm-6 text-center">`
                for (var k = count + 6; k < count + 12; k++) {
                    isDisable = false
                    if (k > totalseat) {
                        break
                    } else {
                        for (var a = 0; a < outputs.length; a++) {
                            if (outputs[a] == k) {
                                t += `<div class="seat"><img src="http://127.0.0.1:8000/static/media/icon/bookedseat.svg" id="${k}"  style="width: 73px!important;height: 73px!important;" class="img-fluid"><p>${k}</p></div>`;
                                isDisable = true
                                break;
                            }
                        }
                        if (isDisable == false) {
                            t += `<div class="seat" onclick="clickme(${k})"><img src="http://127.0.0.1:8000/static/media/icon/unbooked.svg" id="${k}"  style="width: 73px!important;height: 73px!important;" class="img-fluid"><p>${k}</p></div>`;
                        }
                    }
                }
                t += `</div>`
                t += `</div>`
            }
            document.getElementById('seatchair').innerHTML = t;
        }
    };
    xml.open('GET', 'selectedseat?showtimeid=' + showtimeid, true)
    xml.send()
}


function paymentticket() {
    var selected = document.getElementsByClassName("selected");
    if (selected.length < 1) {
        alert('Please Select Ur Seats')
    } else {
        var arr = [];
        for (var i = 0; i < selected.length; i++) {
            arr.push(selected[i].id)
        }
        var amount = parseInt($('#grandtotal').val()) * 100;
        var options = {
            "key": "rzp_test_dRWiKHS7zr2Gki",
            "amount": amount,
            "name": "Movie & Merchandise",
            "description": "Student Project",
            "image": "https://i1.wp.com/www.heyuguys.com/images/2016/05/angry-birds-correct.png?fit=800%2C400&ssl=1",
            "handler": function (response) {
                //alert(response.razorpay_payment_id);
                if (response.razorpay_payment_id == "") {
                    // alert('Failed');
                    window.location.href = "failedPaymentticket";
                } else {
                    var formdata = new FormData();
                    formdata.append('seat', arr)
                    formdata.append('numberofseat', arr.length)
                    formdata.append('showtimeid', $('#showtimeid').val());
                    formdata.append('grandtotal', $('#grandtotal').val());
                    var httpreg = new XMLHttpRequest();
                    httpreg.onreadystatechange = function () {
                        if (this.status == 200 && this.readyState == 4) {
                            var output = this.response;
                            console.log(output);
                            window.location.href = "thankticketbook?thicketid=" + output;
                        }

                    };
                    httpreg.open("POST", "seatselected", true);
                    httpreg.send(formdata);
                }
            },
            "prefill": {
                "name": "",
                "email": $('#disemail').val(),
                "contact": $('#disphone').val()
            },
            "notes": {
                "address": ""
            },
            "theme": {
                "color": "#54f3ce"
            }
        };
        var rzp1 = new Razorpay(options);
        rzp1.open();
    }
}