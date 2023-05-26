import {save_in_history} from "./history.js";


function ajax_delete(tr) {
    $.ajax({
        method: 'post',
        url: delete_product_view,
        data: {'delete_id': tr[0].dataset.productId},
    });
}

$(document).ready(function() {
    $(document).on("click", ".delete-btn", function(){
        let tr = $(this).parents("tr").first();
        $().click(ajax_delete(tr));
        $(".creating-beg").removeAttr("disabled");
        $().click(save_in_history(tr, 'delete'));
        tr.remove();
    });
});