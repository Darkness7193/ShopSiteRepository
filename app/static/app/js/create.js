function ajaxCreate() {
	$.ajax({
		method: 'post',
		url: create_product_view,
		data: {
			'name': $('name')[0].value,
			'price': $('price')[0].value,
			'decription': $('description')[0].value,
			'count': $('count')[0].value,
		},
	});
}


$(document).ready(function(){
    $(document).on("click", ".create-btn", function(){
		let empty = false;
		let tr = $(this).parents("tr");
		let input = tr.find('input[type="text"]');

        input.each(function(){
			if(!$(this).val()){
				$(this).addClass("error");
				empty = true;
			} else{
                $(this).removeClass("error");
            }
		});
		tr.find(".error").first().focus();

		if(!empty){

			input.each(function(){
				$(this).parent("td").html($(this).val());
			});

			tr.find(".create-btn, .update-btn").toggle();
			$(".create-new").removeAttr("disabled");

        }
    });
});