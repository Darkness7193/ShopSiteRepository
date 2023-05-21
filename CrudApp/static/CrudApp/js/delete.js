function ajaxDelete(tr) {
    $.ajax({
        method: 'post',
        url: delete_product_view,
        data: {'delete_id': tr[0].dataset.productId},
    });
}

$(document).ready(function() {
    $(document).on("click", ".delete-btn", function(){
        let tr = $(this).parents("tr").first();
        $().click(ajaxDelete(tr));
        $(".creating-beg").removeAttr("disabled");
        tr.remove();
    });
});