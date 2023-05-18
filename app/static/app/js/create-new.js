let input_tr = `
	<td><input type="text" class="form-control" name="name-input" id="name-input"></td>
	<td><input type="text" class="form-control" name="price-input" id="price-input"></td>
	<td><input type="text" class="form-control" name="description-input" id="description-input"></td>
	<td><input type="text" class="form-control" name="count-input" id="count-input"></td>
	<td>
	    <a class="create-btn"><i class="material-icons">&#xE03B;</i></a>
	    <a class="update-btn"><i class="material-icons">&#xE254;</i></a>
	    <a class="delete-btn"><i class="material-icons">&#xE872;</i></a>
	</td>
`;

$(document).ready(function(){
    $(document).on("click", ".create-new", function(){
		create_mode = "create";
    	$("table").append(`<tr> ${input_tr} </tr>`);

		$("table tbody tr:last-child").find(".create-btn, .update-btn").toggle();

		$(this).attr("disabled", "disabled");
    });
});