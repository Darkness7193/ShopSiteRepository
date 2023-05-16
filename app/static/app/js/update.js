function ajaxUpdate(tr) {
    $.ajax({
        method: 'post',
        url: update_product_view,
        data: {
            'update_id':tr.attr("id"),
            'fields': tr.textContent,
        },
    });
}


$(document).ready(function() {
    $(document).on("click", ".update-btn", function () {
        let tr = $(this).parents("tr");

        tr.find("td:not(:last-child)").each(function () {
            $(this).html('<input type="text" class="form-control" value="' + $(this).text() + '">');
        });

        tr.find(".create-btn, .update-btn").toggle();
        $(".create-new").attr("disabled", "disabled");
    });
});