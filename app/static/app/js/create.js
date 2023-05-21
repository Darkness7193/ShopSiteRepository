function ajaxCreate() {
	let inputs_data = {};
	let inputs = $('input[class=record-changer]');
	inputs.each( function(){
		let name = $(this)[0].getAttribute('name');
		inputs_data[name] = $(this)[0].value;
	});
	$.ajax({
		method: 'post',
		url: create_product_view,
		data: inputs_data,
	});
}

function ajaxUpdate(tr) {
	let inputs_data = {'update_id': tr.attr("id")};
	let inputs = $('input[class=record-changer]');
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

		if (is_empty(inputs)) {
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