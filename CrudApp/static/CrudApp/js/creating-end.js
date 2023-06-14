import {save_in_history} from "./history.js";


function get_inputs_data() {
	let inputs_data = {};
	let inputs = $('.field-changer');
	inputs.each( function(){
		let name = $(this)[0].getAttribute('name');
		inputs_data[name] = $(this)[0].value;
	});
	return inputs_data;
}


function ajax_create(tr) {
	$.ajax({
		method: 'post',
		url: create_product_view,
		data: get_inputs_data(),
		async: false,
		success: function(data) {
			tr[0].dataset.productId = data['new_product_id'];
		},
	});
}

function ajax_update(tr) {
	let data = get_inputs_data();
	data['update_id'] = tr[0].dataset.productId;
    $.ajax({
        method: 'post',
        url: update_product_view,
        data: data,
    });
}

function is_empty(inputs) {
	let empty = false;
	inputs.reverse().each(function(){
		let text = $(this).val();
		if (!text) {
			$(this).addClass("is-empty");
			$(this).first().focus();
			empty = true;
		} else {
		    $(this).removeClass("is-empty");
		}
	});
	return empty
}

$(document).ready(function(){
    $(document).on("click", ".creating-end-btn", function(){

		let tr = $(this).parents("tr").first();
		let inputs = $(".field-changer");

		if (!is_empty(inputs)) {
			if (create_mode === "create") {
				$().click(ajax_create(tr));
			} else if (create_mode=== "update") {
				$().click(ajax_update(tr));
			}

			inputs.each(function(){
				$(this).parent("td").html($(this).val());
			});

			tr.find(".creating-end-btn, .update-btn").toggle();
			$(".creating-beg").removeAttr("disabled");
			tr.removeAttr("id");

			$().click(save_in_history(tr, create_mode));
        }
    });
});