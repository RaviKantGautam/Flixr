function tableseat(data) {
    var s = '';
    if (data.length <= 0) {
        console.log('wow');
        s = '<tr><td colspan="4" class="text-center display-4 font-weight-bold text-danger">Nothing to Show!</td></tr>'
    } else {
        for (var i of data) {
            s += `<tr><form id="${i['id']}" method="get">`;
            s += `<td>${i["id"]}</td>`;
            s += `<!--<td><input type="text" value="${i['id']}" readonly></td>-->`;
            s += `<td><input class="form-control" required name="seatnumber" type="text" id="${i['id']}seat" value="${i['seatnumber']}" readonly></td>`;
            s += `<td><input class="form-control" required name="price" id="${i['id']}price" type="number" min="1" max="1000" value="${i['price']}" readonly></td>`;
            s += `<td><input class="form-control" required name="auditoriumname" type="text" id="${i['id']}auditoriumname" value="${i['auditoriumname']}" readonly></td>`;
            s += `<td><input class="form-control" required name="auditoriumkey" type="text" id="${i['id']}auditoriumkey" value="${i['auditoriumkey']}" readonly></td>`;
            // s += `<td>${i["price"]}</td>`;
            s += `<td id="${i['id']}btn"><button id="${i['id']}btn" onclick="editseat(JSON.stringify(${i['id']}))" class="btn btn-primary"><i class="fa fa-edit"></i></button></td>`
            s += `<td><button type="button" onclick="deleteseat(JSON.stringify(${i['id']}))" class="btn btn-danger"><i class="fa fa-trash"></i></button></td>`
            s += `</form></tr>`
        }
    }
    // console.log(s);
    document.getElementById('tabledataseat').innerHTML = s;
}


function editseat(id) {
    document.getElementById(id + 'seat').readOnly = false;
    document.getElementById(id + 'price').readOnly = false;
    document.getElementById(id + 'auditoriumname').readOnly = false;
    document.getElementById(id + 'auditoriumkey').readOnly = false;
    document.getElementById(id + 'btn').innerHTML = `<button type="button" onclick="editseatchanges(${id})" class="btn btn-success"><i class="fa fa-check"></i></button>`;
}

function editseatchanges(id) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            if (output == 'success') {
                document.getElementById(id + 'seat').readOnly = true;
                document.getElementById(id + 'price').readOnly = true;
                document.getElementById(id + 'auditoriumname').readOnly = true;
                document.getElementById(id + 'auditoriumkey').readOnly = true;
                document.getElementById(id + 'btn').innerHTML = `<button onclick="editseat(${id})" class="btn btn-primary"><i class="fa fa-edit"></i></button>`;
            } else {
                alert(output);
            }
        }
    };
    xml.open('get', 'editseatchanges?id=' + id + "&seat=" + $('#' + id + 'seat').val() + "&price=" + $('#' + id + 'price').val() + "&auditoriumname=" + $('#' + id + 'auditoriumname').val() + "&auditoriumkey=" + $('#' + id + 'auditoriumkey').val(), true);
    xml.send()
}

function deleteseat(id) {
    var deleteconfirm = confirm('Are u sure Your Want To delete?');
    if (deleteconfirm) {
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = JSON.parse(this.response);
                table(output);
            }
        };
        xml.open('GET', 'deleteseat?id=' + id, true);
        xml.send()
    }
}

function mainseat(data) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            tableseat(JSON.parse(output));
        }
    };
    xml.open('GET', 'seatdata?data=' + data, true);
    xml.send()
}

function addseatsubmit() {
    var controls = document.getElementById("addseat").elements;
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
            var output = this.response;
            if (output == 'INVALID QUERY') {
                document.getElementById('addseaterror').innerHTML = `<span class="alert alert-danger m-3">Data Is not correct</span>`
            } else {
                document.getElementById('categoryname').value = "";
                document.getElementById('price').value = "";
                table(JSON.parse(output));
            }
        }
    };
    xml.open('POST', 'addseatsubmit', true);
    xml.send(formdata)

}