


$(document).ready(function() {
    $(document).on("click", ".update-btn", function () {
        create_mode = "update";
        let tr = $(this).parents("tr");

        let headers = $('th');
        tr.find("td:not(:last-child)").each(function (field) {
            let name = headers[field].id+'-input';
            $(this).html(`<input 
                type="text" 
                class="form-control" 
                value="${$(this).text()}"
                name="${name}"
                id="${name}"
            >`);
        });

        tr.find(".create-btn, .update-btn").toggle();
        $(".create-new").attr("disabled", "disabled");
    });
});