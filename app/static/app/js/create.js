function ajaxCreate() {
	$.ajax({
		method: 'post',
		url: create_product_view,
		data: {
			'name': $('#name-input')[0].value,
			'price': $('#price-input')[0].value,
			'description': $('#description-input')[0].value,
			'count': $('#count-input')[0].value,
		},
	});
}

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

function is_validated(inputs) {
	let empty = false;
	inputs.each(function(){
		if(!$(this).val()){
			$(this).addClass("error");
			empty = true;
		} else{
		    $(this).removeClass("error");
		}
	});
	return empty
}


$(document).ready(function(){
    $(document).on("click", ".create-btn", function(){
		let tr = $(this).parents("tr");
		let inputs = tr.find('input[type="text"]');

		if (is_validated(inputs)) {
			tr.find(".error").first().focus();
		} else {
			if (create_mode === "create") {
				$().click(ajaxCreate());
			} else if (create_mode=== "update") {
				$().click(ajaxUpdate(tr));
			}

			inputs.each(function(){
				$(this).parent("td").html($(this).val());
			});

			tr.find(".create-btn, .update-btn").toggle();
			$(".create-new").removeAttr("disabled");
        }
    });
});