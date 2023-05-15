let actions = `
    <a class="create" title="Create" data-toggle="tooltip"><i class="material-icons">&#xE03B;</i></a>
    <a class="edit" title="Edit" data-toggle="tooltip"><i class="material-icons">&#xE254;</i></a>
    <a class="delete" title="Delete" data-toggle="tooltip"><i class="material-icons">&#xE872;</i></a>
`;


$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
    $(document).on("click", ".create-new", function(){
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
		$("table tbody tr").eq(index + 1).find(".create, .edit").toggle();
        $('[data-toggle="tooltip"]').tooltip();
    });
});