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
    $(document).on("click", ".update", function () {
        let tr = $(this).parents("tr");
        ajaxUpdate(tr);

        tr.find("td:not(:last-child)").each(function () {
            $(this).html('<input type="text" class="form-control" value="' + $(this).text() + '">');
        });

        $(this).parents("tr").find(".create, .update").toggle();
        $(".create-new").attr("disabled", "disabled");
    });
});