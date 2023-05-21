function createInput(id, text) {
    return `<input 
        type="text" 
        class="field-changer" 
        value="${text}"
        name="${id}"
        id="${id}"
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
        tr.find(fields).each(function (field) {
            $(this).html(createInput(headers[field].id, $(this).text()));
        });

        tr.find(".create-btn, .update-btn").toggle();
        $(".creating-beg").attr("disabled", "disabled");
    });
});