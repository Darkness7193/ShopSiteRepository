let inputs_tr = `
<tr id="inputs_tr">
	<td><input type="text" class="field-changer" name="name" id="name"></td>
	<td><input type="text" class="field-changer" name="price" id="price"></td>
	<td><input type="text" class="field-changer" name="description" id="description"></td>
	<td><input type="text" class="field-changer" name="count" id="count"></td>
	<td>
	    <a class="create-btn"><i class="material-icons">&#xE03B;</i></a>
	    <a class="update-btn"><i class="material-icons">&#xE254;</i></a>
	    <a class="delete-btn"><i class="material-icons">&#xE872;</i></a>
	</td>
</tr>
`;

$(document).ready(function(){
    $(document).on("click", ".creating-beg", function(){
		create_mode = "create";
    	$("table").append(inputs_tr);

		$("#inputs_tr").find(".create-btn, .update-btn").toggle();

		$(this).attr("disabled", "disabled");
    });
});