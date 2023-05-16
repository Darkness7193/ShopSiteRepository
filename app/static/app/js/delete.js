function ajaxDelete(tr) {
    $.ajax({
        method: 'post',
        url: delete_product_view,
        data: {'delete_id': tr.attr("id")},
    });
}

$(document).ready(function() {
    $(document).on("click", ".delete-btn", function(){
        let tr = $(this).parents("tr");
        $().click(ajaxDelete(tr));
        $(".create-new").removeAttr("disabled");
        tr.remove();
    });
});