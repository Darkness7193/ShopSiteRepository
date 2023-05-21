function bigger_than_zero(n) {
    if (n > 0) { return n;}
	else       { return 0;}
}

function get_validation(header_id) {
    switch (header_id) {
        case 'price':
            return 'type="number" oninput="this.value = bigger_than_zero(this.value)"';
        case 'count':
            return 'type="number" step="1" oninput="this.value = bigger_than_zero(this.value)"';
        default:
            return 'type="text"';
    }
}

function createInput(header_id, text) {
    return `<input 
        class="field-changer" 
        value="${text}"
        name="${header_id}"
        id="${header_id}"
        ${get_validation(header_id)}
    >`
}

$(document).ready(function() {
    $(document).on("click", ".update-btn", function () {
        create_mode = "update";
        let fields;
        let tr = $(this).parents("tr");

        const user_status = JSON.parse(document.getElementById('user_status').textContent);
        if (user_status === "Администратор") {
            fields = "td:not(:last-child)";
        } else {
            fields = "td:nth-child(4)";
        }

        let headers = $('th');
        tr.find(fields).each(function (i) {
            $(this).html(createInput(headers[i].id, $(this).text()));
        });

        tr.find(".creating-end-btn, .update-btn").toggle();
        $(".creating-beg").attr("disabled", "disabled");
    });
});