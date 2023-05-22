function ajaxCreate(tr) {
	let inputs_data = {};
	let inputs = $('input[class=field-changer]');
	inputs.each( function(){
		let name = $(this)[0].getAttribute('name');
		inputs_data[name] = $(this)[0].value;
	});
	$.ajax({
		method: 'post',
		url: create_product_view,
		data: inputs_data,
		success: function(data) {
			tr[0].setAttribute('data-product-id', data['new_product_id']);
		},
	});
}

function ajaxUpdate(tr) {
	let inputs_data = {'update_id': tr[0].dataset.productId};
	let inputs = $('input[class=field-changer]');
	inputs.each( function(){
		let name = $(this)[0].getAttribute('name');
		inputs_data[name] = $(this)[0].value;
	});
    $.ajax({
        method: 'post',
        url: update_product_view,
        data: inputs_data,
    });
}

function is_empty(inputs) {
	let empty = false;
	inputs.each(function(){
		let text = $(this).val();
		if (!text) {
			$(this).addClass("error");
			empty = true;
		} else {
		    $(this).removeClass("error");
		}
	});
	return empty
}

$(document).ready(function(){
    $(document).on("click", ".creating-end-btn", function(){

		let tr = $(this).parents("tr").first();
		let inputs = $(".field-changer");

		if (is_empty(inputs)) {
			tr.find(".error").first().focus();
		} else {
			if (create_mode === "create") {
				$().click(ajaxCreate(tr));
			} else if (create_mode=== "update") {
				$().click(ajaxUpdate(tr));
			}

			inputs.each(function(){
				$(this).parent("td").html($(this).val());
			});

			tr.find(".creating-end-btn, .update-btn").toggle();
			$(".creating-beg").removeAttr("disabled");
        }
    });
});