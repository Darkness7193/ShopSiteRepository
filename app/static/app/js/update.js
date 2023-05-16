function ajaxUpdate(tr) {
    $.ajax({
        method: 'post',
        url: update_product_view,
        data: {
            'update_id': tr.attr("id"),
			'name': $('#name-input')[0].value,
			'price': $('#price-input')[0].value,
			'description': $('#description-input')[0].value,
			'count': $('#count-input')[0].value,
        },
    });
}


$(document).ready(function() {
    $(document).on("click", ".update-btn", function () {
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

        //$().click(ajaxUpdate(tr));
        tr.find(".create-btn, .update-btn").toggle();
        $(".create-new").attr("disabled", "disabled");
    });
});