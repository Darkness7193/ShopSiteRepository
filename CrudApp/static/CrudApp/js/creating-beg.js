function bigger_than_zero(n) {
    if (n > 0) { return n;}
	else {       return 0;}
}


let inputs_tr = `
<tr id="inputs_tr">
	<td><input type="text" class="field-changer" name="name" id="name"></td>
	<td><input 
		class="field-changer" 
		name="price" 
		id="price"
		type="number" 
		oninput="this.value = bigger_than_zero(this.value)"
	></td>
	<td><input type="text" class="field-changer" name="description" id="description"></td>
	<td><input 
		class="field-changer" 
		name="count" 
		id="count"
		type="number" 
		step="1"
		oninput="this.value = bigger_than_zero(this.value)"
	></td>
	<td>
	    <a class="creating-end-btn"><i class="material-icons">&#xE03B;</i></a>
	    <a class="update-btn"><i class="material-icons">&#xE254;</i></a>
	    <a class="delete-btn"><i class="material-icons">&#xE872;</i></a>
	</td>
</tr>
`;

$(document).ready(function(){
    $(document).on("click", ".creating-beg", function(){
		create_mode = "create";
    	$(".crud-table").append(inputs_tr);

		$("#inputs_tr").find(".creating-end-btn, .update-btn").toggle();

		$(this).attr("disabled", "disabled");
    });
});