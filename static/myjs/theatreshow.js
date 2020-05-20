function selectWithIndex(elmsel, name) {
    var selects = document.querySelectorAll(elmsel);
    var arrSel = [...selects]
    arrSel.forEach((v => {
        f(v)
    }))

    function f(el) {
        var iArr = []
        var select = el
        for (var i = 0; i < select.children.length; i++) {
            iArr.push(select.children[i].innerHTML)
        }
        // console.log(select)
        select.selectedIndex = iArr.indexOf(name)
    }
}

function editmodal(data) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response);
            selectWithIndex('#movieidedit', output.moviename);
            selectWithIndex('#audiedit', output.audi);
            $('#showdateedit').val(output.showdate)
            $('#priceedit').val(output.price)
            // $('#showtimeedit').val(output.showtime);
            $('#id').val(output.id);
            $('#exampleModal').modal('show')
        }
    };
    xml.open('GET', 'editshowdata?id=' + data, true);
    xml.send()
}
