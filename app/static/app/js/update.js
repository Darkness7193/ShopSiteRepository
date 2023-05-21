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
            let name = headers[field].id;
            $(this).html(`<input 
                type="text" 
                class="record-changer" 
                value="${$(this).text()}"
                name="${name}"
                id="${name}"
            >`);
        });

        tr.find(".create-btn, .update-btn").toggle();
        $(".create-new").attr("disabled", "disabled");
    });
});