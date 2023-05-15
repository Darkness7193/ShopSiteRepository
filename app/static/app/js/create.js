function ajaxCreate(tr) {
	$.ajax({
		method: 'post',
		url: create_product_view,
		data: {
			'edit_id':tr.attr("id"),
			'name': document.getElementsById('name').textContent,
			'price': document.getElementsById('price').textContent,
			'discription': document.getElementsById('description').textContent,
			'count': document.getElementsById('count').textContent,
		},
	});
}


$(document).ready(function(){
    $(document).on("click", ".create", function(){
		let empty = false;
		let input = $(this).parents("tr").find('input[type="text"]');
        input.each(function(){
			if(!$(this).val()){
				$(this).addClass("error");
				empty = true;
			} else{
                $(this).removeClass("error");
            }
		});
		$(this).parents("tr").find(".error").first().focus();
		if(!empty){
            tr = $(this).parents("tr");
			$().click(ajaxCreate(tr));

			input.each(function(){
				$(this).parent("td").html($(this).val());
			});
			tr.find(".create, .edit").toggle();
			$(".create-new").removeAttr("disabled");

        }
    });
});