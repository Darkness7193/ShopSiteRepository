$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	let actions = `
	    <a class="add" title="Add" data-toggle="tooltip"><i class="material-icons">&#xE03B;</i></a>
        <a class="edit" title="Edit" data-toggle="tooltip"><i class="material-icons">&#xE254;</i></a>
        <a class="delete" title="Delete" data-toggle="tooltip"><i class="material-icons">&#xE872;</i></a>
    `;
    $(document).on("click", ".add-new", function(){
		$(this).attr("disabled", "disabled");
		let index = $("table tbody tr:last-child").index();
        let row = `<tr>
            <td><input type="text" class="form-control" name="name" id="name"></td>
            <td><input type="text" class="form-control" name="price" id="price"></td>
            <td><input type="text" class="form-control" name="description" id="description"></td>
            <td><input type="text" class="form-control" name="count" id="count"></td>
			<td>` + actions + `</td>
        </tr>`;
    	$("table").append(row);
		$("table tbody tr").eq(index + 1).find(".add, .edit").toggle();
        $('[data-toggle="tooltip"]').tooltip();

    });
	$(document).on("click", ".add", function(){
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
			input.each(function(){
				$(this).parent("td").html($(this).val());
			});
			tr.find(".add, .edit").toggle();
			$(".add-new").removeAttr("disabled");
            `
            $.ajax({
                method: 'post',
                url: '{% url 'create_product' %}',
                data: {
                    'edit_id':tr.attr("id"),
                    'name': document.getElementsById('name').textContent,
                    'price': document.getElementsById('price').textContent,
                    'disctription': document.getElementsById('description').textContent,
                    'count': document.getElementsById('count').textContent
                },
            });
            `
        }
    });
	$(document).on("click", ".edit", function(){
        let tr = $(this).parents("tr");
        tr.find("td:not(:last-child)").each(function(){
			$(this).html('<input type="text" class="form-control" value="' + $(this).text() + '">');
		});
		$(this).parents("tr").find(".add, .edit").toggle();
		$(".add-new").attr("disabled", "disabled");
        `
        $.ajax({
            method: 'post',
            url: '{% url 'edit_product' %}',
            data: {
                'edit_id':tr.attr("id"),
                'fields': tr.textContent,
            },
        });
        `
    });
	$(document).on("click", ".delete", function(){
        let tr = $(this).parents("tr");
        `
        $.ajax({
            method: 'post',
            url: '{% url 'delete_product' %}',
            data: {'delete_id':tr.attr("id")},
        });
        `
        tr.remove();
        $(".add-new").removeAttr("disabled");
    });
});