function ajaxCreate() {
	$.ajax({
		method: 'post',
		url: create_product_view,
		data: {
			'name': $('#name-input')[0].value+'aC,',
			'price': $('#price-input')[0].value,
			'description': $('#description-input')[0].value,
			'count': $('#count-input')[0].value,
		},
	});
}


$(document).ready(function(){
    $(document).on("click", ".create-btn", function(){
		console.log('create');
		let empty = false;
		let tr = $(this).parents("tr");
		let inputs = tr.find('input[type="text"]');

        inputs.each(function(){
			if(!$(this).val()){
				$(this).addClass("error");
				empty = true;
			} else{
                $(this).removeClass("error");
            }
		});

		if (empty) {
			tr.find(".error").first().focus();
		}
		else {
			$().click(ajaxCreate());
			console.log($('#name-input'));

			inputs.each(function(){
				$(this).parent("td").html($(this).val());
			});

			tr.find(".create-btn, .update-btn").toggle();
			$(".create-new").removeAttr("disabled");
        }
    });
});