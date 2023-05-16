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
			//$().click(ajaxCreate());
			console.log($('#name-input'));

			inputs.each(function(){
				$(this).parent("td").html($(this).val());
			});

			tr.find(".create-btn, .update-btn").toggle();
			$(".create-new").removeAttr("disabled");
        }
    });
});