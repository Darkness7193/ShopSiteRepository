let actions_field = `
<td>
    <a class="create-btn" data-toggle="tooltip"><i class="material-icons">&#xE03B;</i></a>
    <a class="update-btn" data-toggle="tooltip"><i class="material-icons">&#xE254;</i></a>
    <a class="delete-btn" data-toggle="tooltip"><i class="material-icons">&#xE872;</i></a>
</td>
`;
let inputs_fields = `
	<td><input type="text" class="form-control" name="name-input" id="name-input"></td>
	<td><input type="text" class="form-control" name="price-input" id="price-input"></td>
	<td><input type="text" class="form-control" name="description-input" id="description-input"></td>
	<td><input type="text" class="form-control" name="count-input" id="count-input"></td>
`;


$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
    $(document).on("click", ".create-new", function(){
		$(this).attr("disabled", "disabled");
		let index = $("table tbody tr:last-child").index();

        let row = `<tr> ${inputs_fields} ${actions_field} </tr>`;
    	$("table").append(row);

		$("table tbody tr").eq(index + 1).find(".create-btn, .update-btn").toggle();
        $('[data-toggle="tooltip"]').tooltip();
    });
});